#!/usr/bin/env python

import rospy
import rosmsg
import rostopic
import os
import re
from collections import defaultdict
import grpc_tools.protoc
from snapshot_ros_messages import snapshot_ros_messages
from utils import type_ros2pb, topic2service_name, parse_ros_type


frame_template = '''
from concurrent import futures
import time
import math
import logging

import grpc

import ros_pb2 as ros_pb
import ros_pb2_grpc as ros_grpc

import rostopic
import rospy
import threading
import time
import roslib.message


{classes}


def create_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
{add_servicers}
    return server
'''

add_servicer_template = 'ros_grpc.add_{servicer_class}_to_server({servicer_class}(), server)'

class_template = '''
class {servicer_class}(ros_grpc.{servicer_class}):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('{ros_type}')

    def Publish(self, pb_msg, context):
        print('pb_msg', pb_msg, context)

        if self.pub == None:
            self.pub = rospy.Publisher('{topic}', self.Msg, queue_size=10)

        ros_msg = self.Msg()
{copy_pb2ros}
        print('publishing', ros_msg)
        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {{'unsubscribed': False}}
        ros_messages = []

        def callback(ros_msg):
            print('ros in', ros_msg)
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('{topic}', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        print('sub', request, context)
        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
{copy_ros2pb}
                yield pb_msg
            rospy.sleep(0.01)
        print("over'n out")


'''

def add_tab(lines, tabs=1):
    return re.sub(r'^([^$])',  '    ' * tabs + '\\1', lines, flags=re.MULTILINE)


def generate_msg_copier(type_tree, ros_type, left='pb_msg', right='ros_msg', new_instance=True):
    result = ''
    package, typename, _ = parse_ros_type(ros_type)
    
    if new_instance:
        if package:
            if left.startswith('ros_'):
                result += '{} = roslib.message.get_message_class(\'{}/{}\')()\n'.format(
                    left, package, typename)
            else:
                result += '{} = ros_pb.{}.{}()\n'.format(left, package, typename)
        else:
            result += '{} = ros_pb.{}()\n'.format(left, typename)

    if type_tree[package][typename]:
        for fieldname, ros_type in type_tree[package][typename].items():
            package, typename, is_array = parse_ros_type(ros_type)

            is_complex = (
                type_tree[package] and type_tree[package][typename])

            if is_array:
                sub_left = '{}_'.format(left.split('.')[0])
                sub_right = '{}_'.format(right.split('.')[0])
                result += 'for {sub_right} in {right}.{fieldname}:\n'.format(
                    sub_right=sub_right, right=right, fieldname=fieldname)
                body = ''
                if is_complex:
                    body += generate_msg_copier(
                        type_tree, ros_type, sub_left, sub_right, True)
                    body += '{left}.{fieldname}.append({sub_left})\n'.format(
                        left=left, sub_left=sub_left, fieldname=fieldname)
                else:
                    body += '{left}.{fieldname}.append({sub_right})\n'.format(
                        left=left, sub_right=sub_right, fieldname=fieldname)
                result += add_tab(body)
            elif is_complex:
                sub_left = '{}.{}'.format(left, fieldname)
                sub_right = '{}.{}'.format(right, fieldname)
                result += generate_msg_copier(type_tree,
                                              ros_type, sub_left, sub_right, False)
            else:
                result += '{left}.{fieldname} = {right}.{fieldname}\n'.format(
                    left=left, right=right, fieldname=fieldname)

    return result


def generate_server(type_tree, topics):
    add_servicers = []
    servicer_classes = []
    for topic, ros_type in topics:
        # if not topic == '/tf':
        #     continue
        servicer_class = topic2service_name(topic) + 'Servicer'
        add_servicers.append(add_servicer_template.format(
            servicer_class=servicer_class))
        copy_ros2pb = generate_msg_copier(
            type_tree, ros_type, 'pb_msg', 'ros_msg', new_instance=True)
        copy_pb2ros = generate_msg_copier(
            type_tree, ros_type, 'ros_msg', 'pb_msg', new_instance=False)
        copy_ros2pb = add_tab(copy_ros2pb, 4)
        copy_pb2ros = add_tab(copy_pb2ros, 2)
        servicer_classes.append(class_template.format(
            servicer_class=servicer_class, ros_type=ros_type, topic=topic, copy_ros2pb=copy_ros2pb, copy_pb2ros=copy_pb2ros))

    return frame_template.format(add_servicers=add_tab('\n'.join(add_servicers)), classes='\n'.join(servicer_classes))

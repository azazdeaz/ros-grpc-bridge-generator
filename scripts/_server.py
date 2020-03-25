#!/usr/bin/env python

from concurrent import futures
import time
import math
import logging

import grpc

import generated.ros_pb2 as ros_pb
import generated.ros_pb2_grpc as ros_grpc

import rostopic
import rospy
import threading
import time
import roslib.message


def cb(data):
    print('I heard', data)


class tfServicer(ros_grpc.tfServicer):
    def __init__(self):
        self.pub = None
        self.sub = None
        self.Msg = roslib.message.get_message_class('tf2_msgs/TFMessage')

    def Publish(self, request, context):
        print('request', request, context)

        if self.pub == None:
            self.pub = rospy.Publisher('/tf', self.Msg, queue_size=10)

        msg = self.Msg()
        for pb_item in request.transforms:
            ros_item = roslib.message.get_message_class(
                'geometry_msgs/TransformStamped')()
            # ros_item.header = roslib.message.get_message_class(
            #     'std_msgs/Header')()
            ros_item.header.frame_id = pb_item.header.frame_id
            ros_item.header.stamp.secs = pb_item.header.stamp.secs
            ros_item.header.stamp.nsecs = pb_item.header.stamp.nsecs
            ros_item.header.seq = pb_item.header.seq
            ros_item.child_frame_id = pb_item.child_frame_id
            ros_item.transform.translation.x = pb_item.transform.translation.x
            ros_item.transform.translation.y = pb_item.transform.translation.y
            ros_item.transform.translation.z = pb_item.transform.translation.z
            ros_item.transform.rotation.x = pb_item.transform.rotation.x
            ros_item.transform.rotation.y = pb_item.transform.rotation.y
            ros_item.transform.rotation.z = pb_item.transform.rotation.z
            ros_item.transform.rotation.w = pb_item.transform.rotation.w
            msg.transforms.append(ros_item)
        print('publishing', msg)
        self.pub.publish(msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        unsubscribed = False
        stop_event = threading.Event()
        ros_messages = []

        def callback(ros_msg):
            print('ros in', ros_msg)
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/tf', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.undegister()

        context.add_callback(on_rpc_done)

        print('sub', request, context)
        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.tf2_msgs.TFMessage()
                for ros_item in ros_msg.transforms:
                    pb_item = ros_pb.geometry_msgs.TransformStamped()
                    pb_item.header.frame_id = ros_item.header.frame_id
                    pb_item.header.stamp.secs = ros_item.header.stamp.secs
                    pb_item.header.stamp.nsecs = ros_item.header.stamp.nsecs
                    pb_item.header.seq = ros_item.header.seq
                    pb_item.child_frame_id = ros_item.child_frame_id
                    pb_item.transform.translation.x = ros_item.transform.translation.x
                    pb_item.transform.translation.y = ros_item.transform.translation.y
                    pb_item.transform.translation.z = ros_item.transform.translation.z
                    pb_item.transform.rotation.x = ros_item.transform.rotation.x
                    pb_item.transform.rotation.y = ros_item.transform.rotation.y
                    pb_item.transform.rotation.z = ros_item.transform.rotation.z
                    pb_item.transform.rotation.w = ros_item.transform.rotation.w

                    pb_msg.transforms.append(pb_item)
                yield pb_msg
            rospy.sleep(0.01)
        print("over'n out")


def serve():
    rospy.init_node('grpc_ros_transit', anonymous=True)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ros_grpc.add_tfServicer_to_server(
        tfServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    rospy.spin()


if __name__ == '__main__':
    serve()

#!/usr/bin/env python

import rospy
import rosmsg
import rostopic
import os
import re
from collections import defaultdict
import grpc_tools.protoc
from snapshot_ros_messages import snapshot_ros_messages
from utils import type_ros2pb, topic2service_name
from generate_server import generate_server


service_template = """
service {service_name} {{
    rpc Publish({pb_type}) returns (Empty);
    rpc Subscribe(Empty) returns (stream {pb_type});
}}

"""

header = '''
syntax = 'proto3';

package ros;

message Empty {}

message Time {
    uint32 secs = 1;
    uint32 nsecs = 2;
}

message Duration {
    int32 secs = 1;
    int32 nsecs = 2;
}

'''

def generate_pb_messages(message_tree):
    proto = ''
    for pkgname, pkg in message_tree.items():
        proto += 'message %s {\n' % pkgname

        for msgname, fields in pkg.items():
            proto += '  message %s {\n' % msgname
            for key, (fieldname, ros_type) in enumerate(fields.items()):
                definition = '{} {} = {};'.format(
                    type_ros2pb(ros_type), fieldname, key+1)
                proto += '    {}\n'.format(definition)

            proto += '  }\n'
        proto += '}\n\n'
    return proto

def generate_pb_service(topic, ros_type):
    return service_template.format(service_name=topic2service_name(topic), pb_type=type_ros2pb(ros_type))


def generate_proto_file():
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    proto_dir = os.path.join(scripts_dir, 'generated')
    type_tree, published_topics = snapshot_ros_messages()

    type_tree[None]['time'] = {
        'secs': 'uint32',
        'nsecs': 'uint32',
    }

    type_tree[None]['duration'] = {
        'secs': 'int32',
        'nsecs': 'int32',
    }

    print('Found {} topics'.format(len(published_topics)))


    if not os.path.exists(proto_dir):
        os.makedirs(proto_dir)
    f = open(os.path.join(proto_dir, 'ros.proto'), 'w+')

    f.write(header)
    for (topic, ros_type) in published_topics:
        f.write(generate_pb_service(topic, ros_type))
    f.write(generate_pb_messages(type_tree))
    f.close()
    print('.proto file generated')



    f = open(os.path.join(proto_dir, 'grpc_server.py'), 'w+')
    f.write(generate_server(type_tree, published_topics))
    f.close()
    print('grpc_server.py file generated')

    # print('Generage files in "{}"'.format(proto_dir))
    # grpc_tools.protoc.main(['-I={}'.format(proto_dir), '--python_out={}'.format(
    #     proto_dir), '--grpc_python_out={}'.format(proto_dir), 'ros.proto'])


if __name__ == '__main__':
    try:
        generate_proto_file()

        # talker()
    except rospy.ROSInterruptException:
        pass

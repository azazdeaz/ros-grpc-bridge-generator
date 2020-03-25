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
# TODO ask user to run the generate script if it's not found
from generated.grpc_server import create_server

if __name__ == '__main__':
    rospy.init_node('ros_grpc_server', anonymous=True)
    server = create_server()
    server.add_insecure_port('[::]:50051')
    server.start()
    print('server is running')
    rospy.spin()

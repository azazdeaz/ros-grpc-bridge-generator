
#!/usr/bin/env python3

from concurrent import futures
import time
import math
import logging
import argparse
import sys
import threading
import time

import grpc

import rospy
import roslib.message

import ros_pb2 as ros_pb
import ros_pb2_grpc as ros_grpc



class narrow_stereo_textured_points2Servicer(ros_grpc.narrow_stereo_textured_points2Servicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/PointCloud2')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/narrow_stereo_textured/points2', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.height = pb_msg.height
        ros_msg.width = pb_msg.width
        for pb_msg_ in pb_msg.fields:
            ros_msg_ = roslib.message.get_message_class('sensor_msgs/PointField')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.offset = pb_msg_.offset
            ros_msg_.datatype = pb_msg_.datatype
            ros_msg_.count = pb_msg_.count
            ros_msg.fields.append(ros_msg_)
        ros_msg.is_bigendian = pb_msg.is_bigendian
        ros_msg.point_step = pb_msg.point_step
        ros_msg.row_step = pb_msg.row_step
        ros_msg.data = pb_msg.data
        ros_msg.is_dense = pb_msg.is_dense

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/narrow_stereo_textured/points2', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.PointCloud2()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.height = ros_msg.height
                pb_msg.width = ros_msg.width
                for ros_msg_ in ros_msg.fields:
                    pb_msg_ = ros_pb.sensor_msgs.PointField()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.offset = ros_msg_.offset
                    pb_msg_.datatype = ros_msg_.datatype
                    pb_msg_.count = ros_msg_.count
                    pb_msg.fields.append(pb_msg_)
                pb_msg.is_bigendian = ros_msg.is_bigendian
                pb_msg.point_step = ros_msg.point_step
                pb_msg.row_step = ros_msg.row_step
                pb_msg.data = ros_msg.data
                pb_msg.is_dense = ros_msg.is_dense

                yield pb_msg
            rospy.sleep(0.01)


class outputServicer(ros_grpc.outputServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/PointCloud2')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/output', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.height = pb_msg.height
        ros_msg.width = pb_msg.width
        for pb_msg_ in pb_msg.fields:
            ros_msg_ = roslib.message.get_message_class('sensor_msgs/PointField')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.offset = pb_msg_.offset
            ros_msg_.datatype = pb_msg_.datatype
            ros_msg_.count = pb_msg_.count
            ros_msg.fields.append(ros_msg_)
        ros_msg.is_bigendian = pb_msg.is_bigendian
        ros_msg.point_step = pb_msg.point_step
        ros_msg.row_step = pb_msg.row_step
        ros_msg.data = pb_msg.data
        ros_msg.is_dense = pb_msg.is_dense

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/output', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.PointCloud2()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.height = ros_msg.height
                pb_msg.width = ros_msg.width
                for ros_msg_ in ros_msg.fields:
                    pb_msg_ = ros_pb.sensor_msgs.PointField()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.offset = ros_msg_.offset
                    pb_msg_.datatype = ros_msg_.datatype
                    pb_msg_.count = ros_msg_.count
                    pb_msg.fields.append(pb_msg_)
                pb_msg.is_bigendian = ros_msg.is_bigendian
                pb_msg.point_step = ros_msg.point_step
                pb_msg.row_step = ros_msg.row_step
                pb_msg.data = ros_msg.data
                pb_msg.is_dense = ros_msg.is_dense

                yield pb_msg
            rospy.sleep(0.01)


class rosoutServicer(ros_grpc.rosoutServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('rosgraph_msgs/Log')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/rosout', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.level = pb_msg.level
        ros_msg.name = pb_msg.name
        ros_msg.msg = pb_msg.msg
        ros_msg.file = pb_msg.file
        ros_msg.function = pb_msg.function
        ros_msg.line = pb_msg.line
        for pb_msg_ in pb_msg.topics:
            ros_msg.topics.append(pb_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/rosout', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.rosgraph_msgs.Log()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.level = ros_msg.level
                pb_msg.name = ros_msg.name
                pb_msg.msg = ros_msg.msg
                pb_msg.file = ros_msg.file
                pb_msg.function = ros_msg.function
                pb_msg.line = ros_msg.line
                for ros_msg_ in ros_msg.topics:
                    pb_msg.topics.append(ros_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class rosout_aggServicer(ros_grpc.rosout_aggServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('rosgraph_msgs/Log')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/rosout_agg', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.level = pb_msg.level
        ros_msg.name = pb_msg.name
        ros_msg.msg = pb_msg.msg
        ros_msg.file = pb_msg.file
        ros_msg.function = pb_msg.function
        ros_msg.line = pb_msg.line
        for pb_msg_ in pb_msg.topics:
            ros_msg.topics.append(pb_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/rosout_agg', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.rosgraph_msgs.Log()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.level = ros_msg.level
                pb_msg.name = ros_msg.name
                pb_msg.msg = ros_msg.msg
                pb_msg.file = ros_msg.file
                pb_msg.function = ros_msg.function
                pb_msg.line = ros_msg.line
                for ros_msg_ in ros_msg.topics:
                    pb_msg.topics.append(ros_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class my_pcl_tutorial_get_loggersServicer(ros_grpc.my_pcl_tutorial_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        rospy.wait_for_service('/my_pcl_tutorial/get_loggers')
        call = rospy.ServiceProxy('/my_pcl_tutorial/get_loggers', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.GetLoggersResponse()

        for ros_msg_ in ros_msg.loggers:
            pb_msg_ = ros_pb.roscpp.Logger()
            pb_msg_.name = ros_msg_.name
            pb_msg_.level = ros_msg_.level
            pb_msg.loggers.append(pb_msg_)

        return pb_msg


class my_pcl_tutorial_set_logger_levelServicer(ros_grpc.my_pcl_tutorial_set_logger_levelServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/SetLoggerLevel')
        rospy.wait_for_service('/my_pcl_tutorial/set_logger_level')
        call = rospy.ServiceProxy('/my_pcl_tutorial/set_logger_level', Srv)
        ros_msg = Srv._request_class()
        ros_msg.logger = pb_msg.logger
        ros_msg.level = pb_msg.level

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


class rosout_get_loggersServicer(ros_grpc.rosout_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        rospy.wait_for_service('/rosout/get_loggers')
        call = rospy.ServiceProxy('/rosout/get_loggers', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.GetLoggersResponse()

        for ros_msg_ in ros_msg.loggers:
            pb_msg_ = ros_pb.roscpp.Logger()
            pb_msg_.name = ros_msg_.name
            pb_msg_.level = ros_msg_.level
            pb_msg.loggers.append(pb_msg_)

        return pb_msg


class rosout_set_logger_levelServicer(ros_grpc.rosout_set_logger_levelServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/SetLoggerLevel')
        rospy.wait_for_service('/rosout/set_logger_level')
        call = rospy.ServiceProxy('/rosout/set_logger_level', Srv)
        ros_msg = Srv._request_class()
        ros_msg.logger = pb_msg.logger
        ros_msg.level = pb_msg.level

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


def create_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ros_grpc.add_narrow_stereo_textured_points2Servicer_to_server(narrow_stereo_textured_points2Servicer(), server)
    ros_grpc.add_outputServicer_to_server(outputServicer(), server)
    ros_grpc.add_rosoutServicer_to_server(rosoutServicer(), server)
    ros_grpc.add_rosout_aggServicer_to_server(rosout_aggServicer(), server)
    ros_grpc.add_my_pcl_tutorial_get_loggersServicer_to_server(my_pcl_tutorial_get_loggersServicer(), server)
    ros_grpc.add_my_pcl_tutorial_set_logger_levelServicer_to_server(my_pcl_tutorial_set_logger_levelServicer(), server)
    ros_grpc.add_rosout_get_loggersServicer_to_server(rosout_get_loggersServicer(), server)
    ros_grpc.add_rosout_set_logger_levelServicer_to_server(rosout_set_logger_levelServicer(), server)
    return server


def run_server():
    address = rospy.get_param('address', '[::]:50051')
    rospy.init_node('grpc_server', anonymous=True)
    server = create_server()
    server.add_insecure_port(address)
    server.start()
    print("gRPC server is running at %s" % address )
    rospy.spin()

if __name__ == '__main__':
    run_server()


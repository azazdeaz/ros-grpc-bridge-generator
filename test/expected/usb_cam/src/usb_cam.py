
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



class image_view_outputServicer(ros_grpc.image_view_outputServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/Image')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/image_view/output', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.height = pb_msg.height
        ros_msg.width = pb_msg.width
        ros_msg.encoding = pb_msg.encoding
        ros_msg.is_bigendian = pb_msg.is_bigendian
        ros_msg.step = pb_msg.step
        ros_msg.data = pb_msg.data

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/image_view/output', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.Image()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.height = ros_msg.height
                pb_msg.width = ros_msg.width
                pb_msg.encoding = ros_msg.encoding
                pb_msg.is_bigendian = ros_msg.is_bigendian
                pb_msg.step = ros_msg.step
                pb_msg.data = ros_msg.data

                yield pb_msg
            rospy.sleep(0.01)


class image_view_parameter_descriptionsServicer(ros_grpc.image_view_parameter_descriptionsServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/ConfigDescription')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/image_view/parameter_descriptions', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/Group')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.type = pb_msg_.type
            for pb_msg__ in pb_msg_.parameters:
                ros_msg__ = roslib.message.get_message_class('dynamic_reconfigure/ParamDescription')()
                ros_msg__.name = pb_msg__.name
                ros_msg__.type = pb_msg__.type
                ros_msg__.level = pb_msg__.level
                ros_msg__.description = pb_msg__.description
                ros_msg__.edit_method = pb_msg__.edit_method
                ros_msg_.parameters.append(ros_msg__)
            ros_msg_.parent = pb_msg_.parent
            ros_msg_.id = pb_msg_.id
            ros_msg.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.max.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.max.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.max.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.max.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.max.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.max.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.min.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.min.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.min.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.min.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.min.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.min.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.dflt.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/image_view/parameter_descriptions', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.ConfigDescription()
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.Group()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.type = ros_msg_.type
                    for ros_msg__ in ros_msg_.parameters:
                        pb_msg__ = ros_pb.dynamic_reconfigure.ParamDescription()
                        pb_msg__.name = ros_msg__.name
                        pb_msg__.type = ros_msg__.type
                        pb_msg__.level = ros_msg__.level
                        pb_msg__.description = ros_msg__.description
                        pb_msg__.edit_method = ros_msg__.edit_method
                        pb_msg_.parameters.append(pb_msg__)
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg_.id = ros_msg_.id
                    pb_msg.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.max.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.max.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.max.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.max.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.max.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.max.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.min.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.min.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.min.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.min.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.min.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.min.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.dflt.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class image_view_parameter_updatesServicer(ros_grpc.image_view_parameter_updatesServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/Config')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/image_view/parameter_updates', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/image_view/parameter_updates', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.Config()
                for ros_msg_ in ros_msg.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.groups.append(pb_msg_)

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


class usb_cam_camera_infoServicer(ros_grpc.usb_cam_camera_infoServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/CameraInfo')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/camera_info', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.height = pb_msg.height
        ros_msg.width = pb_msg.width
        ros_msg.distortion_model = pb_msg.distortion_model
        for pb_msg_ in pb_msg.D:
            ros_msg.D.append(pb_msg_)
        for pb_msg_ in pb_msg.K:
            ros_msg.K.append(pb_msg_)
        for pb_msg_ in pb_msg.R:
            ros_msg.R.append(pb_msg_)
        for pb_msg_ in pb_msg.P:
            ros_msg.P.append(pb_msg_)
        ros_msg.binning_x = pb_msg.binning_x
        ros_msg.binning_y = pb_msg.binning_y
        ros_msg.roi.x_offset = pb_msg.roi.x_offset
        ros_msg.roi.y_offset = pb_msg.roi.y_offset
        ros_msg.roi.height = pb_msg.roi.height
        ros_msg.roi.width = pb_msg.roi.width
        ros_msg.roi.do_rectify = pb_msg.roi.do_rectify

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/camera_info', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.CameraInfo()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.height = ros_msg.height
                pb_msg.width = ros_msg.width
                pb_msg.distortion_model = ros_msg.distortion_model
                for ros_msg_ in ros_msg.D:
                    pb_msg.D.append(ros_msg_)
                for ros_msg_ in ros_msg.K:
                    pb_msg.K.append(ros_msg_)
                for ros_msg_ in ros_msg.R:
                    pb_msg.R.append(ros_msg_)
                for ros_msg_ in ros_msg.P:
                    pb_msg.P.append(ros_msg_)
                pb_msg.binning_x = ros_msg.binning_x
                pb_msg.binning_y = ros_msg.binning_y
                pb_msg.roi.x_offset = ros_msg.roi.x_offset
                pb_msg.roi.y_offset = ros_msg.roi.y_offset
                pb_msg.roi.height = ros_msg.roi.height
                pb_msg.roi.width = ros_msg.roi.width
                pb_msg.roi.do_rectify = ros_msg.roi.do_rectify

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_rawServicer(ros_grpc.usb_cam_image_rawServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/Image')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.height = pb_msg.height
        ros_msg.width = pb_msg.width
        ros_msg.encoding = pb_msg.encoding
        ros_msg.is_bigendian = pb_msg.is_bigendian
        ros_msg.step = pb_msg.step
        ros_msg.data = pb_msg.data

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.Image()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.height = ros_msg.height
                pb_msg.width = ros_msg.width
                pb_msg.encoding = ros_msg.encoding
                pb_msg.is_bigendian = ros_msg.is_bigendian
                pb_msg.step = ros_msg.step
                pb_msg.data = ros_msg.data

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_compressedServicer(ros_grpc.usb_cam_image_raw_compressedServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/CompressedImage')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/compressed', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.format = pb_msg.format
        ros_msg.data = pb_msg.data

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/compressed', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.CompressedImage()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.format = ros_msg.format
                pb_msg.data = ros_msg.data

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_compressed_parameter_descriptionsServicer(ros_grpc.usb_cam_image_raw_compressed_parameter_descriptionsServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/ConfigDescription')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/compressed/parameter_descriptions', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/Group')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.type = pb_msg_.type
            for pb_msg__ in pb_msg_.parameters:
                ros_msg__ = roslib.message.get_message_class('dynamic_reconfigure/ParamDescription')()
                ros_msg__.name = pb_msg__.name
                ros_msg__.type = pb_msg__.type
                ros_msg__.level = pb_msg__.level
                ros_msg__.description = pb_msg__.description
                ros_msg__.edit_method = pb_msg__.edit_method
                ros_msg_.parameters.append(ros_msg__)
            ros_msg_.parent = pb_msg_.parent
            ros_msg_.id = pb_msg_.id
            ros_msg.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.max.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.max.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.max.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.max.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.max.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.max.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.min.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.min.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.min.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.min.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.min.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.min.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.dflt.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/compressed/parameter_descriptions', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.ConfigDescription()
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.Group()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.type = ros_msg_.type
                    for ros_msg__ in ros_msg_.parameters:
                        pb_msg__ = ros_pb.dynamic_reconfigure.ParamDescription()
                        pb_msg__.name = ros_msg__.name
                        pb_msg__.type = ros_msg__.type
                        pb_msg__.level = ros_msg__.level
                        pb_msg__.description = ros_msg__.description
                        pb_msg__.edit_method = ros_msg__.edit_method
                        pb_msg_.parameters.append(pb_msg__)
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg_.id = ros_msg_.id
                    pb_msg.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.max.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.max.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.max.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.max.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.max.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.max.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.min.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.min.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.min.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.min.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.min.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.min.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.dflt.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_compressed_parameter_updatesServicer(ros_grpc.usb_cam_image_raw_compressed_parameter_updatesServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/Config')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/compressed/parameter_updates', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/compressed/parameter_updates', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.Config()
                for ros_msg_ in ros_msg.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_compressedDepthServicer(ros_grpc.usb_cam_image_raw_compressedDepthServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('sensor_msgs/CompressedImage')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/compressedDepth', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.format = pb_msg.format
        ros_msg.data = pb_msg.data

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/compressedDepth', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.sensor_msgs.CompressedImage()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.format = ros_msg.format
                pb_msg.data = ros_msg.data

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_compressedDepth_parameter_descriptionsServicer(ros_grpc.usb_cam_image_raw_compressedDepth_parameter_descriptionsServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/ConfigDescription')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/compressedDepth/parameter_descriptions', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/Group')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.type = pb_msg_.type
            for pb_msg__ in pb_msg_.parameters:
                ros_msg__ = roslib.message.get_message_class('dynamic_reconfigure/ParamDescription')()
                ros_msg__.name = pb_msg__.name
                ros_msg__.type = pb_msg__.type
                ros_msg__.level = pb_msg__.level
                ros_msg__.description = pb_msg__.description
                ros_msg__.edit_method = pb_msg__.edit_method
                ros_msg_.parameters.append(ros_msg__)
            ros_msg_.parent = pb_msg_.parent
            ros_msg_.id = pb_msg_.id
            ros_msg.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.max.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.max.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.max.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.max.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.max.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.max.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.min.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.min.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.min.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.min.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.min.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.min.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.dflt.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/compressedDepth/parameter_descriptions', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.ConfigDescription()
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.Group()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.type = ros_msg_.type
                    for ros_msg__ in ros_msg_.parameters:
                        pb_msg__ = ros_pb.dynamic_reconfigure.ParamDescription()
                        pb_msg__.name = ros_msg__.name
                        pb_msg__.type = ros_msg__.type
                        pb_msg__.level = ros_msg__.level
                        pb_msg__.description = ros_msg__.description
                        pb_msg__.edit_method = ros_msg__.edit_method
                        pb_msg_.parameters.append(pb_msg__)
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg_.id = ros_msg_.id
                    pb_msg.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.max.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.max.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.max.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.max.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.max.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.max.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.min.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.min.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.min.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.min.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.min.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.min.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.dflt.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_compressedDepth_parameter_updatesServicer(ros_grpc.usb_cam_image_raw_compressedDepth_parameter_updatesServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/Config')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/compressedDepth/parameter_updates', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/compressedDepth/parameter_updates', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.Config()
                for ros_msg_ in ros_msg.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_theoraServicer(ros_grpc.usb_cam_image_raw_theoraServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('theora_image_transport/Packet')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/theora', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.data = pb_msg.data
        ros_msg.b_o_s = pb_msg.b_o_s
        ros_msg.e_o_s = pb_msg.e_o_s
        ros_msg.granulepos = pb_msg.granulepos
        ros_msg.packetno = pb_msg.packetno

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/theora', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.theora_image_transport.Packet()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.data = ros_msg.data
                pb_msg.b_o_s = ros_msg.b_o_s
                pb_msg.e_o_s = ros_msg.e_o_s
                pb_msg.granulepos = ros_msg.granulepos
                pb_msg.packetno = ros_msg.packetno

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_theora_parameter_descriptionsServicer(ros_grpc.usb_cam_image_raw_theora_parameter_descriptionsServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/ConfigDescription')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/theora/parameter_descriptions', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/Group')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.type = pb_msg_.type
            for pb_msg__ in pb_msg_.parameters:
                ros_msg__ = roslib.message.get_message_class('dynamic_reconfigure/ParamDescription')()
                ros_msg__.name = pb_msg__.name
                ros_msg__.type = pb_msg__.type
                ros_msg__.level = pb_msg__.level
                ros_msg__.description = pb_msg__.description
                ros_msg__.edit_method = pb_msg__.edit_method
                ros_msg_.parameters.append(ros_msg__)
            ros_msg_.parent = pb_msg_.parent
            ros_msg_.id = pb_msg_.id
            ros_msg.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.max.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.max.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.max.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.max.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.max.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.max.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.max.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.min.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.min.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.min.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.min.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.min.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.min.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.min.groups.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.dflt.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.dflt.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.dflt.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/theora/parameter_descriptions', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.ConfigDescription()
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.Group()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.type = ros_msg_.type
                    for ros_msg__ in ros_msg_.parameters:
                        pb_msg__ = ros_pb.dynamic_reconfigure.ParamDescription()
                        pb_msg__.name = ros_msg__.name
                        pb_msg__.type = ros_msg__.type
                        pb_msg__.level = ros_msg__.level
                        pb_msg__.description = ros_msg__.description
                        pb_msg__.edit_method = ros_msg__.edit_method
                        pb_msg_.parameters.append(pb_msg__)
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg_.id = ros_msg_.id
                    pb_msg.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.max.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.max.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.max.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.max.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.max.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.max.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.max.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.min.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.min.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.min.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.min.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.min.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.min.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.min.groups.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.dflt.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.dflt.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.dflt.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class usb_cam_image_raw_theora_parameter_updatesServicer(ros_grpc.usb_cam_image_raw_theora_parameter_updatesServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('dynamic_reconfigure/Config')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/usb_cam/image_raw/theora/parameter_updates', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        for pb_msg_ in pb_msg.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.groups.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/usb_cam/image_raw/theora/parameter_updates', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.dynamic_reconfigure.Config()
                for ros_msg_ in ros_msg.bools:
                    pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.bools.append(pb_msg_)
                for ros_msg_ in ros_msg.ints:
                    pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.ints.append(pb_msg_)
                for ros_msg_ in ros_msg.strs:
                    pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.strs.append(pb_msg_)
                for ros_msg_ in ros_msg.doubles:
                    pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.value = ros_msg_.value
                    pb_msg.doubles.append(pb_msg_)
                for ros_msg_ in ros_msg.groups:
                    pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
                    pb_msg_.name = ros_msg_.name
                    pb_msg_.state = ros_msg_.state
                    pb_msg_.id = ros_msg_.id
                    pb_msg_.parent = ros_msg_.parent
                    pb_msg.groups.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class image_view_get_loggersServicer(ros_grpc.image_view_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        call = rospy.ServiceProxy('/image_view/get_loggers', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.loggers:
            ros_msg_ = roslib.message.get_message_class('roscpp/Logger')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.level = pb_msg_.level
            ros_msg.loggers.append(ros_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.GetLoggersResponse()

        for ros_msg_ in ros_msg.loggers:
            pb_msg_ = ros_pb.roscpp.Logger()
            pb_msg_.name = ros_msg_.name
            pb_msg_.level = ros_msg_.level
            pb_msg.loggers.append(pb_msg_)

        return pb_msg


class image_view_listServicer(ros_grpc.image_view_listServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('nodelet/NodeletList')
        call = rospy.ServiceProxy('/image_view/list', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.nodelets:
            ros_msg.nodelets.append(pb_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.nodelet.NodeletListResponse()

        for ros_msg_ in ros_msg.nodelets:
            pb_msg.nodelets.append(ros_msg_)

        return pb_msg


class image_view_load_nodeletServicer(ros_grpc.image_view_load_nodeletServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('nodelet/NodeletLoad')
        call = rospy.ServiceProxy('/image_view/load_nodelet', Srv)
        ros_msg = Srv._request_class()
        ros_msg.success = pb_msg.success

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.nodelet.NodeletLoadResponse()

        pb_msg.success = ros_msg.success

        return pb_msg


class image_view_set_logger_levelServicer(ros_grpc.image_view_set_logger_levelServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/SetLoggerLevel')
        call = rospy.ServiceProxy('/image_view/set_logger_level', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


class image_view_set_parametersServicer(ros_grpc.image_view_set_parametersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('dynamic_reconfigure/Reconfigure')
        call = rospy.ServiceProxy('/image_view/set_parameters', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.config.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.config.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.config.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.config.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.config.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.config.groups.append(ros_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.dynamic_reconfigure.ReconfigureResponse()

        for ros_msg_ in ros_msg.config.bools:
            pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.bools.append(pb_msg_)
        for ros_msg_ in ros_msg.config.ints:
            pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.ints.append(pb_msg_)
        for ros_msg_ in ros_msg.config.strs:
            pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.strs.append(pb_msg_)
        for ros_msg_ in ros_msg.config.doubles:
            pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.doubles.append(pb_msg_)
        for ros_msg_ in ros_msg.config.groups:
            pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
            pb_msg_.name = ros_msg_.name
            pb_msg_.state = ros_msg_.state
            pb_msg_.id = ros_msg_.id
            pb_msg_.parent = ros_msg_.parent
            pb_msg.config.groups.append(pb_msg_)

        return pb_msg


class image_view_unload_nodeletServicer(ros_grpc.image_view_unload_nodeletServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('nodelet/NodeletUnload')
        call = rospy.ServiceProxy('/image_view/unload_nodelet', Srv)
        ros_msg = Srv._request_class()
        ros_msg.success = pb_msg.success

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.nodelet.NodeletUnloadResponse()

        pb_msg.success = ros_msg.success

        return pb_msg


class rosout_get_loggersServicer(ros_grpc.rosout_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        call = rospy.ServiceProxy('/rosout/get_loggers', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.loggers:
            ros_msg_ = roslib.message.get_message_class('roscpp/Logger')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.level = pb_msg_.level
            ros_msg.loggers.append(ros_msg_)

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
        call = rospy.ServiceProxy('/rosout/set_logger_level', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


class usb_cam_get_loggersServicer(ros_grpc.usb_cam_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        call = rospy.ServiceProxy('/usb_cam/get_loggers', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.loggers:
            ros_msg_ = roslib.message.get_message_class('roscpp/Logger')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.level = pb_msg_.level
            ros_msg.loggers.append(ros_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.GetLoggersResponse()

        for ros_msg_ in ros_msg.loggers:
            pb_msg_ = ros_pb.roscpp.Logger()
            pb_msg_.name = ros_msg_.name
            pb_msg_.level = ros_msg_.level
            pb_msg.loggers.append(pb_msg_)

        return pb_msg


class usb_cam_image_raw_compressed_set_parametersServicer(ros_grpc.usb_cam_image_raw_compressed_set_parametersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('dynamic_reconfigure/Reconfigure')
        call = rospy.ServiceProxy('/usb_cam/image_raw/compressed/set_parameters', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.config.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.config.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.config.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.config.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.config.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.config.groups.append(ros_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.dynamic_reconfigure.ReconfigureResponse()

        for ros_msg_ in ros_msg.config.bools:
            pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.bools.append(pb_msg_)
        for ros_msg_ in ros_msg.config.ints:
            pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.ints.append(pb_msg_)
        for ros_msg_ in ros_msg.config.strs:
            pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.strs.append(pb_msg_)
        for ros_msg_ in ros_msg.config.doubles:
            pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.doubles.append(pb_msg_)
        for ros_msg_ in ros_msg.config.groups:
            pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
            pb_msg_.name = ros_msg_.name
            pb_msg_.state = ros_msg_.state
            pb_msg_.id = ros_msg_.id
            pb_msg_.parent = ros_msg_.parent
            pb_msg.config.groups.append(pb_msg_)

        return pb_msg


class usb_cam_image_raw_compressedDepth_set_parametersServicer(ros_grpc.usb_cam_image_raw_compressedDepth_set_parametersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('dynamic_reconfigure/Reconfigure')
        call = rospy.ServiceProxy('/usb_cam/image_raw/compressedDepth/set_parameters', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.config.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.config.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.config.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.config.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.config.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.config.groups.append(ros_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.dynamic_reconfigure.ReconfigureResponse()

        for ros_msg_ in ros_msg.config.bools:
            pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.bools.append(pb_msg_)
        for ros_msg_ in ros_msg.config.ints:
            pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.ints.append(pb_msg_)
        for ros_msg_ in ros_msg.config.strs:
            pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.strs.append(pb_msg_)
        for ros_msg_ in ros_msg.config.doubles:
            pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.doubles.append(pb_msg_)
        for ros_msg_ in ros_msg.config.groups:
            pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
            pb_msg_.name = ros_msg_.name
            pb_msg_.state = ros_msg_.state
            pb_msg_.id = ros_msg_.id
            pb_msg_.parent = ros_msg_.parent
            pb_msg.config.groups.append(pb_msg_)

        return pb_msg


class usb_cam_image_raw_theora_set_parametersServicer(ros_grpc.usb_cam_image_raw_theora_set_parametersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('dynamic_reconfigure/Reconfigure')
        call = rospy.ServiceProxy('/usb_cam/image_raw/theora/set_parameters', Srv)
        ros_msg = Srv._request_class()
        for pb_msg_ in pb_msg.config.bools:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/BoolParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.bools.append(ros_msg_)
        for pb_msg_ in pb_msg.config.ints:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/IntParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.ints.append(ros_msg_)
        for pb_msg_ in pb_msg.config.strs:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/StrParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.strs.append(ros_msg_)
        for pb_msg_ in pb_msg.config.doubles:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/DoubleParameter')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.value = pb_msg_.value
            ros_msg.config.doubles.append(ros_msg_)
        for pb_msg_ in pb_msg.config.groups:
            ros_msg_ = roslib.message.get_message_class('dynamic_reconfigure/GroupState')()
            ros_msg_.name = pb_msg_.name
            ros_msg_.state = pb_msg_.state
            ros_msg_.id = pb_msg_.id
            ros_msg_.parent = pb_msg_.parent
            ros_msg.config.groups.append(ros_msg_)

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.dynamic_reconfigure.ReconfigureResponse()

        for ros_msg_ in ros_msg.config.bools:
            pb_msg_ = ros_pb.dynamic_reconfigure.BoolParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.bools.append(pb_msg_)
        for ros_msg_ in ros_msg.config.ints:
            pb_msg_ = ros_pb.dynamic_reconfigure.IntParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.ints.append(pb_msg_)
        for ros_msg_ in ros_msg.config.strs:
            pb_msg_ = ros_pb.dynamic_reconfigure.StrParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.strs.append(pb_msg_)
        for ros_msg_ in ros_msg.config.doubles:
            pb_msg_ = ros_pb.dynamic_reconfigure.DoubleParameter()
            pb_msg_.name = ros_msg_.name
            pb_msg_.value = ros_msg_.value
            pb_msg.config.doubles.append(pb_msg_)
        for ros_msg_ in ros_msg.config.groups:
            pb_msg_ = ros_pb.dynamic_reconfigure.GroupState()
            pb_msg_.name = ros_msg_.name
            pb_msg_.state = ros_msg_.state
            pb_msg_.id = ros_msg_.id
            pb_msg_.parent = ros_msg_.parent
            pb_msg.config.groups.append(pb_msg_)

        return pb_msg


class usb_cam_set_camera_infoServicer(ros_grpc.usb_cam_set_camera_infoServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('sensor_msgs/SetCameraInfo')
        call = rospy.ServiceProxy('/usb_cam/set_camera_info', Srv)
        ros_msg = Srv._request_class()
        ros_msg.success = pb_msg.success
        ros_msg.status_message = pb_msg.status_message

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.sensor_msgs.SetCameraInfoResponse()

        pb_msg.success = ros_msg.success
        pb_msg.status_message = ros_msg.status_message

        return pb_msg


class usb_cam_set_logger_levelServicer(ros_grpc.usb_cam_set_logger_levelServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/SetLoggerLevel')
        call = rospy.ServiceProxy('/usb_cam/set_logger_level', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


class usb_cam_start_captureServicer(ros_grpc.usb_cam_start_captureServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('std_srvs/Empty')
        call = rospy.ServiceProxy('/usb_cam/start_capture', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.std_srvs.EmptyResponse()


        return pb_msg


class usb_cam_stop_captureServicer(ros_grpc.usb_cam_stop_captureServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('std_srvs/Empty')
        call = rospy.ServiceProxy('/usb_cam/stop_capture', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.std_srvs.EmptyResponse()


        return pb_msg


def create_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ros_grpc.add_image_view_outputServicer_to_server(image_view_outputServicer(), server)
    ros_grpc.add_image_view_parameter_descriptionsServicer_to_server(image_view_parameter_descriptionsServicer(), server)
    ros_grpc.add_image_view_parameter_updatesServicer_to_server(image_view_parameter_updatesServicer(), server)
    ros_grpc.add_rosoutServicer_to_server(rosoutServicer(), server)
    ros_grpc.add_rosout_aggServicer_to_server(rosout_aggServicer(), server)
    ros_grpc.add_usb_cam_camera_infoServicer_to_server(usb_cam_camera_infoServicer(), server)
    ros_grpc.add_usb_cam_image_rawServicer_to_server(usb_cam_image_rawServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressedServicer_to_server(usb_cam_image_raw_compressedServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressed_parameter_descriptionsServicer_to_server(usb_cam_image_raw_compressed_parameter_descriptionsServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressed_parameter_updatesServicer_to_server(usb_cam_image_raw_compressed_parameter_updatesServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressedDepthServicer_to_server(usb_cam_image_raw_compressedDepthServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressedDepth_parameter_descriptionsServicer_to_server(usb_cam_image_raw_compressedDepth_parameter_descriptionsServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressedDepth_parameter_updatesServicer_to_server(usb_cam_image_raw_compressedDepth_parameter_updatesServicer(), server)
    ros_grpc.add_usb_cam_image_raw_theoraServicer_to_server(usb_cam_image_raw_theoraServicer(), server)
    ros_grpc.add_usb_cam_image_raw_theora_parameter_descriptionsServicer_to_server(usb_cam_image_raw_theora_parameter_descriptionsServicer(), server)
    ros_grpc.add_usb_cam_image_raw_theora_parameter_updatesServicer_to_server(usb_cam_image_raw_theora_parameter_updatesServicer(), server)
    ros_grpc.add_image_view_get_loggersServicer_to_server(image_view_get_loggersServicer(), server)
    ros_grpc.add_image_view_listServicer_to_server(image_view_listServicer(), server)
    ros_grpc.add_image_view_load_nodeletServicer_to_server(image_view_load_nodeletServicer(), server)
    ros_grpc.add_image_view_set_logger_levelServicer_to_server(image_view_set_logger_levelServicer(), server)
    ros_grpc.add_image_view_set_parametersServicer_to_server(image_view_set_parametersServicer(), server)
    ros_grpc.add_image_view_unload_nodeletServicer_to_server(image_view_unload_nodeletServicer(), server)
    ros_grpc.add_rosout_get_loggersServicer_to_server(rosout_get_loggersServicer(), server)
    ros_grpc.add_rosout_set_logger_levelServicer_to_server(rosout_set_logger_levelServicer(), server)
    ros_grpc.add_usb_cam_get_loggersServicer_to_server(usb_cam_get_loggersServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressed_set_parametersServicer_to_server(usb_cam_image_raw_compressed_set_parametersServicer(), server)
    ros_grpc.add_usb_cam_image_raw_compressedDepth_set_parametersServicer_to_server(usb_cam_image_raw_compressedDepth_set_parametersServicer(), server)
    ros_grpc.add_usb_cam_image_raw_theora_set_parametersServicer_to_server(usb_cam_image_raw_theora_set_parametersServicer(), server)
    ros_grpc.add_usb_cam_set_camera_infoServicer_to_server(usb_cam_set_camera_infoServicer(), server)
    ros_grpc.add_usb_cam_set_logger_levelServicer_to_server(usb_cam_set_logger_levelServicer(), server)
    ros_grpc.add_usb_cam_start_captureServicer_to_server(usb_cam_start_captureServicer(), server)
    ros_grpc.add_usb_cam_stop_captureServicer_to_server(usb_cam_stop_captureServicer(), server)
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


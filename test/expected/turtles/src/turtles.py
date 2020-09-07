
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


class shapes_cancelServicer(ros_grpc.shapes_cancelServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('actionlib_msgs/GoalID')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/shapes/cancel', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.stamp.secs = pb_msg.stamp.secs
        ros_msg.stamp.nsecs = pb_msg.stamp.nsecs
        ros_msg.id = pb_msg.id

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/shapes/cancel', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.actionlib_msgs.GoalID()
                pb_msg.stamp.secs = ros_msg.stamp.secs
                pb_msg.stamp.nsecs = ros_msg.stamp.nsecs
                pb_msg.id = ros_msg.id

                yield pb_msg
            rospy.sleep(0.01)


class shapes_feedbackServicer(ros_grpc.shapes_feedbackServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('turtle_actionlib/ShapeActionFeedback')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/shapes/feedback', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.status.goal_id.stamp.secs = pb_msg.status.goal_id.stamp.secs
        ros_msg.status.goal_id.stamp.nsecs = pb_msg.status.goal_id.stamp.nsecs
        ros_msg.status.goal_id.id = pb_msg.status.goal_id.id
        ros_msg.status.status = pb_msg.status.status
        ros_msg.status.text = pb_msg.status.text

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/shapes/feedback', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.turtle_actionlib.ShapeActionFeedback()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.status.goal_id.stamp.secs = ros_msg.status.goal_id.stamp.secs
                pb_msg.status.goal_id.stamp.nsecs = ros_msg.status.goal_id.stamp.nsecs
                pb_msg.status.goal_id.id = ros_msg.status.goal_id.id
                pb_msg.status.status = ros_msg.status.status
                pb_msg.status.text = ros_msg.status.text

                yield pb_msg
            rospy.sleep(0.01)


class shapes_goalServicer(ros_grpc.shapes_goalServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('turtle_actionlib/ShapeActionGoal')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/shapes/goal', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.goal_id.stamp.secs = pb_msg.goal_id.stamp.secs
        ros_msg.goal_id.stamp.nsecs = pb_msg.goal_id.stamp.nsecs
        ros_msg.goal_id.id = pb_msg.goal_id.id
        ros_msg.goal.edges = pb_msg.goal.edges
        ros_msg.goal.radius = pb_msg.goal.radius

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/shapes/goal', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.turtle_actionlib.ShapeActionGoal()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.goal_id.stamp.secs = ros_msg.goal_id.stamp.secs
                pb_msg.goal_id.stamp.nsecs = ros_msg.goal_id.stamp.nsecs
                pb_msg.goal_id.id = ros_msg.goal_id.id
                pb_msg.goal.edges = ros_msg.goal.edges
                pb_msg.goal.radius = ros_msg.goal.radius

                yield pb_msg
            rospy.sleep(0.01)


class shapes_resultServicer(ros_grpc.shapes_resultServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('turtle_actionlib/ShapeActionResult')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/shapes/result', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        ros_msg.status.goal_id.stamp.secs = pb_msg.status.goal_id.stamp.secs
        ros_msg.status.goal_id.stamp.nsecs = pb_msg.status.goal_id.stamp.nsecs
        ros_msg.status.goal_id.id = pb_msg.status.goal_id.id
        ros_msg.status.status = pb_msg.status.status
        ros_msg.status.text = pb_msg.status.text
        ros_msg.result.interior_angle = pb_msg.result.interior_angle
        ros_msg.result.apothem = pb_msg.result.apothem

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/shapes/result', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.turtle_actionlib.ShapeActionResult()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                pb_msg.status.goal_id.stamp.secs = ros_msg.status.goal_id.stamp.secs
                pb_msg.status.goal_id.stamp.nsecs = ros_msg.status.goal_id.stamp.nsecs
                pb_msg.status.goal_id.id = ros_msg.status.goal_id.id
                pb_msg.status.status = ros_msg.status.status
                pb_msg.status.text = ros_msg.status.text
                pb_msg.result.interior_angle = ros_msg.result.interior_angle
                pb_msg.result.apothem = ros_msg.result.apothem

                yield pb_msg
            rospy.sleep(0.01)


class shapes_statusServicer(ros_grpc.shapes_statusServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('actionlib_msgs/GoalStatusArray')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/shapes/status', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.header.seq = pb_msg.header.seq
        ros_msg.header.stamp.secs = pb_msg.header.stamp.secs
        ros_msg.header.stamp.nsecs = pb_msg.header.stamp.nsecs
        ros_msg.header.frame_id = pb_msg.header.frame_id
        for pb_msg_ in pb_msg.status_list:
            ros_msg_ = roslib.message.get_message_class('actionlib_msgs/GoalStatus')()
            ros_msg_.goal_id.stamp.secs = pb_msg_.goal_id.stamp.secs
            ros_msg_.goal_id.stamp.nsecs = pb_msg_.goal_id.stamp.nsecs
            ros_msg_.goal_id.id = pb_msg_.goal_id.id
            ros_msg_.status = pb_msg_.status
            ros_msg_.text = pb_msg_.text
            ros_msg.status_list.append(ros_msg_)

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/shapes/status', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.actionlib_msgs.GoalStatusArray()
                pb_msg.header.seq = ros_msg.header.seq
                pb_msg.header.stamp.secs = ros_msg.header.stamp.secs
                pb_msg.header.stamp.nsecs = ros_msg.header.stamp.nsecs
                pb_msg.header.frame_id = ros_msg.header.frame_id
                for ros_msg_ in ros_msg.status_list:
                    pb_msg_ = ros_pb.actionlib_msgs.GoalStatus()
                    pb_msg_.goal_id.stamp.secs = ros_msg_.goal_id.stamp.secs
                    pb_msg_.goal_id.stamp.nsecs = ros_msg_.goal_id.stamp.nsecs
                    pb_msg_.goal_id.id = ros_msg_.goal_id.id
                    pb_msg_.status = ros_msg_.status
                    pb_msg_.text = ros_msg_.text
                    pb_msg.status_list.append(pb_msg_)

                yield pb_msg
            rospy.sleep(0.01)


class turtle1_cmd_velServicer(ros_grpc.turtle1_cmd_velServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('geometry_msgs/Twist')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/turtle1/cmd_vel', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.linear.x = pb_msg.linear.x
        ros_msg.linear.y = pb_msg.linear.y
        ros_msg.linear.z = pb_msg.linear.z
        ros_msg.angular.x = pb_msg.angular.x
        ros_msg.angular.y = pb_msg.angular.y
        ros_msg.angular.z = pb_msg.angular.z

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/turtle1/cmd_vel', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.geometry_msgs.Twist()
                pb_msg.linear.x = ros_msg.linear.x
                pb_msg.linear.y = ros_msg.linear.y
                pb_msg.linear.z = ros_msg.linear.z
                pb_msg.angular.x = ros_msg.angular.x
                pb_msg.angular.y = ros_msg.angular.y
                pb_msg.angular.z = ros_msg.angular.z

                yield pb_msg
            rospy.sleep(0.01)


class turtle1_color_sensorServicer(ros_grpc.turtle1_color_sensorServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('turtlesim/Color')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/turtle1/color_sensor', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.r = pb_msg.r
        ros_msg.g = pb_msg.g
        ros_msg.b = pb_msg.b

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/turtle1/color_sensor', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.turtlesim.Color()
                pb_msg.r = ros_msg.r
                pb_msg.g = ros_msg.g
                pb_msg.b = ros_msg.b

                yield pb_msg
            rospy.sleep(0.01)


class turtle1_poseServicer(ros_grpc.turtle1_poseServicer):
    def __init__(self):
        self.pub = None
        self.Msg = roslib.message.get_message_class('turtlesim/Pose')

    def Publish(self, pb_msg, context):
        if self.pub == None:
            self.pub = rospy.Publisher('/turtle1/pose', self.Msg, queue_size=10)

        ros_msg = self.Msg()
        ros_msg.x = pb_msg.x
        ros_msg.y = pb_msg.y
        ros_msg.theta = pb_msg.theta
        ros_msg.linear_velocity = pb_msg.linear_velocity
        ros_msg.angular_velocity = pb_msg.angular_velocity

        self.pub.publish(ros_msg)
        return ros_pb.Empty()

    def Subscribe(self, request, context):
        c = {'unsubscribed': False}
        ros_messages = []

        def callback(ros_msg):
            ros_messages.append(ros_msg)
        subscription = rospy.Subscriber('/turtle1/pose', self.Msg, callback)

        def on_rpc_done():
            c['unsubscribed'] = True
            print("Attempting to regain servicer thread...", c)
            subscription.unregister()

        context.add_callback(on_rpc_done)

        while not c['unsubscribed']:
            while ros_messages:
                ros_msg = ros_messages.pop(0)
                pb_msg = ros_pb.turtlesim.Pose()
                pb_msg.x = ros_msg.x
                pb_msg.y = ros_msg.y
                pb_msg.theta = ros_msg.theta
                pb_msg.linear_velocity = ros_msg.linear_velocity
                pb_msg.angular_velocity = ros_msg.angular_velocity

                yield pb_msg
            rospy.sleep(0.01)


class clearServicer(ros_grpc.clearServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('std_srvs/Empty')
        rospy.wait_for_service('/clear')
        call = rospy.ServiceProxy('/clear', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.std_srvs.EmptyResponse()


        return pb_msg


class killServicer(ros_grpc.killServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('turtlesim/Kill')
        rospy.wait_for_service('/kill')
        call = rospy.ServiceProxy('/kill', Srv)
        ros_msg = Srv._request_class()
        ros_msg.name = pb_msg.name

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.turtlesim.KillResponse()


        return pb_msg


class resetServicer(ros_grpc.resetServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('std_srvs/Empty')
        rospy.wait_for_service('/reset')
        call = rospy.ServiceProxy('/reset', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.std_srvs.EmptyResponse()


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


class shapes_get_loggersServicer(ros_grpc.shapes_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        rospy.wait_for_service('/shapes/get_loggers')
        call = rospy.ServiceProxy('/shapes/get_loggers', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.GetLoggersResponse()

        for ros_msg_ in ros_msg.loggers:
            pb_msg_ = ros_pb.roscpp.Logger()
            pb_msg_.name = ros_msg_.name
            pb_msg_.level = ros_msg_.level
            pb_msg.loggers.append(pb_msg_)

        return pb_msg


class shapes_set_logger_levelServicer(ros_grpc.shapes_set_logger_levelServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/SetLoggerLevel')
        rospy.wait_for_service('/shapes/set_logger_level')
        call = rospy.ServiceProxy('/shapes/set_logger_level', Srv)
        ros_msg = Srv._request_class()
        ros_msg.logger = pb_msg.logger
        ros_msg.level = pb_msg.level

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


class sim_get_loggersServicer(ros_grpc.sim_get_loggersServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/GetLoggers')
        rospy.wait_for_service('/sim/get_loggers')
        call = rospy.ServiceProxy('/sim/get_loggers', Srv)
        ros_msg = Srv._request_class()

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.GetLoggersResponse()

        for ros_msg_ in ros_msg.loggers:
            pb_msg_ = ros_pb.roscpp.Logger()
            pb_msg_.name = ros_msg_.name
            pb_msg_.level = ros_msg_.level
            pb_msg.loggers.append(pb_msg_)

        return pb_msg


class sim_set_logger_levelServicer(ros_grpc.sim_set_logger_levelServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('roscpp/SetLoggerLevel')
        rospy.wait_for_service('/sim/set_logger_level')
        call = rospy.ServiceProxy('/sim/set_logger_level', Srv)
        ros_msg = Srv._request_class()
        ros_msg.logger = pb_msg.logger
        ros_msg.level = pb_msg.level

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.roscpp.SetLoggerLevelResponse()


        return pb_msg


class spawnServicer(ros_grpc.spawnServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('turtlesim/Spawn')
        rospy.wait_for_service('/spawn')
        call = rospy.ServiceProxy('/spawn', Srv)
        ros_msg = Srv._request_class()
        ros_msg.x = pb_msg.x
        ros_msg.y = pb_msg.y
        ros_msg.theta = pb_msg.theta
        ros_msg.name = pb_msg.name

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.turtlesim.SpawnResponse()

        pb_msg.name = ros_msg.name

        return pb_msg


class turtle1_set_penServicer(ros_grpc.turtle1_set_penServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('turtlesim/SetPen')
        rospy.wait_for_service('/turtle1/set_pen')
        call = rospy.ServiceProxy('/turtle1/set_pen', Srv)
        ros_msg = Srv._request_class()
        ros_msg.r = pb_msg.r
        ros_msg.g = pb_msg.g
        ros_msg.b = pb_msg.b
        ros_msg.width = pb_msg.width
        ros_msg.off = pb_msg.off

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.turtlesim.SetPenResponse()


        return pb_msg


class turtle1_teleport_absoluteServicer(ros_grpc.turtle1_teleport_absoluteServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('turtlesim/TeleportAbsolute')
        rospy.wait_for_service('/turtle1/teleport_absolute')
        call = rospy.ServiceProxy('/turtle1/teleport_absolute', Srv)
        ros_msg = Srv._request_class()
        ros_msg.x = pb_msg.x
        ros_msg.y = pb_msg.y
        ros_msg.theta = pb_msg.theta

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.turtlesim.TeleportAbsoluteResponse()


        return pb_msg


class turtle1_teleport_relativeServicer(ros_grpc.turtle1_teleport_relativeServicer):
    def Call(self, pb_msg, context):
        Srv = roslib.message.get_service_class('turtlesim/TeleportRelative')
        rospy.wait_for_service('/turtle1/teleport_relative')
        call = rospy.ServiceProxy('/turtle1/teleport_relative', Srv)
        ros_msg = Srv._request_class()
        ros_msg.linear = pb_msg.linear
        ros_msg.angular = pb_msg.angular

        ros_msg = call(ros_msg)
        pb_msg = ros_pb.turtlesim.TeleportRelativeResponse()


        return pb_msg


def create_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ros_grpc.add_rosoutServicer_to_server(rosoutServicer(), server)
    ros_grpc.add_rosout_aggServicer_to_server(rosout_aggServicer(), server)
    ros_grpc.add_shapes_cancelServicer_to_server(shapes_cancelServicer(), server)
    ros_grpc.add_shapes_feedbackServicer_to_server(shapes_feedbackServicer(), server)
    ros_grpc.add_shapes_goalServicer_to_server(shapes_goalServicer(), server)
    ros_grpc.add_shapes_resultServicer_to_server(shapes_resultServicer(), server)
    ros_grpc.add_shapes_statusServicer_to_server(shapes_statusServicer(), server)
    ros_grpc.add_turtle1_cmd_velServicer_to_server(turtle1_cmd_velServicer(), server)
    ros_grpc.add_turtle1_color_sensorServicer_to_server(turtle1_color_sensorServicer(), server)
    ros_grpc.add_turtle1_poseServicer_to_server(turtle1_poseServicer(), server)
    ros_grpc.add_clearServicer_to_server(clearServicer(), server)
    ros_grpc.add_killServicer_to_server(killServicer(), server)
    ros_grpc.add_resetServicer_to_server(resetServicer(), server)
    ros_grpc.add_rosout_get_loggersServicer_to_server(rosout_get_loggersServicer(), server)
    ros_grpc.add_rosout_set_logger_levelServicer_to_server(rosout_set_logger_levelServicer(), server)
    ros_grpc.add_shapes_get_loggersServicer_to_server(shapes_get_loggersServicer(), server)
    ros_grpc.add_shapes_set_logger_levelServicer_to_server(shapes_set_logger_levelServicer(), server)
    ros_grpc.add_sim_get_loggersServicer_to_server(sim_get_loggersServicer(), server)
    ros_grpc.add_sim_set_logger_levelServicer_to_server(sim_set_logger_levelServicer(), server)
    ros_grpc.add_spawnServicer_to_server(spawnServicer(), server)
    ros_grpc.add_turtle1_set_penServicer_to_server(turtle1_set_penServicer(), server)
    ros_grpc.add_turtle1_teleport_absoluteServicer_to_server(turtle1_teleport_absoluteServicer(), server)
    ros_grpc.add_turtle1_teleport_relativeServicer_to_server(turtle1_teleport_relativeServicer(), server)
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


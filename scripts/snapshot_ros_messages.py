#!/usr/bin/env python

import rospy
import rosmsg
import rostopic
import os
import re
from collections import defaultdict
from utils import type_ros2pb, strip_array_notation


def snapshot_ros_messages():
    def parse_ros_message(type_tree, message, msgtype):
        lines = message.splitlines()
        indent_size = 2

        def indent_level(line=''):
            return (len(line)-len(line.lstrip(' '))) / indent_size

        def read_fields():
            indent = indent_level(lines[0])
            prev_line = None
            fields = {}

            while len(lines) > 0:
                current_indent = indent_level(lines[0])
                # end of the definition of this message
                if current_indent == indent:
                    line = prev_line = lines.pop(0)

                    # skip constants
                    if '=' in line:
                        continue

                    # convert the ros field definition and add it to the fields dict
                    ros_type, fieldname = line.lstrip(' ').split(' ')
                    fields[fieldname] = ros_type
                # the previous line has subfields
                elif current_indent > indent:
                    ros_type = prev_line.lstrip(' ').split(' ')[0]
                    package, msgtype = strip_array_notation(
                        ros_type).split('/')
                    type_tree[package][msgtype] = read_fields()
                # we're one indentation level back so this message ended
                else:
                    return fields

            return fields

        package, msgtype = msgtype.split('/')
        type_tree[package][msgtype] = read_fields()

    published_topics = rospy.get_published_topics()
    def deep_dict(): return defaultdict(deep_dict)
    type_tree = deep_dict()

    for (_, ros_type) in published_topics:
        parse_ros_message(
            type_tree, rosmsg.get_msg_text(ros_type), ros_type)
    
    return type_tree, published_topics



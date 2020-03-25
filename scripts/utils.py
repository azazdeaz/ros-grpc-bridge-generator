#!/usr/bin/env python

import re

scalar_ros2pb = {
    'bool': 'bool',
    'int8': 'int32',
    'uint8': 'uint32',
    'int16': 'int32',
    'uint16': 'uint32',
    'int32': 'int32',
    'uint32': 'uint32',
    'int64': 'int64',
    'uint64': 'uint64',
    'float32': 'float',
    'float64': 'double',
    'string': 'string',
    'time': 'Time',
    'duration': 'Duration',
    # deprecated
    'char': 'uint32',
    'byte': 'int32',
}

def strip_array_notation(name):
    return re.sub(r'\[\d*\]$', '', name)

def type_ros2pb(ros_type):
    pb_type = strip_array_notation(ros_type)
    if pb_type in scalar_ros2pb:
        pb_type = scalar_ros2pb[pb_type]

    if ros_type.endswith(']'):
        pb_type = 'repeated ' + pb_type

    return pb_type.replace('/', '.')

def typename_ros2pb(ros_type):
    pb_type = strip_array_notation(ros_type)
    if pb_type in scalar_ros2pb:
        pb_type = scalar_ros2pb[pb_type]

    return pb_type.replace('/', '.')

def topic2service_name(topic):
    return topic.replace('/', '_')[1:]

def parse_ros_type(ros_type):
    is_array = ros_type.endswith(']')
    ros_type = strip_array_notation(ros_type)
    if '/' in ros_type:
        package, typename = ros_type.split('/')
        return package, typename, is_array
    else:
        return None, ros_type, is_array


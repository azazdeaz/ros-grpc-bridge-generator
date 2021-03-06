# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ros_pb2 as ros__pb2


class narrow_stereo_textured_points2Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/ros.narrow_stereo_textured_points2/Publish',
                request_serializer=ros__pb2.sensor_msgs.PointCloud2.SerializeToString,
                response_deserializer=ros__pb2.Empty.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/ros.narrow_stereo_textured_points2/Subscribe',
                request_serializer=ros__pb2.Empty.SerializeToString,
                response_deserializer=ros__pb2.sensor_msgs.PointCloud2.FromString,
                )


class narrow_stereo_textured_points2Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_narrow_stereo_textured_points2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=ros__pb2.sensor_msgs.PointCloud2.FromString,
                    response_serializer=ros__pb2.Empty.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=ros__pb2.Empty.FromString,
                    response_serializer=ros__pb2.sensor_msgs.PointCloud2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.narrow_stereo_textured_points2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class narrow_stereo_textured_points2(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.narrow_stereo_textured_points2/Publish',
            ros__pb2.sensor_msgs.PointCloud2.SerializeToString,
            ros__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ros.narrow_stereo_textured_points2/Subscribe',
            ros__pb2.Empty.SerializeToString,
            ros__pb2.sensor_msgs.PointCloud2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class outputStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/ros.output/Publish',
                request_serializer=ros__pb2.sensor_msgs.PointCloud2.SerializeToString,
                response_deserializer=ros__pb2.Empty.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/ros.output/Subscribe',
                request_serializer=ros__pb2.Empty.SerializeToString,
                response_deserializer=ros__pb2.sensor_msgs.PointCloud2.FromString,
                )


class outputServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_outputServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=ros__pb2.sensor_msgs.PointCloud2.FromString,
                    response_serializer=ros__pb2.Empty.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=ros__pb2.Empty.FromString,
                    response_serializer=ros__pb2.sensor_msgs.PointCloud2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.output', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class output(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.output/Publish',
            ros__pb2.sensor_msgs.PointCloud2.SerializeToString,
            ros__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ros.output/Subscribe',
            ros__pb2.Empty.SerializeToString,
            ros__pb2.sensor_msgs.PointCloud2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class rosoutStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/ros.rosout/Publish',
                request_serializer=ros__pb2.rosgraph_msgs.Log.SerializeToString,
                response_deserializer=ros__pb2.Empty.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/ros.rosout/Subscribe',
                request_serializer=ros__pb2.Empty.SerializeToString,
                response_deserializer=ros__pb2.rosgraph_msgs.Log.FromString,
                )


class rosoutServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_rosoutServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=ros__pb2.rosgraph_msgs.Log.FromString,
                    response_serializer=ros__pb2.Empty.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=ros__pb2.Empty.FromString,
                    response_serializer=ros__pb2.rosgraph_msgs.Log.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.rosout', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class rosout(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.rosout/Publish',
            ros__pb2.rosgraph_msgs.Log.SerializeToString,
            ros__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ros.rosout/Subscribe',
            ros__pb2.Empty.SerializeToString,
            ros__pb2.rosgraph_msgs.Log.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class rosout_aggStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/ros.rosout_agg/Publish',
                request_serializer=ros__pb2.rosgraph_msgs.Log.SerializeToString,
                response_deserializer=ros__pb2.Empty.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/ros.rosout_agg/Subscribe',
                request_serializer=ros__pb2.Empty.SerializeToString,
                response_deserializer=ros__pb2.rosgraph_msgs.Log.FromString,
                )


class rosout_aggServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_rosout_aggServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=ros__pb2.rosgraph_msgs.Log.FromString,
                    response_serializer=ros__pb2.Empty.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=ros__pb2.Empty.FromString,
                    response_serializer=ros__pb2.rosgraph_msgs.Log.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.rosout_agg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class rosout_agg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.rosout_agg/Publish',
            ros__pb2.rosgraph_msgs.Log.SerializeToString,
            ros__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ros.rosout_agg/Subscribe',
            ros__pb2.Empty.SerializeToString,
            ros__pb2.rosgraph_msgs.Log.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class my_pcl_tutorial_get_loggersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/ros.my_pcl_tutorial_get_loggers/Call',
                request_serializer=ros__pb2.roscpp.GetLoggersRequest.SerializeToString,
                response_deserializer=ros__pb2.roscpp.GetLoggersResponse.FromString,
                )


class my_pcl_tutorial_get_loggersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_my_pcl_tutorial_get_loggersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=ros__pb2.roscpp.GetLoggersRequest.FromString,
                    response_serializer=ros__pb2.roscpp.GetLoggersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.my_pcl_tutorial_get_loggers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class my_pcl_tutorial_get_loggers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.my_pcl_tutorial_get_loggers/Call',
            ros__pb2.roscpp.GetLoggersRequest.SerializeToString,
            ros__pb2.roscpp.GetLoggersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class my_pcl_tutorial_set_logger_levelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/ros.my_pcl_tutorial_set_logger_level/Call',
                request_serializer=ros__pb2.roscpp.SetLoggerLevelRequest.SerializeToString,
                response_deserializer=ros__pb2.roscpp.SetLoggerLevelResponse.FromString,
                )


class my_pcl_tutorial_set_logger_levelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_my_pcl_tutorial_set_logger_levelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=ros__pb2.roscpp.SetLoggerLevelRequest.FromString,
                    response_serializer=ros__pb2.roscpp.SetLoggerLevelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.my_pcl_tutorial_set_logger_level', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class my_pcl_tutorial_set_logger_level(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.my_pcl_tutorial_set_logger_level/Call',
            ros__pb2.roscpp.SetLoggerLevelRequest.SerializeToString,
            ros__pb2.roscpp.SetLoggerLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class rosout_get_loggersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/ros.rosout_get_loggers/Call',
                request_serializer=ros__pb2.roscpp.GetLoggersRequest.SerializeToString,
                response_deserializer=ros__pb2.roscpp.GetLoggersResponse.FromString,
                )


class rosout_get_loggersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_rosout_get_loggersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=ros__pb2.roscpp.GetLoggersRequest.FromString,
                    response_serializer=ros__pb2.roscpp.GetLoggersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.rosout_get_loggers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class rosout_get_loggers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.rosout_get_loggers/Call',
            ros__pb2.roscpp.GetLoggersRequest.SerializeToString,
            ros__pb2.roscpp.GetLoggersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class rosout_set_logger_levelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/ros.rosout_set_logger_level/Call',
                request_serializer=ros__pb2.roscpp.SetLoggerLevelRequest.SerializeToString,
                response_deserializer=ros__pb2.roscpp.SetLoggerLevelResponse.FromString,
                )


class rosout_set_logger_levelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_rosout_set_logger_levelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=ros__pb2.roscpp.SetLoggerLevelRequest.FromString,
                    response_serializer=ros__pb2.roscpp.SetLoggerLevelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ros.rosout_set_logger_level', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class rosout_set_logger_level(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ros.rosout_set_logger_level/Call',
            ros__pb2.roscpp.SetLoggerLevelRequest.SerializeToString,
            ros__pb2.roscpp.SetLoggerLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

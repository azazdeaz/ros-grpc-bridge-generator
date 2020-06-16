#!/usr/bin/env python

try:
    import generated.grpc_server
except ImportError as e:
    print("Can't import generated/grcp_server. Did you run the generate script? (ie. '$ rosrun ros_grpc_wrapper generate')")
    raise e

generated.grpc_server.parse_args_and_run_server()

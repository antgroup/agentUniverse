# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/5/11 14:58
# @Author  : fanen.lhy
# @Email   : fanen.lhy@antgroup.com
# @FileName: test_grpc_server.py.py
import grpc
from agentuniverse.agent_serve.web.rpc.grpc import agentuniverse_service_pb2, \
    agentuniverse_service_pb2_grpc


# Start you server_application first.
def test_run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = agentuniverse_service_pb2_grpc.AgentUniverseServiceStub(channel)
        response = stub.service_run(agentuniverse_service_pb2.AgentServiceRequest(
            service_id='demo_service',
            params='{"input":"(18+3-5)/2*4=?"}',
            saved=True
        ))
        print("client received: " + response.request_id)

        response = stub.service_run_result(agentuniverse_service_pb2.AgentResultRequest(
            request_id=response.request_id
        ))
        print("client received: " + response.result)

if __name__ == '__main__':
    test_run()
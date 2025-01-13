## gRPC
除了HTTP API之外，我们也内置提供了GRPC的Agent服务调用接口。

### 启动gRPC服务
如您需要开启GRPC服务的话，可在`config.toml`文件中进行如下配置：
```toml
[GRPC]
activate = 'true'
max_workers = 10
server_port = 50051
```
- **activate**: 仅在该值为`true`的时候启动gRPC服务器
- **max_workers**: gRPC服务器线程池的最大线程数量，默认为10
- **server_port**: gRPC服务器的服务端口，默认为50051

然后启动grpc服务器：
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server()
```


### 调用gRPC服务

### 接口定义
gRPC服务接口的完整定义文件如下：
```text
syntax = "proto3";

package agentuniverse;

service AgentUniverseService {
  rpc service_run(AgentServiceRequest) returns (AgentServiceResponse);
  rpc service_run_async(AgentServiceRequest) returns (AgentServiceResponse);
  rpc service_run_result(AgentResultRequest) returns (AgentServiceResponse);
}

message AgentServiceRequest {
  string service_id = 1;
  string params = 2;
  bool saved = 3;
}

message AgentServiceResponse {
  string message = 1;
  bool success = 2;
  string request_id = 3;
  string result = 4;
}

message AgentResultRequest {
    string request_id = 1;
}
```
\
与[Web API](服务Api.md)类似，gRPC服务包含三个接口：
```text
service AgentUniverseService {
  rpc service_run(AgentServiceRequest) returns (AgentServiceResponse);
  rpc service_run_async(AgentServiceRequest) returns (AgentServiceResponse);
  rpc service_run_result(AgentResultRequest) returns (AgentServiceResponse);
}
```
- **service_run**: 同步调用Agent服务，调用过程中阻塞直到Agent返回结果。
- **service_run_async**: 异步调用Agent服务，调用后先返回一个`request_id`,后续可用该ID通过`service_run_result`接口查询Agent服务结果。
- **service_run_result**: 查询Agent服务的结果。

\
调用Agent服务的请求体结构如下：
```text
message AgentServiceRequest {
  string service_id = 1;
  string params = 2;
  bool saved = 3;
}
```
- **service_id**: 应用中注册的模型服务id。
- **params**: JSON String格式的服务入参，会被`json.loads`拆解为`**kwargs`的形式传递给底层的Agent。
- **saved**: 是否需要保存本次请求结果，该值为`false`的话则本次请求无法在`service_run_result`中查询到。

\
查询Agent服务结果的请求体结构如下：
```text
message AgentResultRequest {
    string request_id = 1;
}
```
- **request_id**: 需要查询的请求ID。

\
返回结果的结构如下：
```text
message AgentServiceResponse {
  string message = 1;
  bool success = 2;
  string request_id = 3;
  string result = 4;
}
```
- **message**: 请求失败时的详细错误信息。
- **success**: 表示本次请求执行是否成功。
- **request_id**: 本次请求的Id。
- **result**: Agent服务执行的结果，异步接口`service_run_async`中为空。

### 调用示例
```python
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
```




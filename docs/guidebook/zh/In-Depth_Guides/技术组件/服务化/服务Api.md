# Web API

AgentUniverse的Web Server提供了数个调用Agent服务的API接口，允许开发者按自己的需求从外部调用Agent服务。

为了方便说明，我们假设Web Server启动在本地的8888端口上，并注册了一个名为`demo_service`的Agent服务：
```yaml
name: 'demo_service'
description: 'A demo service used for explaining.'
agent: 'demo_agent'
metadata:
  type: 'SERVICE'
```
其中的`demo_agent`接受一个str类型的input参数,  
并返回一个字符串:`"Your input is {input}."`

## /service_run
该POST接口以同步的方式调用Agent服务，调用会阻塞直到目标Agent服务返回结果。  
调用示例如下:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"service_id":"demo_service","params":{"input":"Hello!"}}' http://127.0.0.1:8888/service_run
```
预期收到的返回值示例如下：
```shell
{
        "success": true,
        "result": "Your input is Hello!.",
        "message": null,
        "request_id": "7dd7d737b6b64c3c92addf541e73e97c"
}
```
- **`success`**:表示Agent调用的成功与否，取值为`true`和`false`。
- **`message`**:当`success`值为`false`时，该值表示错误信息，成功时为`null`。
- **`result`**:Agent调用成功时，表示执行的结果。
- **`request_id`**:一串随机的字符串，用于一个唯一的请求。可以用于[/service_run_result]()接口，查询对应请求的结果。

## /service_run_stream

该POST接口类似`/service_run`，调用方式与其一致:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"service_id":"demo_service","params":{"input":"Hello!"}}' http://127.0.0.1:8888/service_run_stream
```
但是Agent的返回结果会以流式的形式返回:
```text
# agentuniverse.agent_serve_web.flask_server.service_run_stream

response = Response(task.stream_run(), mimetype="text/event-stream")
response.headers['X-Request-ID'] = task.request_id
```
`request_id`会被包含在响应头`X-Request-ID`中。

## /service_run_async
该POST接口以异步的形式调用Agent服务。调用方式如下:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"service_id":"demo_service","params":{"input":"Hello!"}}' http://127.0.0.1:8888/service_run_async
```
该接口调用后会立刻返回:
```shell
{
        "success": true,
        "result": null,
        "message": null,
        "request_id": "7dd7d737b6b64c3c92addf541e73e97c"
}
```
返回结果中仅会包含表示调用成功与否的`success`与表示本次调用的`request_id`。
对于调用的结果，您需要使用`request_id`在[/service_run_result]()接口中进行查询。

## /service_run_result
该GET接口允许用户用request_id的状态，调用样例如下：
```shell
 curl 'http://127.0.0.1:8888/service_run_result?request_id=8e6f17dbe7ff4730a62b4a2914d73c74'
```
预期收到的返回值示例如下：
```shell
{
  "message":null,
  "request_id":"8e6f17dbe7ff4730a62b4a2914d73c74",
  "result":{
    "result":"Your input is Hello!.",
    "state":"finish",
    "steps":[]
    },
  "success":true}

```
其中`result`包含三个部分：`result`表示Agent服务的执行结果，`state`表示Agent服务的执行状态，`steps`表示Agent服务执行的中间过程。

`state`表示的任务状态包含以下几种情况：
```text
# agentuniverse.agent_serve.web.request_task.TaskStateEnum

class TaskStateEnum(Enum):
    """All possible state of a web request task."""
    INIT = "init"
    RUNNING = "running"
    FINISHED = "finished"
    FAIL = "fail"
    CANCELED = "canceled"
```

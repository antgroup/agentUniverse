# Web API

The Web Server of AgentUniverse provides several API interfaces for calling Agent services, allowing developers to call Agent services through web api.

For convenience, let's assume that the Web Server is started on port 8888 locally and has registered an Agent service named `demo_service`：
```yaml
name: 'demo_service'
description: 'A demo service used for explaining.'
agent: 'demo_agent'
metadata:
  type: 'SERVICE'
```
The `demo_agent` accepts a string type input parameter and returns a string in the format:: `"Your input is {input}."`

## /service_run
This POST interface invokes the Agent service in a synchronous manner, meaning that the call will block until the targeted Agent service responds with a result.
An example response structure is as follows:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"service_id":"demo_service","params":{"input":"Hello!"}}' http://127.0.0.1:8888/service_run
```
The expected return value example is as follows:
```shell
{
        "success": true,
        "result": "Your input is Hello!.",
        "message": null,
        "request_id": "7dd7d737b6b64c3c92addf541e73e97c"
}
```
- **`success`**:  Indicates whether the Agent invocation was successful. It takes the values `true` or `false`.
- **`message`**: When `success` is `false`, this field contains the error message. It is `null` when the operation is successful.
- **`result`**: Represents the outcome of the execution when the Agent invocation is successful.
- **`request_id`**: A randomly generated string serving as a unique identifier for the request. It can be utilized in the [/service_run_result](#service_run_result) interface to retrieve the result of the corresponding request.

## /service_run_stream

This POST interface is similar to `/service_run`, and its call method is consistent with it:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"service_id":"demo_service","params":{"input":"Hello!"}}' http://127.0.0.1:8888/service_run_stream
```
However, there is one key difference: the return result of the Agent will be streamed back to the client. 
```text
# agentuniverse.agent_serve_web.flask_server.service_run_stream

response = Response(task.stream_run(), mimetype="text/event-stream")
response.headers['X-Request-ID'] = task.request_id
```
Additionally, the `request_id` will be included in the response header as X-Request-ID.

## /service_run_async
This POST interface calls the Agent service in an asynchronous manner. The calling method is as follows:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"service_id":"demo_service","params":{"input":"Hello!"}}' http://127.0.0.1:8888/service_run_async
```
The interface will return immediately:
```shell
{
        "success": true,
        "result": null,
        "message": null,
        "request_id": "7dd7d737b6b64c3c92addf541e73e97c"
}
```
The response will only include an indication of success (whether the call was successful or not) and a request_id that uniquely identifies this specific call.
To retrieve the result of the call, you need to use the request_id to query the [/service_run_result](#service_run_result) interface.

## /service_run_result
This GET interface enables users to check the status of a request using the request_id. An example of how to make such a call is as follows:
```shell
 curl 'http://127.0.0.1:8888/service_run_result?request_id=8e6f17dbe7ff4730a62b4a2914d73c74'
```
The expected return value example is as follows:
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
The `result` comprises three parts: `result` indicates the outcome of the Agent service execution, `state` represents the status of the Agent service execution, and `steps` details the intermediate processes involved in the Agent service execution.  
The `state` field indicates the task status and encompasses the following scenarios:
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

# Web Server

AgentUniverse提供了一个基于Flask的Web Server，您可以通过Web Server中预置的API调用开发完成的Agent服务。

## Web Server启动
您需要在AgentUniverse应用启动后，启动Web Server。  
以下是一种启动的示例写法：
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server()
```
Flask服务的默认启动端口为8888，您可以通过bind参数修改启动端口:
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server(bind="127.0.0.1:8002")
```

如果您需要配置更多细节或是追求生产的稳定性，您可以使用Gunicorn作为HTTP Server。

## Gunicorn配置
您可以通过在配置文件中进行如下配置将Gunicorn设置为您的HTTP Server:
```toml
[GUNICORN]
activate = 'true'
```

Gunicorn的配置按照优先度从低到高包含四个层次:`gunicorn`原生默认配置，AgentUniverse默认配置，配置文件配置和启动时配置。其中`gunicorn`的原生默认配置请参考对应版本的`gunicorn`官方文档。

### AgentUniverse默认配置
```python
DEFAULT_GUNICORN_CONFIG = {
    'bind': '127.0.0.1:8888',
    'workers': 5,
    'backlog': 2048,
    'worker_class': 'gthread',
    'threads': 4,
    'timeout': 60,
    'keepalive': 10
}
```
AgentUniverse根据框架的工作特性预先进行了部分参数的配置，您可以通过下面的配置文件或者是启动Web Server时的参数进行修改。

### 配置文件路径
Web Server的配置路径会在AgentUniverse的主配置config.toml中指定。
```toml
[GUNICORN]
# Gunicorn config file path, an absolute path or a relative path based on the dir where the current config file is located.
gunicorn_config_path = './gunicorn_config.toml'
```
如果该参数为相对路径形式，对应的父目录为主配置config.toml所在目录。

### 配置文件
```toml
[GUNICORN_CONFIG]
bind = '127.0.0.1:8888'
backlog = 2048
worker_class = 'gthread'
threads = 4
workers = 5
timeout = 60
keepalive = 10
```
配置文件以toml格式书写，具体的配置项不局限于上述实例中的内容，您可以参考`gunicorn`的官方文档进行更详细的配置。

### 启动配置
您也可以通过以下方式在启动Web Server时进行配置：
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server(bind="127.0.0.1:8002", threads=4)
```
如果您有某些函数想在启动后执行，可以用类似以下方式添加:
```python
from agentuniverse.agent_serve.web.post_fork_queue import add_post_fork
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

def print_hello(name: str):
    print(f"hello {name}")

add_post_fork(print_hello, "name")
AgentUniverse().start()
start_web_server(bind="127.0.0.1:8002")
```
您可以在启动后看到和worker数相等的"hello name"。
# Web Server

agentUniverse provides a web server based on Flask, allowing users to invoke the developed agent services through the predefined APIs on the server.

## Web Server Launch
You need to start the web server after launching the AgentUniverse application. 
Here is an example demonstrating how to launch it:
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server()
```
The default port for the Flask server is 8888. You can change it by editing the `bind` parameter.
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server(bind="127.0.0.1:8002")
```

If you require more detailed configuration or aim for production stability, you can utilize Gunicorn as the HTTP server.

## Gunicorn Configuration
You can set Gunicorn as your HTTP server by configuring it in the configuration file, as detailed below:
```toml
[GUNICORN]
activate = 'true'
```

The configuration of the Gunicorn server comprises four levels of priority, in ascending order: the native default configuration of Gunicorn, the default configuration provided by AgentUniverse, settings specified in the configuration file, and startup configuration. For information on Gunicorn's native default configuration, please refer to the official documentation for the relevant version of Gunicorn.

### AgentUniverse Default Configuration
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
agentUniverse has pre-configured certain parameters based on the framework's operational characteristics. These parameters can be modified either through the configuration file provided below or by specifying parameters when launching the web server.

### Configuration File Path
The configuration path for the web server is designated in AgentUniverse's main configuration file,  `config.toml`.
```toml
[GUNICORN]
# Gunicorn config file path, an absolute path or a relative path based on the dir where the current config file is located.
gunicorn_config_path = './gunicorn_config.toml'
```
If the path is specified in a relative format, the corresponding parent directory is the one where the main configuration file, config.toml, is located.

### Configuration File
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
The configuration file is formatted in TOML, and the specific configuration items included are not exhaustive, as they are merely illustrative examples. For more comprehensive and detailed configurations, you can refer to the official Gunicorn documentation.

### Startup Configuration
You can also configure the web server at startup as follows:
```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse

AgentUniverse().start()
start_web_server(bind="127.0.0.1:8002", threads=4)
```
If you have certain functions you that you wish to execute after Gunicorn fork child processes, you can add them in a manner similar to the following:
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
You should observe an equal unmber of "hello name" output as there are Gunicorn workers processes.
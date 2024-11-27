# Application Engineering Structure and Explanation
As you can see, `agentUniverse` is designed with lightness and integrative capabilities in mind, allowing you to incorporate `agentUniverse` into any of your projects for seamless operation.

## Recommended Project Directory Structure and Explanation
The directory structure provided below is only a suggestion, and you are free to adjust it according to your preferences and actual situation. We will explain this in more detail later in the document.

```
/
├── app/
│   ├── biz/
│   ├── bootstarp/
│   │   └── server_application.py
│   ├── core/
│   │   ├── agent
│   │   ├── knowledge
│   │   ├── llm
│   │   ├── memory
│   │   ├── planner
│   │   ├── service
│   │   └── tool
│   ├── test/
│   └── web/
├── config
├── pyproject.toml
└── other project files...
```

The specific meanings of each package directory level are as follows:
* app - The main application program code
  * biz - Your business code, where you can organize the next level of the directory structure as you wish
  * bootstrap - The entry layer for starting the web server, for starting details refer to server_application.py
  * core - The core layer of LLM agent application components
    * agent - Place the agents you build
    * knowledge - The knowledge you customize and use
    * llm - The LLM (Language Model) you customize and use
    * memory - The memory you customize and use
    * planner - The collaborative mode you customize and use
    * service - Service registration directory
    * tool - The tools you customize and use
  * test - Directory for tests
  * web - The upper web layer, currently left blank
* config - Application configuration code

## Using Any Project Directory Structure
You can adjust the project directory structure according to your preferences and actual circumstances, but please be sure to follow the rules below.

### Bootstrap Startup Directory
Regardless of the location of your project's startup script, except for testing, please ensure that the application service is started with the following statement:

```python
from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse


class ServerApplication:
    """
    Server application.
    """

    @classmethod
    def start(cls):
        AgentUniverse().start()
        start_web_server()

ServerApplication.start()

```
`ServerApplication.start()` is the server startup method for this framework, which accepts a configuration path `config_path` as an input parameter. The default `config_path` is a file located at `project_root_dir/config/config.toml` under the config directory in the project root path. Please ensure that the config file path is correct. If you've further changed the directory of the config file, please adjust the `config_path` accordingly.

### Config Directory
As mentioned in the [Bootstrap Startup Directory](#bootstrap-startup-directory), the default config path for the project is `project_root_dir/config/config.toml`. If you have made any adjustments to this, please ensure that the correct config file path is passed to the startup method when the application server is launched.

### Core Directory
As demonstrated by the recommended directory structure for the project, the project directory within the core directory is mainly used for placing custom domain components such as agents, knowledge, LLM, and others. You are free to position all core components wherever you like and not limited to the same main package. You only need to define it in the `[CORE_PACKAGE]` section of the main configuration file `config/config.toml` of the project, as follows:

```toml
[CORE_PACKAGE]
# Perform a full component scan and registration for all the paths under this list.
default = ['sample_standard_app.intelligence.agentic']
# Scan and register agent components for all paths under this list, with priority over the default.
agent = ['sample_standard_app.intelligence.agentic.agent']
# Scan and register knowledge components for all paths under this list, with priority over the default.
knowledge = ['sample_standard_app.intelligence.agentic.knowledge']
# Scan and register llm components for all paths under this list, with priority over the default.
llm = ['sample_standard_app.intelligence.agentic.llm']
# Scan and register tool components for all paths under this list, with priority over the default.
tool = ['sample_standard_app.intelligence.agentic.tool']
# Scan and register memory components for all paths under this list, with priority over the default.
memory = ['sample_standard_app.intelligence.agentic.memory']
# Scan and register service components for all paths under this list, with priority over the default.
service = ['sample_standard_app.intelligence.service.agent_service']
# Scan and register prompt components for all paths under this list, with priority over the default.
prompt = ['sample_standard_app.intelligence.agentic.prompt']
# Scan and register store components for all paths under this list, with priority over the default.
store = ['sample_standard_app.intelligence.agentic.knowledge.store']
# Scan and register rag_router components for all paths under this list, with priority over the default.
rag_router = ['sample_standard_app.intelligence.agentic.knowledge.rag_router']
# Scan and register doc_processor components for all paths under this list, with priority over the default.
doc_processor = ['sample_standard_app.intelligence.agentic.knowledge.doc_processor']
# Scan and register query_paraphraser components for all paths under this list, with priority over the default.
query_paraphraser = ['sample_standard_app.intelligence.agentic.knowledge.query_paraphraser']
# Scan and register memory_compressor components for all paths under this list, with priority over the default.
memory_compressor = ['sample_standard_app.intelligence.agentic.memory.memory_compressor']
# Scan and register memory_storage components for all paths under this list, with priority over the default.
memory_storage = ['sample_standard_app.intelligence.agentic.memory.memory_storage']
# Scan and register product components for all paths under this list, with priority over the default.
product = ['sample_standard_app.platform.difizen.product']
# Scan and register workflow components for all paths under this list, with priority over the default.
workflow = ['sample_standard_app.platform.difizen.workflow']
```
The format for defining packages follows the standard Python package path format. The framework will register, scan, and manage all types of component packages uniformly based on the defined package paths during startup.

**Tips**: The package path starts one level below your project's root directory. For example, in the sample_standard_app example, since the package path is under the agentUniverse level, it starts with sample_standard_app. If you are using sample_standard_app as a project template, then the path should start with app.xxx.
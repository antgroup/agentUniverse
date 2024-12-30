# Start Tutorial
we will show you how to:

* Prepare the environment and application engineering
* Build a simple agent
* Use pattern components to achieve multi-agent collaboration
* Test and tune the performance of the agent
* Quickly service-orient the agent.

## Environment & Application Preparation
### python version requirement
- python 3.10+

### Application Preparation
We provide a standard project template which you can access [here](../../../../examples/sample_standard_app) . 

The "sample_standard_app" folder contains a standard project template that you can modify according to your own needs. You can also copy the "sample_standard_app" folder to use as the root directory of your application project.

### Installation
**Install via pip**
```shell
pip install agentUniverse
```
More version information can be found on the
[PyPi agentUniverse](https://pypi.org/project/agentUniverse/)

or use package management tools like `poetry` for installation and management.

**Install via poetry**
```shell
# Enter the root directory of your project
poetry add agentUniverse
poetry update
```

### Configuration
#### Main Configuration
Create a `config.toml` file in the root directory of your project. The content is as follows:
```toml
# config.toml
[BASE_INFO]
# The app name will be applied to all processes including agent service integration.
appname = 'demo_app'

[CORE_PACKAGE]
# Perform a full component scan and registration for all the paths under this list.
default = ['sample_standard_app.intelligence.agentic']
# Further information is omitted here.

[SUB_CONFIG_PATH]
# Custom key file path, use to save your own secret key like open ai or sth else. REMEMBER TO ADD IT TO .gitignore.
custom_key_path = './custom_key.toml'
# Further information is omitted here.
```
In this, the `[BASE_INFO]` part is the basic information configuration, the `[CORE_PACKAGE]` part is the component scanning and registration configuration, and the `[SUB_CONFIG_PATH]` part is the sub-configuration file path configuration. For more detailed information, please refer to the subsequent configuration file section.


#### Custom Configuration
During use, you may need some private configurations, such as keys. We recommend that you save these private configurations in a separate file, such as `custom_key.toml`. You can configure the path of this file in `config.toml`'s `custom_key_path`. The private configuration file in the `custom_key_path` path will be automatically registered in the system's environment variables. You can read these private configurations in subsequent code through the `Config` operator or through system variables.

Here is an example of a `custom_key.toml`:
```toml
# Example file of custom_key.toml. Rename to custom_key.toml while using.
[KEY_LIST]
# Perform a full component scan and registration for all the paths under this list.
example_key = 'AnExampleKey'
SERPER_API_KEY='YourSerKey'
OPENAI_API_KEY='YourOpenAIKey'
```

## Build a Simple Agent
### Create an Agent Configuration
Create a `xx_agent_case_a.yaml` file in the `agent` directory of your project. The content is as follows:
```yaml
info:
  name: 'demo_rag_agent'
  description: 'demo rag agent'
profile:
  introduction: You are an AI assistant proficient in information analysis.
  target: Your goal is to determine whether the answers to questions provide valuable information and to make suggestions and evaluations about the answers.
  instruction: |
    The rules you must adhere to are:

    1.You must answer questions posed by users in English, integrating background information with the knowledge you possess.
    2.Generate structured responses, using blank lines as necessary to enhance readability.
    3.Do not adopt incorrect information from the background context.
    4.Consider the relevance of the answer to the question; do not provide answers that do not help with the question.
    5.Provide thorough answers with emphasis on key points, avoiding excessive embellishments.
    6.Avoid vague speculations.
    7.Use numerical information as much as possible.
    
    Background information is:
    {background}
    
    Begin!
    
    The question that needs to be answered is: {input}
  llm_model:
    name: 'demo_llm'
    model_name: 'gpt-4-turbo'
plan:
  planner:
    name: 'rag_planner'
action:
  tool:
    - 'google_search_tool'
metadata:
  type: 'AGENT'
  module: 'sample_standard_app.intelligence.agentic.agent.agent_instance.rag_agent_case.demo_rag_agent'
  class: 'DemoRagAgent'
```
In `xx_agent_case_a.yaml`, we define the configuration of a `DemoRagAgent`. The `info` part is the basic information setting of the agent, the `profile` part contains the setting of the agent using the llm model, the `plan` part contains the behavior planning setting of the agent (determining the working mode of the agent), the `action` part contains the setting of the tools and knowledge that the agent can use, and the `metadata` part contains the metadata setting of the agent object.

### Create an Agent Class
Create a `xx_agent_case_a.py` file with the same name in the `agent` directory of your project. The content is as follows:
```python
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject

class DemoRagAgent(Agent):
    def input_keys(self) -> list[str]:
        return ['input']

    def output_keys(self) -> list[str]:
        return ['output']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        agent_input['input'] = input_object.get_data('input')
        return agent_input

    def parse_result(self, planner_result: dict) -> dict:
        return planner_result
```
In `xx_agent_case_a.py`, we define a `DemoRagAgent` class, which inherits from the `Agent` class. In the `DemoRagAgent` class, we implement the `input_keys`, `output_keys`, `parse_input`, and `parse_result` methods. These methods are used to define the input and output keys, parse the input, and parse the output.

### More Details
For more details on agent development, please refer to the subsequent agent development chapters.

## Use pattern components to complete multi-agent collaboration
Planner determines the role of the agent in the collaboration mode. In `xx_agent_case_a.yaml`, we define a `rag_planner` configuration, which determines that `XXagent` will work in the RAG mode; in complex work scenarios, we often need multiple agents to work together. We can achieve this by configuring multiple agents. 

For example, we can configure a `demo_rag_agent` and a `demo_peer_agent` to work together in the PEER mode.

### Create an Agent Configuration in Collaboration Mode
Create a `xx_agent_case_b.yaml` file in the `agent` directory of your project. The content is as follows:
```yaml
info:
  name: 'demo_peer_agent'
  description: 'demo peer agent'
plan:
  planner:
    name: 'peer_planner'
    eval_threshold: 60
    retry_count: 2
    planning: 'demo_planning_agent'
    executing: 'demo_executing_agent'
    expressing: 'demo_expressing_agent'
    reviewing: 'demo_reviewing_agent'
metadata:
  type: 'AGENT'
  module: 'sample_standard_app.intelligence.agentic.agent.agent_instance.peer_agent_case.demo_peer_agent'
  class: 'DemoPeerAgent'
```
In `xx_agent_case_b.yaml`, we define the configuration of a `DemoPeerAgent`. The `info` part is the basic information setting of the agent, the `plan` part contains the behavior planning setting of the agent (determining the working mode of the agent), and the `metadata` part contains the metadata setting of the agent object.

`planner` field defines a `peer_planner` configuration, in which the `planning`, `executing`, `expressing`, and `reviewing` fields define the agent configuration of the four stages of PEER. You can continue to create sub-agents corresponding to each stage, and the configuration of each sub-agent can use different agent pattern modes.

### More Details
For more details on agent pattern development, please refer to the subsequent agent pattern chapters.

### Create an Agent Class in Collaboration Mode
Create a `xx_agent_case_b.py` file with the same name in the `agent` directory of your project.


## Test and tune the performance of the agent
After the agent is developed, we need to test the agent to verify its performance. You can use the `unittest` framework to test the agent. Here is an example of a test case for the `DemoRagAgent` agent:
```python
import unittest
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse


class RagAgentTest(unittest.TestCase):
    """
    Test cases for the rag agent
    """

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_rag_agent(self):
        """Test demo rag agent."""
        instance: Agent = AgentManager().get_instance_obj('demo_rag_agent')
        output_object: OutputObject = instance.run(input='英伟达股票大涨原因是什么？')
        print(output_object.get_data('output'))


if __name__ == '__main__':
    unittest.main()
```
In the `RagAgentTest` class, we define a test case for the `DemoRagAgent` agent. In the `setUp` method, we start the `agentuniverse` framework. In the `test_rag_agent` method, we get the instance object of the `demo_rag_agent` agent through `AgentManager().get_instance_obj`, and then execute the agent's logic through the `instance.run` method.

Through testing, you can observe whether the agent's reasoning and answers meet your expectations, and optimize the corresponding settings, enhance tools and knowledge, continuously repeating this step until the results are satisfactory.

## Quickly serve the agent
### Use Configuration to Register Services
Create a `xx_service.yaml` file in the `service` directory of your project. The content is as follows:
```yaml
name: 'demo_service'
description: 'demo service of demo agent'
agent: 'demo_rag_agent'
metadata:
  type: 'SERVICE'
```
In `xx_service.yaml`, we define a `demo_service` configuration. The `name` field defines the name of the service, the `description` field defines the description of the service, and the `agent` field defines which agent provides the service.

### Start the Service
Start using the `server_application.py` file found in the `boostrap` folder within your IDE,
or enter the following command in the terminal to start the service interface and begin listening:
```shell
# under the boostrap directory of the project
cd `your boostrap directory path`
python server_application.py
```

When the command line shows that the service is listening successfully, the service is started. By default, the service listens on the address `127.0.0.1` and port `8000`, with 5 workers. You can modify the configuration in `config/gunicorn_config.toml`.(Note that on Windows systems and when directly using Flask to start, the default listening port is currently 8888.)
![image](../../_picture/1_3_Quick%20Start_0.png)

### Access the Service
#### Local Access
You can access the service through the terminal using the curl command or tools like Postman. The curl access command is as follows:
```shell
curl http://127.0.0.1:8000/service_run -X POST --header "Content-Type: application/json;charset=UTF-8" -d '{"service_id":"demo_service", "params":{"input":"Your input text here"}}'
```

#### Remote Access
If your service is deployed on a remote server, you can access it through a domain name or IP address.

### More Details
For more details on service development, please refer to the subsequent service chapters. In addition to the standard HTTP service development method, we will also extend the gRPC service development method in the near future. You can choose the appropriate service development method according to your needs.

## Summary
Through this chapter, you have learned how to use this framework to prepare the environment and application engineering, how to build a simple agent, how to use pattern components to achieve multi-agent collaboration, how to test and tune the performance of agents, and how to quickly serve agents. 

The actual capabilities of this framework are far more extensive than this. You can continue to read the following sections:
* Further study the principles and core components of the framework;
* Further enhance the capabilities of your agents by combining the framework with professional tools, knowledge, and evaluation methods;
* Further apply the framework to provide end-to-end solutions and products;
* Further read the best practices of the framework in various industry scenarios.

Let's explore and progress together!
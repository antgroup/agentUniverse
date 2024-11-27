# How to create agents.
You might have already learned how to quickly create an agent in the [Quick Start](1_3_Quick_Start.md) chapter, or grasped the important components of an agent in the [Principles of Agents](2_2_1_Agent.md). In this section, we will further elaborate on how to create an agent in detail.

Based on the design features of the agentUniverse domain components, creating an agent consists of two parts during the creation process.
* agent_xx.yaml
* agent_xx.py

Among them, `agent_xx.yaml` must be created, which includes important attribute information of the agent such as Introduction, Target, Instruction, LLM, etc.; `agent_xx.py` is created as needed, containing specific behaviors of the agent and supporting users to inject custom domain behaviors into the agent. Understanding this principle, let's take a closer look at how to create these two parts.

## Creating Agent Configuration - agent_xx.yaml
We will provide detailed descriptions of each component in the configuration.

### Setting the basic information of the agent.
**`info` - basic information of the agent**
* `name`:  name of the agent
* `description`:  description of the agent

### Setting the global configurations for the agent.
**`profile` - Agent global settings.**
* `introduction`:  introduction to the agent's role
* `target`:  target of the agent
* `instruction`: instruction of the agent
* `llm_model`: The LLM used by the agent
  * `name`: name of LLM
  * `model_name`: model_name of LLM

  You can choose any existing LLM or connect to any LLM of your choice. We will not elaborate on this part here; you can refer to the [LLM section](2_2_2_LLM.md) for more details.

### Setting the agent's plan
**`plan` - plan of agent**
* `planner` : planner of agent
  * `name`: name of planner
  
  You can choose any existing Planner or connect to any Planner of your choice. We will not elaborate on this part here; you can refer to the Planner section for more details.

### Setting the agent's action
**`action` - action of agent**
* `Tool` : Tools available for the agent's use.
  * tool_name_list，list of tool names, for example:  
    \- tool_name_a  
    \- tool_name_b  
    \- tool_name_c  

  You can choose any existing Tool or connect to any Tool of your choice. We will not elaborate on this part here; you can refer to the [Tool section](2_2_3_Tool.md) for more details.

* `Knowledge` : Knowledge available for the agent's use.
  * knowledge_name_list，list of knowledge names, for example:   
    \- knowledge_name_a  
    \- knowledge_name_b  
    \- knowledge_name_c
  
  You can choose any existing Knowledge or connect to any Knowledge of your choice. We will not elaborate on this part here; you can refer to the Knowledge section for more details.

### Setting up the agent's memory.
**`memory` - memory of agent**

The agent already has a default memory mode built-in, so you do not need to set it up. Additionally, memory supports customization and type selection, and we will make this capability available in an upcoming feature.

### Setting up component metadata.
**`metadata` - metadata of component**
* `type` : type of component，use 'AGENT'
* `module`: Agent entity package path
* `class`: Agent entity class name

All provided Agent components will have their corresponding `module` and `class` copied to this section. This section will integrate all configurations and behaviors of the agent into a whole. If you have extended the behavior of the agent, you need to fill in this section according to the actual path. We will further explain this in the "Creating from an Existing Agent Object" section later in the text.

### An actual example of an agent configuration.
```yaml
info:
  name: 'demo_rag_agent'
  description: 'demo rag agent'
profile:
  introduction: You are an AI assistant proficient in information analysis.
  target: Your goal is to determine whether the answer to a question provides valuable information and to make suggestions and evaluations about the answer.
  instruction: |
    The rules you need to follow are:

    1.Must answer the question posed by the user in Chinese, combining the background information and your knowledge.
    2.Generate structured answers, and when necessary, use blank lines to enhance the reading experience.
    3.Do not adopt incorrect information from the background.
    4.Consider the relevance of the answer to the question, and do not provide answers that are not helpful to the question.
    5.Answer the question comprehensively, with emphasis on the main points, without excessive fancy wording.
    6.Do not make vague speculations.
    7.Use numerical information as much as possible. 
    
    Background information is: {background} 
    
    Begin! 
    
    The question to answer is: {input}
  llm_model:
    name: 'demo_llm'
    model_name: 'gpt-4o'
plan:
  planner:
    name: 'rag_planner'
action:
  tool:
    - 'google_search_tool'
#  knowledge:
#    - 'knowledge_a'
metadata:
  type: 'AGENT'
  module: 'sample_standard_app.intelligence.agentic.agent.agent_instance.rag_agent_case.demo_rag_agent'
  class: 'DemoRagAgent'
```
The above is an actual example of an agent configuration. In addition to the standard configuration items introduced above, the observant among you may have noticed variables in the prompt like `{background}` and `{input}`. This is a very practical prompt replacement feature, which we will explain in the section [How to dynamically adjust settings based on user input](#How to dynamically adjust settings based on user input).

You can find more agent configuration YAML examples in our sample project under the path `sample_standard_app.intelligence.agentic.agent`.

In addition to this, agentUniverse does not restrict users from extending the YAML configuration content for agents. You can create any custom configuration key according to your own requirements, but please be careful not to duplicate the default configuration keywords mentioned above.

## Creating Agent Domain Behavior Definition agent_xx.py
In this section, you can orchestrate and customize the behavior of any agent. Of course, if you are completely using existing Agent capabilities, this section is not mandatory.

In this section, we will focus on commonly used definitions of agent domain behavior and the common techniques you may use in the actual process of defining agent domain behaviors.

### Create an Agent class object.
Create the corresponding Agent class object and inherit the AgentUniverse framework's base class Agent.

### Customize the corresponding agent domain behaviors.
Common customizable agent behaviors are as follows.

#### input_keys method
Represents the list of input key parameters from users in the agent's execution process, which needs to be implemented by each custom Agent class.

For example, if the agent runs with only one parameter passed in, such as question=xxx, then the input_keys method should return ['question'].

#### output_keys method
Represents the list of output key parameters when the agent's execution ends, which needs to be implemented by each custom Agent class.

For example, if the agent outputs a result that includes a response, then the output_keys method should return ['response'].

#### parse_input method
The input processing node before agent execution; an agent's input can be natural language or structured data such as JSON. You can process any user input in this part, and it needs to be implemented by each custom Agent class.

This section has two input parameters, as follows:

* `input_object`: The original data inputted to the agent
  * You can retrieve corresponding data from input_object using the `input_object.get_data('input_key')` method.
  
    For example, if a user inputs `question=xxx` to the agent, we can obtain the current question from the user by using `input_object.get_data('question')`.

* `agent_input`: The data processed by the agent's input handler, of type `dict`.
  * `agent_input` includes the following key parameters and data by default.
    * `chat_history`: Includes historical chat data.
    * `background`: Includes background.
    * `date`: Includes the current date.
  * Append the user input to agent_input.
    * For example: `agent_input['input'] = input_object.get_data('question')`.
  
The output object for the `parse_input` method is generally used `agent_input`.

#### parse_result method
The output processing node before agent execution, where an agent's output can be natural language or structured data such as JSON. You can manage any content that needs to be output in this part, and it needs to be implemented by each custom Agent class.

This section has one input parameter, as follows:
* `agent_result`: Agent output data, of type `dict`.  
* The output object for the `parse_result` method is typically used `agent_result`.

#### execute method
This method is the core entry point for the agent's execution flow. The agent's base class implements the execution method by default, and users can also override this method to customize the execution method for any agent.

##### Default execute implementation.
* The default logic for the execute method in the agent base class is as follows:

  * Get the planner name corresponding to the agent YAML configuration
  * Obtain a Planner instance through the Planner manager
  * Execute the invoke method of the Planner instance

##### Custom execute implementation.
You can also customize the execution flow of the agent by overriding the execute method. Overriding execute will override the default implementation of the agent's base class, meaning the agent will lose the ability to automatically select a Planner. If needed, you can refer to the default implementation of the agent's base class to load and use the corresponding planner.

Below is an example of a custom execute implementation:
```text
def execute(self, input_object: InputObject, agent_input: dict) -> dict:
    # Do anything, as exemplified below.
    
    # Invoke tool A to get data.
    
    # Analyze the data and determine whether it can answer the user's questions.
    
    # Organize language to answer questions.
    
    # Output the answer.
    
    return {'output': 'xxx'}
```

#### Get the properties of the agent object.
Through `self.agent_model`, the agent object can access the properties of the agent. In the definition of agent domain behaviors, you can read all the properties configured in the agent configuration section.

A specific example is as follows:
```text
def execute(self, input_object: InputObject, agent_input: dict) -> dict:
    """Execute agent instance.

    Args:
        input_object (InputObject): input parameters passed by the user.
        agent_input (dict): agent input parsed from `input_object` by the user.

    Returns:
        dict: planner result generated by the planner execution.
    """

    planner_base: Planner = PlannerManager().get_instance_obj(self.agent_model.plan.get('planner').get('name'))
    planner_result = planner_base.invoke(self.agent_model, agent_input, input_object)
    return planner_result
```

In this example, the `plan` section from the agent configuration attributes is accessed within the execution method using `self.agent_model.plan`, and further, the actual name of the `planner` is obtained through the get method.


The properties and domain behaviors of the agent are both dependent on the Agent base class in the agentUniverse framework, which is located at `agentuniverse.agent.agent.Agent`. We will also focus on the underlying objects in the sections on agents and related domain objects. If you are interested in the underlying technical implementation, you can further refer to the corresponding code and documentation.

#### An actual example of an agent domain behavior definition.
```python
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.plan.planner.planner import Planner
from agentuniverse.agent.plan.planner.planner_manager import PlannerManager

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

    # def execute(self, input_object: InputObject, agent_input: dict) -> dict:    
    #     planner_base: Planner = PlannerManager().get_instance_obj(self.agent_model.plan.get('planner').get('name'))
    #     planner_result = planner_base.invoke(self.agent_model, agent_input, input_object)
    #     return planner_result
```
The above is an actual example of an agent domain behavior definition.

## Pay attention to the package path where your defined agent is located
With the above agent configuration and domain definition part, you have mastered all the steps to create an agent; next, we will use these agents. Before using, please ensure that the created agents are within the correct package scanning path.

In the `config.toml` of the agentUniverse project, you need to configure the package corresponding to the agent file. Please confirm again that the package path where your created file is located is under the `CORE_PACKAGE` in the `agent` path or its subpaths.

Taking the configuration of the example project as a reference, it would be as follows：

```yaml
[CORE_PACKAGE]
# Scan and register agent components for all paths under this list, with priority over the default.
agent = ['sample_standard_app.intelligence.agentic.agent']
```

## Other techniques for agent development
### Customize and orchestrate the execution process of agents freely
In the [Creating Agent Domain Behavior Definitions](#Creating Agent Domain Behavior Definition-agent_xx.py) section of this document, we have already detailed how to customize an execute method. This method is often used in practice customizing processes and inject SOPs (Standard Operating Procedures) according to user demands.

### How to dynamically adjust settings based on user input

**Method 1 (Recommended): Through the standard prompt template variable replacement method.**  

In [An actual example of an agent configuration](#An actual example of an agent configuration.) section of this document, the prompt includes variables like `{background}`,`{input}`, etc. This feature is the prompt variable template replacement function, aimed at dynamically influencing the prompt based on the user's input. One only needs to define the text using `{variable}` format in the agent configuration settings section, and define it in the parse_input's `agent_input` to dynamically replace the corresponding prompt based on the input portion.

For example, in the sample agent `sample_standard_app.intelligence.agentic.agent.agent_instance.rag_agent_case.demo_rag_agent.py`, there is the following `parse_input` method.

```text
def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
    agent_input['input'] = input_object.get_data('input')
    return agent_input
```

In its agent settings `sample_standard_app.intelligence.agentic.agent.agent_instance.rag_agent_case.demo_rag_agent.yaml`, in the `instruction` section, we can see the following configuration.

```text
instruction: |
    The rules you need to follow are:

    1.Must answer the question posed by the user in Chinese, combining the background information and your knowledge.
    2.Generate structured answers, and when necessary, use blank lines to enhance the reading experience.
    3.Do not adopt incorrect information from the background.
    4.Consider the relevance of the answer to the question, and do not provide answers that are not helpful to the question.
    5.Answer the question comprehensively, with emphasis on the main points, without excessive fancy wording.
    6.Do not make vague speculations.
    7.Use numerical information as much as possible. 
    
    Background information is: {background} 
    
    Begin! 
    
    The question to answer is: {input}
```

Through this process, we can bring each input, memory or background knowledge, and any information you care about into the interaction between the agent and the LLM using this method.

**Method 2: Adjust the prompt within the parse_input method or the execute method**

Through the agent's `parse_input` method or `execute` method, we can customize the agent in terms of data or behavior. Additionally, by combining the get method in `self.agent_model` with the agent input parameter `input_object`, this means that you can modify any of your settings content through these customization methods.

### Create an agent from an existing agent object

In the actual process of creating applications, we may have many agents of the same type. For example, we might want to create several Retrieval Augmented Generation (RAG) type agents to be used in different question-answering scenarios. By analyzing their similarities and differences, it is not difficult to find that most RAG type agents share the following commonalities and differences:

* Main similarity: They often need to retrieve multiple types of knowledge simultaneously.
* Main difference: RAG agents in different scenarios need to retrieve using different tools and may have different global agent settings.

Upon further analysis, we can achieve this goal through the same domain behavior and differentiated attribute configurations. This is why configuring settings in YAML is essential during the agent creation process, while domain behavior customization is based on actual needs.

Fortunately, we have a significant number of effective agent types, and they are still expanding. As described in this case, combining the agent domain component setting process, we only need to set different types of agent configuration YAMLs, and complete this goal by setting `metadata`.


For example:

**Financial RAG Agent Settings**
```yaml
info:
  name: 'financial_RAG_agent'
  description: 'demo financial rag agent'
profile:
  introduction:  Demo introduction, such as you are a financial RAG agent.
  target: Demo target, such as use financial tools to retrieve and enhance answer performance.
  instruction: |
    demo instruction, xxx, {input}
  llm_model:
    name: 'demo_llm'
    model_name: 'gpt-4o'
plan:
  planner:
    name: 'rag_planner'
action:
  tool:
    - 'financial_data_tool'
metadata:
  type: 'AGENT'
  module: 'agentuniverse.agent.default.rag_agent.rag_agent'
  class: 'RagAgent'
```

**Tech RAG Agent Settings**
```yaml
info:
  name: 'tech_RAG_agent'
  description: 'demo tech rag agent'
profile:
  introduction:  Demo introduction, such as you are a tech RAG agent.
  target: Demo target, such as use tech tools to retrieve and enhance answer performance.
  instruction: |
    demo instruction, xxx, {input}
  llm_model:
    name: 'demo_llm'
    model_name: 'gpt-4o'
plan:
  planner:
    name: 'rag_planner'
action:
  tool:
    - 'tech_data_tool'
metadata:
  type: 'AGENT'
  module: 'agentuniverse.agent.default.rag_agent.rag_agent'
  class: 'RagAgent'
```

You can find more information about existing agents and understand their roles in the [Learn more about agents](#Learn more about agents) section of this document.

# How to Use an Agent
In the agentUniverse, all agent entities are managed by a global agent manager. If you need to use an agent during any framework execution process, you can do so through the agent manager. Additionally, leveraging the framework's service capabilities, you can quickly turn an agent into a service and make network calls to it using standard HTTP or RPC protocols.

## Solution 1: Use the agent manager

Through the `get_instance_obj('agent_name_xxx')` method in the agent manager, you can obtain the agent instance with the corresponding name. Meanwhile, the agent can be utilized through its own `run(input='xxx')` method. The `test_rag_agent(self)` method in the test class below demonstrates debugging the agent using this approach.

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
        output_object: OutputObject = instance.run(input="What is the reason for the sharp rise in Nvidia's stock?")
        print(output_object.get_data('output'))

if __name__ == '__main__':
    unittest.main()
```

## Solution 2: Utilize the service capabilities of agent_serve

The agentUniverse offers a variety of standard web serve capabilities, along with standard HTTP and RPC protocols. You can further refer to the documentation sections on [Service Registration and Usage](2_4_1_Service_Registration_and_Usage.md) and [Web_Server](2_4_1_Web_Server.md).

# Learn more about agents
The agents provided by the framework can be found under the `agentuniverse.agent.default` package path. You can further explore the corresponding code or learn more about them in our extension component introduction section.

# Conclusion
By now, you have mastered all the content related to the creation and use of agents. Let's use this knowledge to customize your own exclusive agent.
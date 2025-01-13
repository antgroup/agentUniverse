# Python Auto Runner
## Case Illustration
This case is built using ReactPlanner, creating a simple application that can automatically generate and execute Python code.
This case is leverages the QianWen large language model and the google_search function, necessitating the configuration of environment variables DASHSCOPE_API_KEY and SERPER_API_KEY prior to use.

## Quick Start
### Configure API Key
For instance, configure key information in the custom_key.toml file, which is where agentUniverse manages private keys (the default setup uses qwen as the base model and serper as the google search tool).
```toml
[KEY_LIST]
# serper google search key
SERPER_API_KEY='xxx'
# openai api key
DASHSCOPE_API_KEY='xxx'
```

### Agent Configuration
```yaml
info:
  name: 'demo_react_agent'
  description: 'react agent'
profile:
  prompt_version: qwen_react_agent.cn
  llm_model:
    name: 'default_qwen_llm'
    model_name : 'qwen-max'
    temperature: 0
action:
  tool:
    - 'google_search_tool'
    - 'python_runner'
plan:
  planner:
    name: 'react_planner'
metadata:
  type: 'AGENT'
  module: 'agentuniverse.agent.default.react_agent.react_agent'
  class: 'ReActAgent'
```

Here we used two tools: google_search_tool and python_runner. The relevant tool code links are as follows:
- [google_search_tool](../../../../examples/sample_apps/react_agent_app/intelligence/agentic/tool/google_search_tool.yaml)
- [python_runner](../../../../examples/sample_apps/react_agent_app/intelligence/agentic/tool/python_runner.yaml)


### Case Run
1. Test Case Run
Directly run with test code[test_case](../../../../examples/sample_apps/react_agent_app/intelligence/test/test_react_agent.py)
2. Interface Run
After configuring the related keys, start the web service and use the following curl for testing.
```shell
curl --location --request POST 'http://localhost:8888/service_run' \
--header 'Cookie: spanner=fQ47DxJmWYzf8rKDhs69LExySZYZFUiVXt2T4qEYgj0' \
--header 'Content-Type: application/json' \
--data-raw '{
    
    "service_id": "demo_react_service",
    "params": {
        "input": "请帮我生成一段python代码，可以计算三数之和"
    }
}'
```

### Result
![test_case](../../_picture/react_demo_step.png)

In the image, React underwent a total of three steps:
Step 1: The model provided a piece of Python code and submitted it to the Python Runner tool for execution. However,  the execution failed due to an inability to use print to output the execution result.
Step 2: The model recognized the mistake and proactively revised the code. It then resubmitted the code to the Python Runner tool for execution, which was successful this time.
Step 3: The model conveyed the successfully executed code to the user.  

### Please note
Due to limitations of the model's capabilities, it is recommended to use the qwen-max model for testing.
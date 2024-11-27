# Python Auto Runner
## Case Illustration
This case is based on ReactPlanner, building a simple case that can automatically generate and execute Python code.
This case is based on the QianWen large language model and the google_search function, requiring you to configure the environment variables DASHSCOPE_API_KEY, SERPER_API_KEY before use.

## Quick Start
### Configure API Key
For example, configure key information in the file custom_key.toml where agentUniverse manages private keys (the default discussion group uses qwen as the base model and serper as the google search tool).
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
- [google_search_tool](../../../sample_standard_app/intelligence/agentic/tool/google_search_tool.yaml)
- [python_runner](../../../sample_standard_app/intelligence/agentic/tool/python_repl_tool.yaml)


### Case Run
1. Test Case Run
Directly run with test code[test_case](../../../sample_standard_app/intelligence/test/test_react_agent.py)
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
![test_case](../_picture/react_demo_step.png)

In the image, React went through three steps in total:  
Step 1: The model provided a piece of Python code and handed it over to the Python Runner tool for execution, but the execution failed due to the failure to use print to output the execution result.  
Step 2: The model realized the mistake and proactively modified the code. It then used the Python Runner tool again for execution, which was successful.  
Step 3: The model conveyed the successfully executed code to the user.  

### Please note
Due to limitations of the model's capabilities, it is recommended to use the qwen-max model for testing.
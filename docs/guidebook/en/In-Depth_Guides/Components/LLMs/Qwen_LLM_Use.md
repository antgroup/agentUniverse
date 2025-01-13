# Qwen Use
## 1. Create the relevant file.
Create a YAML file, for example, user_qwen.yaml
Paste the following content into your user_qwen.yaml file.
```yaml
name: 'user_qwen_llm'
description: 'user qwen llm with spi'
model_name: 'qwen-turbo'
max_tokens: 1000
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.qwen_openai_style_llm'
  class: 'QWenOpenAIStyleLLM'
```
## 2. Environment Setup
Must be configured:DASHSCOPE_API_KEY  
Optional: DASHSCOPE_PROXY
### 2.1 Configure through Python code
```python
import os
os.environ['DASHSCOPE_API_KEY'] = 'sk-***'
os.environ['DASHSCOPE_PROXY'] = 'https://xxxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
DASHSCOPE_API_KEY="sk-******"
DASHSCOPE_PROXY="https://xxxxxx"
```
## 3. Obtaining the DASHSCOPE API KEY 
Reference Dashscope Official Documentation：https://dashscope.console.aliyun.com/apiKey

## 4. Tips
In agentuniverse, we have already created an llm with the name default_qwen_llm. After configuring the DASHSCOPE_API_KEY, users can directly use it.



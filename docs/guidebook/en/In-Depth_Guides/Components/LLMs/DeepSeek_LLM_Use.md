# DeepSeek  Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_deepseek_llm.yaml
Paste the following content into your user_deepseek_llm.yaml file.
```yaml
name: 'user_deepseek_llm'
description: 'default default_deepseek_llm llm with spi'
model_name: 'deepseek-chat'
max_tokens: 1000
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.deep_seek_openai_style_llm'
  class: 'DefaultDeepSeekLLM'
```
##  2. Environment Setup
Must be configured: DEEPSEEK_API_KEY  
Optional: DEEPSEEK_API_BASE
### 2.1 Configure through Python code
```python
import os
os.environ['DEEPSEEK_API_KEY'] = 'sk-***'
os.environ['DEEPSEEK_API_BASE'] = 'https://xxxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
DEEPSEEK_API_KEY="sk-******"
DEEPSEEK_API_BASE="https://xxxxxx"
```
## 3. Obtaining the DeepSeek API KEY 
Please refer to the official documentation of DEEPSEEK:https://platform.deepseek.com/api_keys

## 4. Tips
In the agentuniverse, we have established an LLM named default_deepseek_llm. Users can directly utilize it after configuring their DEEPSEEK_API_KEY.


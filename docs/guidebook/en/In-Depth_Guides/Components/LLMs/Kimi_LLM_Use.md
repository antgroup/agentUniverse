# KIMI Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_kimi.yaml
Paste the following content into your user_kimi.yaml file.
```yaml
name: 'user_kimi_llm'
description: 'user kimi llm with spi'
model_name: 'moonshot-v1-8k'
max_tokens: 1000
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.kimi_openai_style_llm'
  class: 'KIMIOpenAIStyleLLM'
```
## 2. Environment Setup
Must be configured: KIMI_API_KEY
Optional: KIMI_PROXY
### 2.1 Configure through Python code
```python
import os
os.environ['KIMI_API_KEY'] = 'sk-***'
os.environ['KIMI_PROXY'] = 'https://xxxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
KIMI_API_KEY="sk-******"
KIMI_PROXY="https://xxxxxx" 
```
## 3. Obtaining the KIMI API KEY 
Reference KIMI Official Documentation:https://platform.moonshot.cn/console/api-keys

## 4. Tips
In agentuniverse, we have already created an llm with the name default_kimi_llm. After configuring the KIMI_API_KEY, users can directly use it.

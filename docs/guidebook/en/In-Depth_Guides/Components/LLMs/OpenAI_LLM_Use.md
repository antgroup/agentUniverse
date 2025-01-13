# OpenAI Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_openai.yaml
Paste the following content into your user_openai.yaml file.
```yaml
name: 'user_openai_llm'
description: 'user define openai llm'
model_name: 'gpt-3.5-turbo'
max_tokens: 1000
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.default_openai_llm'
  class: 'DefaultOpenAILLM'
```
## 2. Environment Setup
Must be configured: OPENAI_API_KEY    
Optional: OPENAI_PROXY, OPENAI_API_BASE
### 2.1 Configure through Python code
```python
import os
os.environ['OPENAI_API_KEY'] = 'sk-***'
os.environ['OPENAI_PROXY'] = 'https://xxxxxx'
os.environ['OPENAI_API_BASE'] = 'http://xxxx/v1'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
OPENAI_API_KEY="sk-******"
OPENAI_PROXY="https://xxxxxx"
OPENAI_API_BASE="http://xxxx/v1"
```
## 3. Obtaining the OpenAI API KEY 
[Reference](https://platform.openai.com/account/api-keys)

## 4. Tips
In agentuniverse, we have already created an llm with the name default_openai_llm. After configuring the OPENAI_API_KEY, users can directly use it.



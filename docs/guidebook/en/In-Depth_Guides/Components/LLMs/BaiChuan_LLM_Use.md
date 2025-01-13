# BaiChuan Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_claude.yaml
Paste the following content into your user_claude.yaml file.
```yaml
name: 'user_baichuan_llm'
description: 'user baichuan llm with spi'
model_name: 'Baichuan2-Turbo'
max_tokens: 1000
max_context_length: The maximum length of context
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.baichuan_openai_style_llm'
  class: 'BAICHUANOpenAIStyleLLM'
```
## 2. Environment Setup
### 2.1 Configure through Python code
Must be configured: BAICHUAN_API_KEY  
Optional: BAICHUAN_API_BASE, BAICHUAN_PROXY
```python
import os
os.environ['BAICHUAN_API_KEY'] = 'sk-***'
os.environ['BAICHUAN_PROXY'] = 'https://xxxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
BAICHUAN_API_KEY="sk-******"
BAICHUAN_PROXY="https://xxxxxx"
```
## 3. Obtaining the BAICHUAN API KEY
Reference BaiChuan Official Documentation: https://platform.baichuan-ai.com/console/apikey

## 4. Tips
In agentuniverse, we have already created an llm with the name default_baichuan_llm. After configuring the BAICHUAN_API_KEY, users can directly use it.


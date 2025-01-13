# GLM Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_glm.yaml
Paste the following content into your user_glm.yaml file.
```yaml
name: 'user_zhipu_llm'
description: 'default default_zhipu_llm llm with spi'
model_name: 'glm-4-flash'
max_tokens: 1000
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.zhipu_openai_style_llm'
  class: 'DefaultZhiPuLLM'
```
## 2. Environment Setup
Must be configured: ZHIPU_API_KEY
Optional: ZHIPU_API_BASE
### 2.1 Configure through Python code
```python
import os
os.environ['ZHIPU_API_KEY'] = '*****'
os.environ['ZHIPU_API_BASE'] = 'xxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
ZHIPU_API_KEY='xxxxxx'
ZHIPU_API_BASE='https://open.bigmodel.cn/api/paas/v4/'
```
## 3. Obtaining the GLM API KEY 
Reference GLM Official Documentation: https://maas.aminer.cn

## 4. Tips
In agentuniverse, we have already created a llm with the name default_zhipu_llm. After configuring the ZHIPU_API_KEY, users can directly use it.




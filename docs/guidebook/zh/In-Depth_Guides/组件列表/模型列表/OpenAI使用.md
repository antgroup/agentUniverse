# OpenAI 使用
## 1. 创建相关文件

创建一个yaml文件，例如 user_openai.yaml
将以下内容粘贴到您的user_openai.yaml文件当中
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
## 2. 环境设置
必须配置：OPENAI_API_KEY    
可选配置：OPENAI_PROXY, OPENAI_API_BASE
### 2.1 通过python代码配置
```python
import os
os.environ['OPENAI_API_KEY'] = 'sk-***'
os.environ['OPENAI_PROXY'] = 'https://xxxxxx'
os.environ['OPENAI_API_BASE'] = 'http://xxxx/v1'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
OPENAI_API_KEY="sk-******"
OPENAI_PROXY="https://xxxxxx"
OPENAI_API_BASE="http://xxxx/v1"
```
## 3. API KEY 获取
[参考文档](https://platform.openai.com/account/api-keys)

## 4. Tips
在agentuniverse中，我们已经创建了一个name为default_openai_llm的llm,用户在配置OPENAI_API_KEY之后可以直接使用。


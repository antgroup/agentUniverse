# Qwen 使用
## 1. 创建相关文件

创建一个yaml文件，例如 user_qwen.yaml
将以下内容粘贴到您的user_qwen.yaml文件当中
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
## 2. 环境设置
必须配置：DASHSCOPE_API_KEY  
可选配置：DASHSCOPE_PROXY
### 2.1 通过python代码配置
```python
import os
os.environ['DASHSCOPE_API_KEY'] = 'sk-***'
os.environ['DASHSCOPE_PROXY'] = 'https://xxxxxx'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
DASHSCOPE_API_KEY="sk-******"
DASHSCOPE_PROXY="https://xxxxxx"
```
## 3. DASHSCOPE API KEY 获取
参考 Dashscope 官方文档：https://dashscope.console.aliyun.com/apiKey

## 4. Tips
在agentuniverse中，我们已经创建了一个name为default_qwen_llm的llm,用户在配置DASHSCOPE_API_KEY之后可以直接使用。



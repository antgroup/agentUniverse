# 百川 使用
## 1. 创建相关文件
创建一个yaml文件，例如 user_baichuan.yaml
将以下内容粘贴到您的user_baichuan.yaml文件当中
```yaml
name: 'user_baichuan_llm'
description: 'user baichuan llm with spi'
model_name: 'Baichuan2-Turbo'
max_tokens: 1000
api_key_name: 'BAICHUAN_API_KEY'
api_base_name: 'BAICHUAN_API_BASE'
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.baichuan_openai_style_llm'
  class: 'BAICHUANOpenAIStyleLLM'
```
## 2. 环境设置
### 2.1 通过python代码配置
必须配置：BAICHUAN_API_KEY  
可选配置：BAICHUAN_API_BASE, BAICHUAN_PROXY
```python
import os
os.environ['BAICHUAN_API_KEY'] = 'sk-***'
os.environ['BAICHUAN_PROXY'] = 'https://xxxxxx'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
BAICHUAN_API_KEY="sk-******"
BAICHUAN_PROXY="https://xxxxxx"
```
## 3. BAICHUAN API KEY 获取
参考 百川 官方文档：https://platform.baichuan-ai.com/console/apikey

## 4. Tips
在agentuniverse中，我们已经创建了一个name为default_baichuan_llm的llm,用户在配置BAICHUAN_API_KEY之后可以直接使用。


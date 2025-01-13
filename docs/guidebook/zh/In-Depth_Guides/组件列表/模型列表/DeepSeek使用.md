# DeepSeek 使用
## 1. 创建相关文件
创建一个yaml文件，例如 user_deepseek_llm.yaml
将以下内容粘贴到您的user_deepseek_llm.yaml文件当中
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
## 2. 环境设置
### 2.1 通过python代码配置
必须配置：DEEPSEEK_API_KEY  
可选配置：DEEPSEEK_API_BASE
```python
import os
os.environ['DEEPSEEK_API_KEY'] = 'sk-***'
os.environ['DEEPSEEK_API_BASE'] = 'https://xxxxxx'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
DEEPSEEK_API_KEY="sk-******"
DEEPSEEK_API_BASE="https://xxxxxx"
```
## 3. DEEPSEEK API KEY 获取
参考 DEEPSEEK 官方文档：https://platform.deepseek.com/api_keys

## 4. Tips
在agentuniverse中，我们已经创建了一个name为default_deepseek_llm的llm,用户在配置DEEPSEEK_API_KEY之后可以直接使用。


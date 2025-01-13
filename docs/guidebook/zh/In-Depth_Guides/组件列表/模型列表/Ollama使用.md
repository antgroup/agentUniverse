# Ollama 使用
## 1. 创建相关文件
创建一个yaml文件，例如 user_ollama.yaml
将以下内容粘贴到您的user_ollama.yaml文件当中
```yaml
name: 'user_ollama_llm'
description: 'user ollama llm with spi'
model_name: 'qwen2:7b'
max_tokens: 1000
max_context_length: 32000
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.default_ollama_llm'
  class: 'OllamaLLM'
```
## 2. 环境设置
### 2.1 通过python代码配置
必须配置：OLLAMA_BASE_URL
```python
import os
os.environ['OLLAMA_BASE_URL'] = 'https://xxxxxx'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
OLLAMA_BASE_URL="https://xxxxxx"
```

## 3. Tips
在agentuniverse中，我们已经创建了一个name为default_ollama_llm的llm,用户在配置OLLAMA_BASE_URL之后可以直接使用。
使用ollama参考官方地址：https://www.ollama.com/library/qwen2


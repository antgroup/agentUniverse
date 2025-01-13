# Ollama Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_ollama.yaml
Paste the following content into your user_ollama.yaml file.
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
## 2. Environment Setup
### 2.1 Configure through Python code
Must be configured: OLLAMA_BASE_URL
```python
import os
os.environ['OLLAMA_BASE_URL'] = 'https://xxxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
OLLAMA_BASE_URL="https://xxxxxx"
```

## 4. Tips
In agentuniverse, we have already created an llm with the name default_ollama_llm. After configuring the OLLAMA_BASE_URL, users can directly use it.
Reference: https://www.ollama.com/library/qwen2


# Calude Usage
## 1. Create the relevant file.
Create a YAML file, for example, user_claude.yaml
Paste the following content into your user_claude.yaml file.
```yaml
name: 'user_claude_llm'
description: 'user claude llm with spi'
model_name: 'claude-3-opus-20240229'
max_tokens: 4096
metadata:
  type: 'LLM'
  module: 'agentuniverse.llm.default.claude_llm'
  class: 'ClaudeLLM'
```
## 2. Environment Setup
Must be configured: ANTHROPIC_API_KEY  
Optional: ANTHROPIC_API_URL
### 2.1 Configure through Python code
```python
import os
os.environ['ANTHROPIC_API_KEY'] = 'sk-***'
os.environ['ANTHROPIC_API_URL'] = 'https://xxxxxx'
```
### 2.2 Configure through the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
ANTHROPIC_API_KEY="sk-******"
ANTHROPIC_API_URL="https://xxxxxx"
```
## 3. Obtaining the ANTHROPIC API KEY
Reference Claude Official Documentation: https://docs.anthropic.com/zh-CN/docs/getting-access-to-claude

## 4. Note
In agentuniverse, we have already created an llm with the name default_claude_llm. After configuring the ANTHROPIC_API_KEY, users can directly use it.
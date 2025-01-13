# Claude 使用
## 1. 创建相关文件
创建一个yaml文件，例如 user_claude.yaml
将以下内容粘贴到您的user_claude.yaml文件当中
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
## 2. 环境设置
必须配置：ANTHROPIC_API_KEY  
选配：ANTHROPIC_API_URL
### 2.1 通过python代码配置
```python
import os
os.environ['ANTHROPIC_API_KEY'] = 'sk-***'
os.environ['ANTHROPIC_API_URL'] = 'https://xxxxxx'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
ANTHROPIC_API_KEY="sk-******"
ANTHROPIC_API_URL="https://xxxxxx"
```
## 3. Claude API KEY 获取
参考 Claude 官方文档：https://docs.anthropic.com/zh-CN/docs/getting-access-to-claude

## 4. 注意
在agentuniverse中，我们已经创建了一个name为default_claude_llm的llm,用户在配置ANTHROPIC_API_KEY之后可以直接使用
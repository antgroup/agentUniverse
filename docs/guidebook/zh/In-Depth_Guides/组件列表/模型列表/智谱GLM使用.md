# GLM 使用
## 1. 创建相关文件
创建一个yaml文件，例如 user_glm.yaml
将以下内容粘贴到您的user_glm.yaml文件当中
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
## 2. 环境设置
必须配置：ZHIPU_API_KEY、ZHIPU_API_BASE
### 2.1 通过python代码配置
```python
import os
os.environ['ZHIPU_API_KEY'] = '*****'
os.environ['ZHIPU_API_BASE'] = 'xxxxx'
```
### 2.2 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
ZHIPU_API_KEY='xxxxxx'
ZHIPU_API_BASE='https://open.bigmodel.cn/api/paas/v4/'
```
## 3.ZHIPU API KEY 获取
参考 智谱GLM 官方文档：https://maas.aminer.cn

## 4. Tips
在agentuniverse中，我们已经创建了一个name为default_zhipu_llm的llm,用户在配置ZHIPU_API_KEY、ZHIPU_API_BASE之后可以直接使用。




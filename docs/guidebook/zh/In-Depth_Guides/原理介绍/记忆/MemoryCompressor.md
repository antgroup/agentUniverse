# MemoryCompressor

MemoryCompressor负责在记忆组件的prune裁剪记忆流程中，对裁剪的记忆进行压缩总结，合成满足token数限制的最终记忆信息。

## 如何定义MemoryCompressor组件

根据agentUniverse领域组件的设计特性，同其他组件一样，创建一个记忆压缩器memory_compressor定义由2部分组成:

- xx_memory_compressor.yaml
- xx_memory_compressor.py

xx_memory_compressor.yaml包含了memory_compressor组件的名称、描述、压缩记忆使用的prompt版本、压缩记忆使用的llm模型名称等重要信息；xx_memory_compressor.py包含了记忆压缩器的具体定义。理解这一原理后，让我们具体看看该如何创建这两部分内容。

## 如何使用MemoryCompressor组件

### 创建MemoryCompressor配置 - xx_memory_compressor.yaml

#### 一个记忆压缩器定义配置的实际样例

```yaml
name: 'demo_memory_compressor'
description: 'demo memory compressor'
compressor_prompt_version: 'chat_memory.summarizer_cn'
compressor_llm_name: 'qwen_llm'
metadata:
  type: 'MEMORY_COMPRESSOR'
  module: 'agentuniverse.agent.memory.memory_compressor.memory_compressor'
  class: 'MemoryCompressor'
```

- name: 记忆压缩器组件名称，用于标识记忆压缩器
- description: 记忆压缩器描述信息，用于标识记忆压缩器的用途
- compressor_prompt_version:
  记忆压缩器使用的prompt版本，可参考agentUniverse内置的记忆压缩prompt：`chat_memory.summarizer_cn`
- compressor_llm_name: 记忆压缩器使用的llm领域组件名称
- metadata: 组件元数据信息，包括组件类型、组件类名、组件包路径等

### 创建MemoryCompressor领域行为定义 - xx_memory_compressor.py

agentUniverse提供了一个MemoryCompressor基础类，并提供了默认的记忆压缩方法，您可以直接在yaml定义文件中使用该类或是继承它并改写`compress_memory`
函数。

#### [MemoryCompressor类的定义:](../../../../../../agentuniverse/agent/memory/memory_compressor/memory_compressor.py)

- compress_memory(self, new_memories: List[Message], max_tokens: int = 500, existing_memory: str = '', **kwargs) -> str:
  : 记忆信息压缩，将待压缩的记忆信息结合已有的记忆信息，压缩为满足压缩后的记忆信息最大token数限制的最终memory。

### 在Memory中配置使用

如上文中创建的`demo_memory_compressor`实例，在memory中您可以这样设置：

```yaml
name: 'demo_memory'
# omitted part
memory_compressor: demo_memory_compressor
# omitted part
```

### 关注您定义的MEMORY_COMPRESSOR所在的包路径

在agentUniverse项目的config.toml中需要配置MEMORY_COMPRESSOR配置对应的package,
请再次确认您创建的文件所在的包路径是否在`CORE_PACKAGE`中`memory_compressor`路径或其子路径下。

以示例工程中的配置为例，如下：

```yaml
[CORE_PACKAGE]
memory_compressor = ['sample_standard_app.intelligence.agentic.memory.memory_compressor']
```

## agentUniverse目前内置有以下MemoryCompressor:

### [default_memory_compressor](../../../../../../agentuniverse/agent/memory/memory_compressor/default_memory_compressor.yaml)

组件配置文件如下：

```yaml
name: 'default_memory_compressor'
description: 'default memory compressor'
compressor_prompt_version: 'chat_memory.summarizer_cn'
compressor_llm_name: 'default_qwen_llm'
metadata:
  type: 'MEMORY_COMPRESSOR'
  module: 'agentuniverse.agent.memory.memory_compressor.memory_compressor'
  class: 'MemoryCompressor'
```
其中`compressor_prompt_version`为记忆压缩器使用的压缩记忆prompt版本，`compressor_llm_name`为记忆压缩器使用的llm领域组件名称。

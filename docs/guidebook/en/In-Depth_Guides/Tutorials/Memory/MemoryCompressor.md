# MemoryCompressor

MemoryCompressor is responsible for compressing and summarizing the pruned memories in the memory component's pruning
process, synthesizing the final memory information that meets the token limit.

## How to Define a MemoryCompressor Component

Following the design characteristics of agentUniverse domain components, like other components, creating a memory
compressor (memory_compressor) definition consists of two parts:

- xx_memory_compressor.yaml
- xx_memory_compressor.py

xx_memory_compressor.yaml contains important information such as the name, description, prompt version used for
compressing memories, and the name of the LLM model used for compressing memories; xx_memory_compressor.py contains the
specific definition of the memory compressor. After understanding this principle, let's take a look at how to create
these two parts.

## How to Use the MemoryCompressor Component

### Creating a MemoryCompressor Configuration - xx_memory_compressor.yaml

#### An Actual Example of a Memory Compressor Definition Configuration

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
- name: The name of the memory compressor component, used to identify the memory compressor.
- description: The description of the memory compressor, used to indicate the purpose of the memory compressor.
- compressor_prompt_version:
  The version of the prompt used by the memory compressor, you can refer to the built-in memory compression prompt in agentUniverse: `chat_memory.summarizer_en`.
- compressor_llm_name: The name of the LLM domain component used by the memory compressor.
- metadata: Component metadata, including component type, component class name, component package path, etc.

### Creating MemoryCompressor Domain Behavior Definition - xx_memory_compressor.py

agentUniverse provides a base MemoryCompressor class with a default memory compression method. You can either use this class directly in the yaml definition file or inherit it and override the `compress_memory` function.

#### [Definition of MemoryCompressor Class:](../../../../../../agentuniverse/agent/memory/memory_compressor/memory_compressor.py)

- compress_memory(self, new_memories: List[Message], max_tokens: int = 500, existing_memory: str = '', **kwargs) -> str:
  : Memory compression, combines the memories to be compressed with the existing memory information, and compresses it to meet the maximum token limit for the final memory information.

### Configuring and Using in Memory

As with the `demo_memory_compressor` instance created in the previous text, you can set it up in the memory like this:

```yaml
name: 'demo_memory'
# omitted part
memory_compressor: demo_memory_compressor
# omitted part
```

### Pay Attention to the Package Path of Your Defined MEMORY_COMPRESSOR

In the `config.toml` of the agentUniverse project, you need to configure the package corresponding to the MEMORY_COMPRESSOR configuration. Please confirm again that the package path where you created the file is under the `memory_compressor` path in `CORE_PACKAGE` or its sub-path.

For example, the configuration in the sample project is as follows:

```yaml
[CORE_PACKAGE]
memory_compressor = ['sample_standard_app.intelligence.agentic.memory.memory_compressor']
```

## agentUniverse currently has the following built-in MemoryCompressor:

### [default_memory_compressor](../../../../../../agentuniverse/agent/memory/memory_compressor/default_memory_compressor.yaml)

The component configuration file is as follows:

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
Here, `compressor_prompt_version` is the version of the prompt used by the memory compressor for compressing memories, and `compressor_llm_name` is the name of the LLM domain component used by the memory compressor.

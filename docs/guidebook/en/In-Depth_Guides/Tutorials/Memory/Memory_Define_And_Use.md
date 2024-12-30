# How to Define the Memory Component

Based on the design characteristics of the agentUniverse domain components, like other components, creating a memory
definition consists of two parts:

- xx_memory.yaml
- xx_memory.py

xx_memory.yaml contains important information such as the name, description, type, memory compressor, and memory storage
of the memory component; xx_memory.py contains the specific definition of the memory. After understanding this
principle, let's take a look at how to create these two parts.

# How to Use the Memory Component

## Create Memory Configuration - xx_memory.yaml

### An actual example of a memory definition configuration

```yaml
name: 'demo_memory'
description: 'demo memory with multiple storages'
memory_key: 'chat_history'
max_tokens: 3000
memory_compressor: default_memory_compressor
memory_storages:
  - chroma_memory_storage
memory_retrieval_storage: chroma_memory_storage
metadata:
  type: 'MEMORY'
  module: 'agentuniverse.agent.memory.memory'
  class: 'Memory'
```

- name: The name of the memory component
- description: The description of the memory component
- memory_key: The key of the memory component, corresponding to the memory variable name in the agent's prompt
- max_tokens: The token limit for memory information in the prompt; if exceeded, the memory component will automatically compress
- memory_compressor: The compressor of the memory component, used for compressing memory
- memory_storages: A list of memory storages for the memory component, used for multi-route storage of memory; if not configured by the user, the default local_memory_storage local memory storage is used
- memory_retrieval_storage: The storage retrieval of the memory component, representing the source of memory retrieval; if not configured by the user, the first memory storage component in memory_storages is used by default
- metadata: The metadata of the memory component, used to identify the type, module, and class name of the memory component

The aU sample project includes two examples of memory configurations:

1. [demo_memory_with_chroma_storage](../../../../../../examples/sample_standard_app/intelligence/agentic/memory/demo_memory_a.yaml): An example of memory with a chroma storage mounted
2. [demo_memory_with_local_storage](../../../../../../examples/sample_standard_app/intelligence/agentic/memory/demo_memory_b.yaml): An example of memory with a local memory storage mounted

## Creating Memory Domain Behavior Definition - xx_memory.py

agentUniverse provides a standard Memory class, which you can directly use in the yaml definition file or inherit it and override some of its methods.

### [Memory Class Definition:](../../../../../../agentuniverse/agent/memory/memory.py)


- add(self, message_list: List[Message], session_id: str = '', agent_id: str = '', **kwargs) -> None:
  : Adds memory by obtaining multiple `memory_storage` (memory storage) domain components configured in the memory instance, and storing the memory message list, agent ID (agent_id), session ID (session_id), source (memory source), and other information through multi-route storage.

- delete(self, session_id: str = None, **kwargs) -> None:
  : Deletes memory by obtaining multiple `memory_storage` (memory storage) domain components configured in the memory instance, and filtering based on the session ID (session_id) condition to perform multi-route deletion.

- get(self, session_id: str = '', agent_id: str = '', **kwargs) -> List[Message]:
  : Retrieves memory by obtaining the `memory_retrieval_storage` domain component configured in the memory instance (if the user has not configured it, the first memory storage component in `memory_storages` is used by default), and retrieving memory based on the agent ID (agent_id), session ID (session_id), and source (memory source).

- prune(self, memories: List[Message]) -> List[Message]:
  : Prunes and compresses memory by obtaining the `max_tokens` parameter (the maximum number of tokens for memory in the prompt) and the `memory_compressor` (memory compression) domain component configured in the memory instance. If the memory information obtained during the memory retrieval process exceeds the maximum token count, it is pruned and compressed.

## Configuring and Using in Agent

You can set up your memory instance in the agent's memory according to the content in [Creating and Using Agents](../Agent/Agent_Create_And_Use.md). For example, if you have created the `demo_memory` instance mentioned above, you can configure it in the agent like this:

```yaml
info:
  name: 'demo_agent'
  description: 'demo agent'
# omitted part
memory:
  name: 'demo_memory'
# omitted part
```


### Case Study
For example, in the PEER working mode, configure the `demo_memory` instance created above for the three agents in the aU sample project: [demo_planning_agent](../../../../../../examples/sample_standard_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_planning_agent.yaml), [demo_expressing_agent](../../../../../../examples/sample_standard_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_expressing_agent.yaml), and [demo_peer_agent](../../../../../../examples/sample_standard_app/intelligence/agentic/agent/agent_instance/peer_agent_case/demo_peer_agent.yaml). When making a peer call, pass in the `session_id` as `peer_1`. After the call is completed, check the contents of the memory storage as follows:

#### mysql_memory_storage
![mysql_memory](../../../../_picture/mysql_memory.png)

#### chroma_memory_storage
![chroma_memory](../../../../_picture/chroma_memory.png)

## Using the Memory Manager

Through the `.get_instance_obj(xx_memory_name)` method in the Memory Manager, you can obtain the Memory content with the corresponding name.

```python
from agentuniverse.agent.memory.memory_manager import MemoryManager

memory_name = 'xxx'
memory = MemoryManager().get_instance_obj(component_instance_name=memory_name)
```

# Summary

By now, you have mastered the basic usage of Memory. For specific details on the `memory_compressor` and `memory_storage` domain components, you can refer to the [MemoryCompressor Documentation](MemoryCompressor.md) and [MemoryStorage Documentation](MemoryStorage.md).

Go ahead and try using Memory now.

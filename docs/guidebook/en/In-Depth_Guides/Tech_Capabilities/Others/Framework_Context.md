# Framework Context

agentUniverse provides a context management tool that is independent of both threads and coroutines, enabling the storage and retrieval of context variables in a key-value format. These context variables need to be managed independently within threads or coroutines.

## Usage

### Creating Context Variables
#### Method 1:
```python
from agentuniverse.base.context.framework_context import FrameworkContext

with FrameworkContext({"context_var1": 1,
                       "context_var2":"context_var"}):
    pass
```
By using the `with` keyword to create a `FrameworkContext` instance, which accepts a parameter of  type `dict`, agentUniverse will store all key-value pairs from the parameters within the context manager's scope during with block, and will remove them upon exit from the block.
#### Method 2:
```python
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager

FrameworkContextManager().set_context("context_var", "value")
```
You can create a new context variable directly using `FrameworkContextManager` within the AgentUniverse framework. Variables created in this manner will persist throughout the entire lifecycle of the thread or coroutine in which they are created. These variables can be manually deleted using the following code:
```python
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager

FrameworkContextManager().del_context("context_var")
```
### Using Context Variables
You can retrieve previously saved variables through the `FrameworkContextManager`：
```python
from agentuniverse.base.context.framework_context_manager import FrameworkContextManager

FrameworkContextManager().get_context("context_var", default_value=None)
```
The `default_value` is `None` by default. When there is no corresponding key in the context, the `default_value` will be returned.
# modal.call_graph

Source: https://modal.com/docs/reference/modal.call_graph

---

```python
modal.call_graph
modal.call_graph.InputInfo 
class InputInfo(object)
```

Simple data structure storing information about a function input.

```python
def __init__(self, input_id: str, function_call_id: str, task_id: str, status: modal.call_graph.InputStatus, function_name: str, module_name: str, children: list['InputInfo']) -> None
```

```python
modal.call_graph.InputStatus 
class InputStatus(enum.IntEnum)
```

Enum representing status of a function input.

The possible values are:

PENDING
SUCCESS
FAILURE
INIT_FAILURE
TERMINATED
TIMEOUT

# modal.container_process

Source: https://modal.com/docs/reference/modal.container_process

---

```python
modal.container_process
modal.container_process.ContainerProcess 
class ContainerProcess(typing.Generic)
```

Represents a running process in a container.

```python
def __init__(
    self,
    process_id: str,
    task_id: str,
    client: _Client,
    stdout: StreamType = StreamType.PIPE,
    stderr: StreamType = StreamType.PIPE,
    exec_deadline: Optional[float] = None,
    text: bool = True,
    by_line: bool = False,
    command_router_client: Optional[TaskCommandRouterClient] = None,
) -> None:
```

stdout
@property
```python
def stdout(self) -> _StreamReader[T]:
```

StreamReader for the container process’s stdout stream.

stderr
@property
```python
def stderr(self) -> _StreamReader[T]:
```

StreamReader for the container process’s stderr stream.

stdin
@property
```python
def stdin(self) -> _StreamWriter:
```

StreamWriter for the container process’s stdin stream.

returncode
@property
```python
def returncode(self) -> int:
```

poll
```python
def poll(self) -> Optional[int]:
```

Check if the container process has finished running.

Returns None if the process is still running, else returns the exit code.

wait
```python
def wait(self) -> int:
```

Wait for the container process to finish running. Returns the exit code.

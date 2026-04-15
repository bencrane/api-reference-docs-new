# modal.file_io

Source: https://modal.com/docs/reference/modal.file_io

---

```python
modal.file_io
modal.file_io.FileIO 
class FileIO(typing.Generic)
```

[Alpha] FileIO handle, used in the Sandbox filesystem API.

Deprecated on 2026-03-09. Use the Sandbox.filesystem APIs instead.

The API is designed to mimic Python’s io.FileIO.

Currently this API is in Alpha and is subject to change. File I/O operations may be limited in size to 100 MiB, and the throughput of requests is restricted in the current implementation. For our recommendations on large file transfers see the Sandbox filesystem access guide.

Usage

```python
import modal

app = modal.App.lookup("my-app", create_if_missing=True)

sb = modal.Sandbox.create(app=app)
f = sb.open("/tmp/foo.txt", "w")
```

f.write("hello")
f.close()
```python
def __init__(self, client: _Client, task_id: str) -> None:
```

create
@classmethod
```python
def create(
    cls, path: str, mode: Union["_typeshed.OpenTextMode", "_typeshed.OpenBinaryMode"], client: _Client, task_id: str
) -> "_FileIO":
```

Create a new FileIO handle.

read
```python
def read(self, n: Optional[int] = None) -> T:
```

Read n bytes from the current position, or the entire remaining file if n is None.

readline
```python
def readline(self) -> T:
```

Read a single line from the current position.

readlines
```python
def readlines(self) -> Sequence[T]:
```

Read all lines from the current position.

write
```python
def write(self, data: Union[bytes, str]) -> None:
```

Write data to the current position.

Writes may not appear until the entire buffer is flushed, which can be done manually with flush() or automatically when the file is closed.

flush
```python
def flush(self) -> None:
```

Flush the buffer to disk.

seek
```python
def seek(self, offset: int, whence: int = 0) -> None:
```

Move to a new position in the file.

whence defaults to 0 (absolute file positioning); other values are 1 (relative to the current position) and 2 (relative to the file’s end).

ls
@classmethod
```python
def ls(cls, path: str, client: _Client, task_id: str) -> list[str]:
```

List the contents of the provided directory.

mkdir
@classmethod
```python
def mkdir(cls, path: str, client: _Client, task_id: str, parents: bool = False) -> None:
```

Create a new directory.

rm
@classmethod
```python
def rm(cls, path: str, client: _Client, task_id: str, recursive: bool = False) -> None:
```

Remove a file or directory in the Sandbox.

watch
@classmethod
```python
def watch(
    cls,
    path: str,
    client: _Client,
    task_id: str,
    filter: Optional[list[FileWatchEventType]] = None,
    recursive: bool = False,
    timeout: Optional[int] = None,
) -> Iterator[FileWatchEvent]:
```

close
```python
def close(self) -> None:
```

Flush the buffer and close the file.

```python
modal.file_io.FileWatchEvent 
class FileWatchEvent(object)
```

FileWatchEvent(paths: list[str], type: modal.file_io.FileWatchEventType)

```python
def __init__(self, paths: list[str], type: modal.file_io.FileWatchEventType) -> None
```

```python
modal.file_io.FileWatchEventType 
class FileWatchEventType(enum.Enum)
```

An enumeration.

The possible values are:

Unknown
Access
Create
Modify
Remove
```python
modal.file_io.ls 
async def ls(path: str, client: _Client, task_id: str) -> list[str]:
```

List the contents of the provided directory.

```python
modal.file_io.mkdir 
async def mkdir(path: str, client: _Client, task_id: str, parents: bool = False) -> None:
```

Create a new directory.

```python
modal.file_io.rm 
async def rm(path: str, client: _Client, task_id: str, recursive: bool = False) -> None:
```

Remove a file or directory in the Sandbox.

```python
modal.file_io.watch 
async def watch(
    path: str,
    client: _Client,
    task_id: str,
    filter: Optional[list[FileWatchEventType]] = None,
    recursive: bool = False,
    timeout: Optional[int] = None,
) -> AsyncIterator[FileWatchEvent]:
```

Watch a file or directory for changes.

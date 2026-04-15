# modal.SandboxSnapshot

Source: https://modal.com/docs/reference/modal.SandboxSnapshot

---

```python
modal.SandboxSnapshot
class SandboxSnapshot(modal.object.Object)
```

Sandbox memory snapshots are in early preview.

A SandboxSnapshot object lets you interact with a stored Sandbox snapshot that was created by calling ._experimental_snapshot() on a Sandbox instance. This includes both the filesystem and memory state of the original Sandbox at the time the snapshot was taken.

hydrate
```python
def hydrate(self, client: Optional[_Client] = None) -> Self:
```

Synchronize the local object with its identity on the Modal server.

It is rarely necessary to call this method explicitly, as most operations will lazily hydrate when needed. The main use case is when you need to access object metadata, such as its ID.

Added in v0.72.39: This method replaces the deprecated .resolve() method.

from_id
@deprecate_aio_usage((2025, 12, 5), "SandboxSnapshot.from_id")
@classmethod
```python
def from_id(
    cls, sandbox_snapshot_id: str, client: Optional["modal.client.Client"] = None
) -> typing_extensions.Self:
```

Construct a SandboxSnapshot object from a sandbox snapshot ID.

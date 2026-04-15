# modal.Probe

Source: https://modal.com/docs/reference/modal.Probe

---

```python
modal.Probe
class Probe(object)
```

Probe configuration for the Sandbox Readiness Probe.

Usage:

```python
# Wait until a file exists.
readiness_probe = modal.Probe.with_exec(
    "sh", "-c", "test -f /tmp/ready",
)

# Wait until a TCP port is accepting connections.
readiness_probe = modal.Probe.with_tcp(8080)

app = modal.App.lookup('sandbox-readiness-probe', create_if_missing=True)
sandbox = modal.Sandbox.create(
    "python3", "-m", "http.server", "8080",
    readiness_probe=readiness_probe,
    app=app,
)
```

sandbox.wait_until_ready()
```

```python
```python
def __init__(self, tcp_port: Optional[int] = None, exec_argv: Optional[tuple[str, ...]] = None, interval_ms: int = 100) -> None
```

with_tcp
@classmethod
```python
def with_tcp(cls, port: int, *, interval_ms: int = 100) -> "Probe":
```

with_exec
@classmethod
```python
def with_exec(cls, *argv: str, interval_ms: int = 100) -> "Probe":
```

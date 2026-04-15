# modal.Tunnel

Source: https://modal.com/docs/reference/modal.Tunnel

---

```python
modal.Tunnel
class Tunnel(object)
```

A port forwarded from within a running Modal container. Created by modal.forward().

Important: This is an experimental API which may change in the future.

```python
def __init__(self, host: str, port: int, unencrypted_host: str, unencrypted_port: int) -> None
```

url
@property
```python
def url(self) -> str:
```

Get the public HTTPS URL of the forwarded port.

tls_socket
@property
```python
def tls_socket(self) -> tuple[str, int]:
```

Get the public TLS socket as a (host, port) tuple.

tcp_socket
@property
```python
def tcp_socket(self) -> tuple[str, int]:
```

Get the public TCP socket as a (host, port) tuple.

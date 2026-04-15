# modal.Client

Source: https://modal.com/docs/reference/modal.Client

---

```python
modal.Client
class Client(object)
```

is_closed
```python
def is_closed(self) -> bool:
```

hello
```python
def hello(self):
```

Connect to server and retrieve version information; raise appropriate error for various failures.

from_credentials
@classmethod
```python
def from_credentials(cls, token_id: str, token_secret: str) -> "_Client":
```

Constructor based on token credentials; useful for managing Modal on behalf of third-party users.

Usage:

```python
client = modal.Client.from_credentials("my_token_id", "my_token_secret")

modal.Sandbox.create("echo", "hi", client=client, app=app)
```

get_input_plane_metadata
```python
def get_input_plane_metadata(self, input_plane_region: str) -> list[tuple[str, str]]:
```

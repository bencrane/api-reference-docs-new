# modal.is_local

Source: https://modal.com/docs/reference/modal.is_local

---

```python
modal.is_local
def is_local() -> bool:
```

Returns if we are currently on the machine launching/deploying a Modal app

Returns True when executed locally on the user’s machine. Returns False when executed from a Modal container in the cloud.

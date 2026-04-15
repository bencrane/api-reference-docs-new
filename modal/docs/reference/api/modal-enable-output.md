# modal.enable_output

Source: https://modal.com/docs/reference/modal.enable_output

---

```python
modal.enable_output
```

@contextlib.contextmanager
```python
def enable_output() -> Generator[None, None, None]:
```

Context manager that enable output when using the Python SDK.

This will print to stdout and stderr things such as

Logs from running functions
Status of creating objects
Map progress

Example:

```python
app = modal.App()
with modal.enable_output():
    with app.run():
        ...
```

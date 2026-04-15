# modal.Error

Source: https://modal.com/docs/reference/modal.Error

---

```python
modal.Error
class Error(Exception)
```

Base class for all Modal errors. See modal.exception for the specialized error classes.

Usage

```python
import modal

try:
    ...
```

except modal.Error:
```python
    # Catch any exception raised by Modal's systems.
    print("Responding to error...")
```

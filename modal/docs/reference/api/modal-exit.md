# modal.exit

Source: https://modal.com/docs/reference/modal.exit

---

```python
modal.exit
def exit(_warn_parentheses_missing=None) -> Callable[[NullaryMethod], _PartialFunction]:
```

Decorator for methods which should be executed when a container is about to exit.

See the lifeycle function guide for more information.

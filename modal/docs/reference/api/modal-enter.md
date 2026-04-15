# modal.enter

Source: https://modal.com/docs/reference/modal.enter

---

```python
modal.enter
def enter(
    *,
    snap: bool = False,
) -> Callable[[Union[_PartialFunction, NullaryMethod]], _PartialFunction]:
```

Decorator for methods which should be executed when a new container is started.

See the lifeycle function guide for more information.

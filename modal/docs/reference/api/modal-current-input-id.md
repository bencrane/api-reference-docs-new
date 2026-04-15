# modal.current_input_id

Source: https://modal.com/docs/reference/modal.current_input_id

---

```python
modal.current_input_id
def current_input_id() -> Optional[str]:
```

Returns the input ID for the current input.

Can only be called from Modal function (i.e. in a container context).

```python
from modal import current_input_id

@app.function()
def process_stuff():
    print(f"Starting to process {current_input_id()}")
```

# Run your first function

Modal makes it easy to deploy and scale code. To run code on Modal:

1. Create a [Modal App](https://modal.com/docs/reference/modal.App)
2. Wrap a Python function with `@app.function`

Modal takes that code, puts it in a container, and runs it in the cloud.

Click **Run** to see it in action!

## Code

**File:** `get_started.py`

```python
import modal

# 1) Create a Modal App
app = modal.App("example-get-started")


# 2) Add this decorator to run in the cloud
@app.function()
def square(x=2):
    print(f"The square of {x} is {x**2}")  # This runs on a remote worker!
```

## Running

```bash
modal run get_started.py
```

---

**Next:** [2. Customize your container](custom-container.md)

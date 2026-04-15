# Scale out horizontally

Modal can [instantly scale](https://modal.com/docs/guide/scale) to hundreds of containers for your Function. Let's invoke our Function with `.map` to process 100 inputs in parallel.

1. We'll need a way to call the Function outside of the command line. One way to do this is to invoke the Modal Function from another function. Wrap the local caller function with `@app.local_entrypoint`.
2. Call the Modal Function with `.map` and pass in a list of inputs.

## Code

**File:** `scaling_out.py`

```python
import modal

image = modal.Image.debian_slim().pip_install("numpy")

app = modal.App("example-scaling-out", image=image)


@app.function()
def square(x=2):
    import numpy as np

    print(f"The square of {x} is {np.square(x)}")


# 1) Create a local entrypoint function
@app.local_entrypoint()
def main():
    # 2) Run `.map` to process inputs in parallel (wrap with list command to execute)
    list(square.map(range(100)))
```

## Running

```bash
modal run scaling_out.py
```

---

**Previous:** [2. Customize your container](custom-container.md)

**Next:** [4. Run on GPUs](gpu.md)

# Run on GPUs

You can [use GPUs](https://modal.com/docs/guide/gpu) to accelerate your app even further. A common pattern might look like this:

1. Use an officially supported [CUDA image](https://modal.com/docs/guide/cuda#for-more-complex-setups-use-an-officially-supported-cuda-image)
2. Add your GPU dependencies to your Image
3. Attach a GPU to your function with `gpu="A10G"`

Click **Run** to see it in action!

## Code

**File:** `gpu.py`

```python
import subprocess

import modal

image = (
    # 1) Use an officially supported CUDA image
    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")
    # 2) Install cupy, a CUDA replacement for numpy
    .pip_install("cupy-cuda12x")
)

app = modal.App("example-gpu", image=image)


# 3) Attach a GPU to your function
@app.function(gpu="A10G")
def square(x=2):
    import cupy as cp

    subprocess.run(["nvidia-smi"])
    print(f"The square of {x} is {cp.square(x)}")
```

## Running

```bash
modal run gpu.py
```

---

**Previous:** [3. Scale out horizontally](scaling-out.md)

**Next:** [5. Run LLM inference](inference.md)

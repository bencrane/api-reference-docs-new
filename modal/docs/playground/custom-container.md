# Customize your container

Let's see how we can add arbitrary packages for the Modal Function you defined in the previous section:

1. Define a [Modal Image](https://modal.com/docs/guide/images) that pip installs `numpy`
2. Attach this Image to your App
3. Import the library in your Function

Click **Run** to see it in action!

## Code

**File:** `custom_container.py`

```python
import modal

# 1) Define a Modal Image that includes NumPy
image = modal.Image.debian_slim().pip_install("numpy")

# 2) Attach the image
app = modal.App("example-custom-container", image=image)


@app.function()
def square(x=2):
    # 3) Inside the container, import and use the library
    import numpy as np

    print(f"The square of {x} is {np.square(x)}")
```

## Running

```bash
modal run custom_container.py
```

---

**Previous:** [1. Run your first function](get-started.md)

**Next:** [3. Scale out horizontally](scaling-out.md)

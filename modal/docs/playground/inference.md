# Run LLM inference

Modal's cloud GPU infrastructure makes running your own LLMs easy!

1. Install any dependencies your LLM inference needs
2. Attach a GPU to your Function with `gpu="h100"`
3. Run LLM inference code inside the Function

This demo shows an LLM explaining the code of the demo.

Click **Run** to see it in action!

If you want to see what a more sophisticated LLM inference server on Modal looks like,
check out [this example](https://modal.com/docs/examples/llm_inference).

You can also explore our [gallery of other examples](https://modal.com/docs/examples) for inference, training, batch jobs,
sandboxed code execution, and more!

## Code

**File:** `inference.py`

```python
from pathlib import Path

import modal

# 1) Define a Modal Image that includes LLM dependencies
app = modal.App("example-inference")
image = modal.Image.debian_slim().uv_pip_install("transformers[torch]")


# 2) Attach a GPU to your Modal Function
@app.function(gpu="h100", image=image)
def chat(prompt: str | None = None) -> list[dict]:
    # 3) Run LLM inference
    from transformers import pipeline

    if prompt is None:
        prompt = f"/no_think Read this code.\n\n{Path(__file__).read_text()}\nIn one paragraph, what does the code do?"

    print(prompt)
    context = [{"role": "user", "content": prompt}]

    chatbot = pipeline(model="Qwen/Qwen3-1.7B-FP8", device_map="cuda", max_new_tokens=1024)
    result = chatbot(context)
    print(result[0]["generated_text"][-1]["content"])

    return result
```

## Running

```bash
modal run inference.py
```

---

**Previous:** [4. Run on GPUs](gpu.md)

**Next:** [Explore examples](https://modal.com/examples)

# Modal Playground Tutorial

The Modal Playground is an interactive tutorial series that walks you through the basics of running code on Modal's cloud infrastructure. Each step builds on the previous one, progressively introducing new concepts.

Source: https://modal.com/playground/get_started

## Pages

| # | Title | File | URL |
|---|-------|------|-----|
| 1 | Run your first function | [get-started.md](get-started.md) | [/playground/get_started](https://modal.com/playground/get_started) |
| 2 | Customize your container | [custom-container.md](custom-container.md) | [/playground/custom_container](https://modal.com/playground/custom_container) |
| 3 | Scale out horizontally | [scaling-out.md](scaling-out.md) | [/playground/scaling_out](https://modal.com/playground/scaling_out) |
| 4 | Run on GPUs | [gpu.md](gpu.md) | [/playground/gpu](https://modal.com/playground/gpu) |
| 5 | Run LLM inference | [inference.md](inference.md) | [/playground/inference](https://modal.com/playground/inference) |

## Tutorial Progression

1. **Run your first function** -- Create a Modal App and run a simple Python function in the cloud.
2. **Customize your container** -- Add dependencies (like numpy) to your container image using `pip_install`.
3. **Scale out horizontally** -- Use `.map` to process 100 inputs in parallel across multiple containers.
4. **Run on GPUs** -- Attach GPUs to your functions using CUDA images and `gpu="A10G"`.
5. **Run LLM inference** -- Run LLM inference on H100 GPUs using the transformers library.

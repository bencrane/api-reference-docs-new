# Dynamic batching
Modal’s `@batched` feature allows you to accumulate requests
and process them in dynamically-sized batches, rather than one-by-one. Batching increases throughput at a potential cost to latency.
Batched requests can share resources and reuse work, reducing the time and cost per request.
Batching is particularly useful for GPU-accelerated machine learning workloads,
as GPUs are designed to maximize throughput and are frequently bottlenecked on shareable resources,
like weights stored in memory. Static batching can lead to unbounded latency, as the function waits for a fixed number of requests to arrive.
Modal’s dynamic batching waits for the lesser of a fixed time *or* a fixed number of requests before executing,
maximizing the throughput benefit of batching while minimizing the latency penalty. 
## Enable dynamic batching with @batched
To enable dynamic batching, apply the [@modal.batched decorator](https://modal.com/docs/reference/modal.batched) to the target
Python function. Then, wrap it in `@app.function()` and run it on Modal,
and the inputs will be accumulated and processed in batches. Here’s what that looks like: When you invoke a function decorated with `@batched`, you invoke it asynchronously on individual inputs.
Outputs are returned where they were invoked. For instance, the code below invokes the decorated `batch_add` function above three times, but `batch_add` only executes twice: The first time it is executed with `xs` batched to `[1, 2]` and `ys` batched to `[300, 200]`. After about a one second delay, it is executed with `xs` batched to `[3]` and `ys` batched to `[100]`.
The result is an iterator that yields `301`, `202`, and `101`. 
## Use @batched with functions that take and return lists
For a Python function to be compatible with `@modal.batched`, it must adhere to
the following rules: The inputs to the function must be lists.** In the example above, we pass `xs` and `ys`, which are both lists of `int`s.
- **The function must return a list**. In the example above, the function returns
a list of sums.
- **The lengths of all the input lists and the output list must be the same.** In the example above, if `L == len(xs) == len(ys)`, then `L == len(batch_add(xs, ys))`.

## Modal Cls methods are compatible with dynamic batching

Methods on Modal [Cls](https://modal.com/docs/guide/lifecycle-functions)es also support dynamic batching.

One additional rule applies to classes with Batched Methods:
- If a class has a Batched Method, it **cannot have other Batched Methods or [Methods](https://modal.com/docs/reference/modal.method#modalmethod)**.

## Configure the wait time and batch size of dynamic batches

The `@batched` decorator takes in two required configuration parameters:
- `max_batch_size` limits the number of inputs combined into a single batch.
- `wait_ms` limits the amount of time the Function waits for more inputs after
the first input is received.

The first invocation of the Batched Function initiates a new batch, and subsequent
calls add requests to this ongoing batch. If `max_batch_size` is reached,
the batch immediately executes. If the `max_batch_size` is not met but `wait_ms` has passed since the first request was added to the batch, the unfilled batch is
executed.

### Selecting a batch configuration

To optimize the batching configurations for your application, consider the following heuristics:
- Set `max_batch_size` to the largest value your function can handle, so you
can amortize and parallelize as much work as possible.
- Set `wait_ms` to the difference between your targeted latency and the execution time. Most applications
have a targeted latency, and this allows the latency of any request to stay
within that limit.

## Serve web endpoints with dynamic batching

Here’s a simple example of serving a Function that batches requests dynamically
with a [@modal.fastapi_endpoint](https://modal.com/docs/guide/webhooks). Run [modal serve](https://modal.com/docs/reference/cli/serve), submit requests to the endpoint,
and the Function will batch your requests on the fly.

Now, you can submit requests to the web endpoint and process them in batches. For instance, the three requests
in the following example, which might be requests from concurrent clients in a real deployment,
will be batched into two executions:

# modal.FunctionCall

Source: https://modal.com/docs/reference/modal.FunctionCall

---

```python
modal.FunctionCall
class FunctionCall(typing.Generic, modal.object.Object)
```

A reference to an executed function call.

Constructed using .spawn(...) on a Modal function with the same arguments that a function normally takes. Acts as a reference to an ongoing function call that can be passed around and used to poll or fetch function results at some later time.

Conceptually similar to a Future/Promise/AsyncResult in other contexts and languages.

hydrate
```python
def hydrate(self, client: Optional[_Client] = None) -> Self:
```

Synchronize the local object with its identity on the Modal server.

It is rarely necessary to call this method explicitly, as most operations will lazily hydrate when needed. The main use case is when you need to access object metadata, such as its ID.

Added in v0.72.39: This method replaces the deprecated .resolve() method.

num_inputs
@live_method
```python
def num_inputs(self) -> int:
```

Get the number of inputs in the function call.

get
@live_method
```python
def get(self, timeout: Optional[float] = None, *, index: int = 0) -> ReturnType:
```

Get the result of the index-th input of the function call. .spawn() calls have a single output, so only specifying index=0 is valid. A non-zero index is useful when your function has multiple outputs, like via .spawn_map().

This function waits indefinitely by default. It takes an optional timeout argument that specifies the maximum number of seconds to wait, which can be set to 0 to poll for an output immediately.

The returned coroutine is not cancellation-safe.

iter
@live_method_gen
```python
def iter(self, *, start: int = 0, end: Optional[int] = None) -> Iterator[ReturnType]:
```

Iterate in-order over the results of the function call.

Optionally, specify a range [start, end) to iterate over.

Example:

```python
@app.function()
def my_func(a):
    return a ** 2

@app.local_entrypoint()
def main():
    fc = my_func.spawn_map([1, 2, 3, 4])
    assert list(fc.iter()) == [1, 4, 9, 16]
    assert list(fc.iter(start=1, end=3)) == [4, 9]
```

If end is not provided, it will iterate over all results.

get_call_graph
@live_method
```python
def get_call_graph(self) -> list[InputInfo]:
```

Returns a structure representing the call graph from a given root call ID, along with the status of execution for each node.

See modal.call_graph reference page for documentation on the structure of the returned InputInfo items.

cancel
@live_method
```python
def cancel(
    self,
    # if true, containers running the inputs are forcibly terminated
    terminate_containers: bool = False,
):
```

Cancels the function call, which will stop its execution and mark its inputs as TERMINATED.

If terminate_containers=True - the containers running the cancelled inputs are all terminated causing any non-cancelled inputs on those containers to be rescheduled in new containers.

from_id
@deprecate_aio_usage((2025, 11, 14), "FunctionCall.from_id")
@classmethod
```python
def from_id(
    cls, function_call_id: str, client: Optional["modal.client.Client"] = None
) -> "modal.functions.FunctionCall[Any]":
```

Instantiate a FunctionCall object from an existing ID.

Examples:

```python
# Spawn a FunctionCall and keep track of its object ID
fc = my_func.spawn()
fc_id = fc.object_id

# Later, use the ID to re-instantiate the FunctionCall object
fc = FunctionCall.from_id(fc_id)
result = fc.get()
```

Note that it’s only necessary to re-instantiate the FunctionCall with this method if you no longer have access to the original object returned from Function.spawn.

gather
@staticmethod
```python
def gather(*function_calls: "_FunctionCall[T]") -> typing.Sequence[T]:
```

Wait until all Modal FunctionCall objects have results before returning.

Accepts a variable number of FunctionCall objects, as returned by Function.spawn().

Returns a list of results from each FunctionCall, or raises an exception from the first failing function call.

Examples:

fc1 = slow_func_1.spawn()
fc2 = slow_func_2.spawn()

result_1, result_2 = modal.FunctionCall.gather(fc1, fc2)

Added in v0.73.69: This method replaces the deprecated modal.functions.gather function.

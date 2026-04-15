# Running commands in Sandboxes
Once you have created a Sandbox, you can run commands inside it using the [Sandbox.exec](https://modal.com/docs/reference/modal.Sandbox#exec) method.

`Sandbox.exec` returns a [ContainerProcess](https://modal.com/docs/reference/modal.container_process#modalcontainer_processcontainerprocess) object, which allows access to the process’s `stdout`, `stderr`, and `stdin`.
The `timeout` parameter ensures that the `exec` command will run for at most `timeout` seconds.

## Input

The Sandbox and ContainerProcess `stdin` handles are [StreamWriter](https://modal.com/docs/reference/modal.io_streams#modalio_streamsstreamwriter) objects. This object supports flushing writes with both synchronous and asynchronous APIs:

## Output

The Sandbox and ContainerProcess `stdout` and `stderr` handles are [StreamReader](https://modal.com/docs/reference/modal.io_streams#modalio_streamsstreamreader) objects. These objects support reading from the stream in both synchronous and asynchronous manners.
These handles also respect the timeout given to `Sandbox.exec`.

To read from a stream after the underlying process has finished, you can use the `read` method, which blocks until the process finishes and returns the entire output stream.

To stream output, take advantage of the fact that `stdout` and `stderr` are
iterable:

### Stream types

By default, all streams are buffered in memory, waiting to be consumed by the
client. You can control this behavior with the `stdout` and `stderr` parameters.
These parameters are conceptually similar to the `stdout` and `stderr` parameters of the [subprocess](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL) module.

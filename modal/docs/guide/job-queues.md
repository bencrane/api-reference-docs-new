# Job processing
Modal can be used as a scalable job queue to handle asynchronous tasks submitted
from a web app or any other Python application. This allows you to offload up to 1 million
long-running or resource-intensive tasks to Modal, while your main application
remains responsive. 
## Creating jobs with .spawn()
The basic pattern for using Modal as a job queue involves three key steps: Defining and deploying the job processing function using `modal deploy`.
- Submitting a job using [modal.Function.spawn()](https://modal.com/docs/reference/modal.Function#spawn)
- Polling for the job’s result using [modal.FunctionCall.get()](https://modal.com/docs/reference/modal.FunctionCall#get)

Here’s a simple example that you can run with `modal run my_job_queue.py`:

In this example:
- `process_job` is the Modal function that performs the actual job processing.
To deploy the `process_job` function on Modal, run `modal deploy my_job_queue.py`.
- `submit_job` submits a new job by first looking up the deployed `process_job` function, then calling `.spawn()` with the job data. It returns the unique ID
of the spawned function call.
- `get_job_result` attempts to retrieve the result of a previously submitted job
using [FunctionCall.from_id()](https://modal.com/docs/reference/modal.FunctionCall#from_id) and [FunctionCall.get()](https://modal.com/docs/reference/modal.FunctionCall#get). [FunctionCall.get()](https://modal.com/docs/reference/modal.FunctionCall#get) waits indefinitely
by default. It takes an optional timeout argument that specifies the maximum
number of seconds to wait, which can be set to 0 to poll for an output
immediately. Here, if the job hasn’t completed yet, we return a pending
response.
- The results of a `.spawn()` are accessible via `FunctionCall.get()` for up to
7 days after completion. After this period, we return an expired response.

[Document OCR Web App](https://modal.com/docs/examples/doc_ocr_webapp) is an example that uses
this pattern.

## Integration with web frameworks

You can easily integrate the job queue pattern with web frameworks like FastAPI.
Here’s an example, assuming that you have already deployed `process_job` on
Modal with `modal deploy` as above. This example won’t work if you haven’t
deployed your app yet.

In this example:
- The `/submit` endpoint accepts job data, submits a new job using `await process_job.spawn.aio()`, and returns the job’s ID to the client.
- The `/result/{call_id}` endpoint allows the client to poll for the job’s
result using the job ID. If the job hasn’t completed yet, it returns a 202
status code to indicate that the job is still being processed. If the job
has expired, it returns a 404 status code to indicate that the job is not found.

You can try this app by serving it with `modal serve`:

Then interact with its endpoints with `curl`:

## Scaling and reliability

Modal automatically scales the job queue based on the workload, spinning up new
instances as needed to process jobs concurrently. It also provides built-in
reliability features like automatic retries and timeout handling.

You can customize the behavior of the job queue by configuring the `@app.function()` decorator with options like [retries](https://modal.com/docs/guide/retries#function-retries), [timeout](https://modal.com/docs/guide/timeouts#timeouts), and [max_containers](https://modal.com/docs/guide/scale#configuring-autoscaling-behavior).

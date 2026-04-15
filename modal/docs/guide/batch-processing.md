# Batch Processing
Modal is optimized for large-scale batch processing, allowing functions to scale to thousands of parallel containers with zero additional configuration. Function calls can be submitted asynchronously for background execution, eliminating the need to wait for jobs to finish or tune resource allocation.

This guide covers Modal’s batch processing capabilities, from basic invocation to integration with existing pipelines.

## Background Execution with .spawn_map

The fastest way to submit multiple jobs for asynchronous processing is by invoking a function with `.spawn_map`. When combined with the [--detach](https://modal.com/docs/reference/cli/run) flag, your App continues running until all jobs are completed.

Here’s an example of submitting 100,000 videos for parallel embedding. You can disconnect after submission, and the processing will continue to completion in the background:

This pattern works best for jobs that store results externally—for example, in a [Modal Volume](https://modal.com/docs/guide/volumes), [Cloud Bucket Mount](https://modal.com/docs/guide/cloud-bucket-mounts), or your own database*.

** For database connections, consider using [Modal Proxy](https://modal.com/docs/guide/proxy-ips) to maintain a static IP across thousands of containers.*

## Parallel Processing with .map

Using `.map` allows you to offload expensive computations to powerful machines while gathering results. This is particularly useful for pipeline steps with bursty resource demands. Modal handles all infrastructure provisioning and de-provisioning automatically.

Here’s how to implement parallel video similarity queries as a single Modal function call:

This example runs `compute_video_similarity` on an autoscaling pool of L40S GPUs, returning scores to a local process for further processing.

## Integration with Existing Systems

The recommended way to use Modal Functions within your existing data pipeline is through [deployed function invocation](https://modal.com/docs/guide/trigger-deployed-functions). After deployment, you can call Modal functions from external systems:

You can invoke Modal Functions from any Python context, gaining access to built-in observability, resource management, and GPU acceleration.

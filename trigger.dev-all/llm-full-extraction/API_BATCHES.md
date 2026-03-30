> Sources:
> - https://trigger.dev/docs/management/batches/create
> - https://trigger.dev/docs/management/batches/retrieve
> - https://trigger.dev/docs/management/batches/retrieve-results
> - https://trigger.dev/docs/management/batches/stream-items

# Batches API

## Create batch

openapi POST /api/v3/batches
Phase 1 of 2-phase batch API. Creates a batch record and optionally blocks the parent run for batchTriggerAndWait.
After creating a batch, stream items via POST /api/v3/batches/{batchId}/items.

---

## Retrieve a batch

v3-openapi GET /api/v1/batches/{batchId}
Retrieve a batch by its ID, including its status and the IDs of all runs in the batch.

---

## Retrieve batch results

v3-openapi GET /api/v1/batches/{batchId}/results
Returns the execution results of all completed runs in a batch. Only finished runs (successful or failed) are included in the items array — runs that are still executing are omitted. Returns 404 if the batch doesn't exist.

---

## Stream batch items

openapi POST /api/v3/batches/{batchId}/items
Phase 2 of 2-phase batch API. Accepts an NDJSON stream of batch items and enqueues them.
Each line in the body should be a valid BatchItemNDJSON object.
The stream is processed with backpressure - items are enqueued as they arrive.
The batch is sealed when the stream completes successfully.

---

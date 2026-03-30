> Sources:
> - https://trigger.dev/docs/management/queues/list
> - https://trigger.dev/docs/management/queues/retrieve
> - https://trigger.dev/docs/management/queues/pause
> - https://trigger.dev/docs/management/queues/concurrency-override
> - https://trigger.dev/docs/management/queues/concurrency-reset

# Queues API

## List Queues

v3-openapi GET /api/v1/queues
List all queues in your environment with pagination support.

---

## Retrieve Queue

v3-openapi GET /api/v1/queues/{queueParam}
Get a queue by its ID, or by type and name.

---

## Pause or Resume Queue

v3-openapi POST /api/v1/queues/{queueParam}/pause
Pause a queue to prevent new runs from starting, or resume a paused queue. Runs that are currently executing will continue to completion.

---

## Override Concurrency Limit

v3-openapi POST /api/v1/queues/{queueParam}/concurrency/override
Override the concurrency limit of a queue. This is useful for temporarily scaling up or down based on demand.

---

## Reset Concurrency Limit

v3-openapi POST /api/v1/queues/{queueParam}/concurrency/reset
Reset the concurrency limit of a queue back to its base value defined in code.

---

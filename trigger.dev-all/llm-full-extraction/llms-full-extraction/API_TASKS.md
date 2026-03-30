> Sources:
> - https://trigger.dev/docs/management/tasks/trigger
> - https://trigger.dev/docs/management/tasks/batch-trigger
> - https://trigger.dev/docs/management/tasks/trigger-batch

# Tasks API

## Trigger

v3-openapi POST /api/v1/tasks/{taskIdentifier}/trigger
Trigger a task by its identifier.

---

## Batch trigger

v3-openapi POST /api/v1/tasks/batch
Batch trigger tasks with up to 1,000 payloads with SDK 4.3.1+ (500 in prior versions).

---

## Trigger task batch

v3-openapi POST /api/v1/tasks/{taskIdentifier}/batch
Batch trigger a specific task with up to 1,000 payloads. All items in the batch run the same task.

---

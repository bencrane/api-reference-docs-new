> Sources:
> - https://trigger.dev/docs/management/runs/list
> - https://trigger.dev/docs/management/runs/retrieve
> - https://trigger.dev/docs/management/runs/replay
> - https://trigger.dev/docs/management/runs/cancel
> - https://trigger.dev/docs/management/runs/reschedule
> - https://trigger.dev/docs/management/runs/update-metadata
> - https://trigger.dev/docs/management/runs/add-tags
> - https://trigger.dev/docs/management/runs/retrieve-events
> - https://trigger.dev/docs/management/runs/retrieve-trace
> - https://trigger.dev/docs/management/runs/retrieve-result

# Runs API

## List runs

v3-openapi GET /api/v1/runs
List runs in a specific environment. You can filter the runs by status, created at, task identifier, version, and more.

---

## Retrieve run

v3-openapi GET /api/v3/runs/{runId}
Retrieve information about a run, including its status, payload, output, and attempts. If you authenticate with a Public API key, we will omit the payload and output fields for security reasons.

---

## Replay run

v3-openapi POST /api/v1/runs/{runId}/replay
Creates a new run with the same payload and options as the original run.

---

## Cancel run

v3-openapi POST /api/v2/runs/{runId}/cancel
Cancels an in-progress run. If the run is already completed, this will have no effect.

---

## Reschedule run

v3-openapi POST /api/v1/runs/{runId}/reschedule
Updates a delayed run with a new delay. Only valid when the run is in the DELAYED state.

---

## Update metadata

v3-openapi PUT /api/v1/runs/{runId}/metadata
Update the metadata of a run.

---

## Add tags to a run

v3-openapi POST /api/v1/runs/{runId}/tags
Adds one or more tags to a run. Runs can have a maximum of 10 tags. Duplicate tags are ignored.

---

## Retrieve run events

v3-openapi GET /api/v1/runs/{runId}/events
Returns all OTel span events for a run. Useful for debugging and observability.

---

## Retrieve run trace

v3-openapi GET /api/v1/runs/{runId}/trace
Returns the full OTel trace tree for a run, including all spans and their children.

---

## Retrieve run result

v3-openapi GET /api/v1/runs/{runId}/result
Returns the execution result of a completed run. Returns 404 if the run doesn't exist or hasn't finished yet.

---

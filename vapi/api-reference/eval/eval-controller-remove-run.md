# Delete Eval Run API Reference

## Endpoint

**Method:** `DELETE`

**URL:** `https://api.vapi.ai/eval/run/{id}`

## Description

This endpoint removes an evaluation run from the system. When you delete an eval run, it's permanently removed and can no longer be accessed or referenced.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the eval run to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200 OK)

The endpoint returns the deleted `EvalRun` object with the following structure:

```json
{
  "id": "string",
  "status": "running|ended|queued",
  "endedReason": "mockConversation.done|error|timeout|cancelled|aborted"
}
```

### Status Values

- **running** - Eval run is currently executing
- **ended** - Eval run has completed
- **queued** - Eval run is waiting to start

### Ended Reason Values

- **mockConversation.done** - Completed normally
- **error** - Failed due to Chat error or configuration issues
- **timeout** - Exceeded time limit
- **cancelled** - User cancelled the run
- **aborted** - Vapi cancelled the run

## Example Request

```bash
curl -X DELETE https://api.vapi.ai/eval/run/eval_run_123 \
  -H "Authorization: your-api-key"
```

## Example Response

```json
{
  "id": "eval_run_123",
  "status": "ended",
  "endedReason": "mockConversation.done"
}
```

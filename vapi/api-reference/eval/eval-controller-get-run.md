# Get Eval Run - API Reference

## Endpoint

**GET** `https://api.vapi.ai/eval/run/{id}`

Retrieves details about a specific evaluation run by its ID.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the eval run |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200)

Returns an `EvalRun` object containing evaluation run details.

#### EvalRun Schema Properties

| Property | Type | Description |
|----------|------|-------------|
| `status` | EvalRunStatus | Current state: `running`, `ended`, or `queued` |
| `endedReason` | EvalRunEndedReason | Reason for completion: `mockConversation.done`, `error`, `timeout`, `cancelled`, or `aborted` |

### Status Values

- **running**: Eval actively processing
- **ended**: Eval completed
- **queued**: Awaiting execution

### Ended Reason Values

- **mockConversation.done**: Finished normally
- **error**: Failed due to Chat error or misconfiguration
- **timeout**: Exceeded time limits
- **cancelled**: User-initiated termination
- **aborted**: Vapi-initiated termination

## Example Request

```bash
curl -X GET "https://api.vapi.ai/eval/run/your-eval-id" \
  -H "Authorization: your-api-key"
```

## Example Response

```json
{
  "id": "eval-run-12345",
  "status": "ended",
  "endedReason": "mockConversation.done"
}
```

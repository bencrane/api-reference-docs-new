# Delete Campaign API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/campaign/{id}`

## Description

Removes a campaign from the system. This operation permanently deletes the specified campaign and returns the deleted campaign object.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the campaign to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)" |

## Response

### Success Response (200)

**Content-Type:** `application/json`

**Schema:** Campaign object

The response returns the complete Campaign object that was deleted, including:

- `id`: Campaign identifier
- `status`: Current status (scheduled, in-progress, or ended)
- `endedReason`: Explanation for how campaign ended (if applicable)
- All other campaign configuration details

### Campaign Status Values

- `scheduled`: Campaign is awaiting execution
- `in-progress`: Campaign is currently running
- `ended`: Campaign has completed

### Campaign End Reasons

- `campaign.scheduled.ended-by-user`: User terminated scheduled campaign
- `campaign.in-progress.ended-by-user`: User terminated active campaign
- `campaign.ended.success`: Campaign completed successfully

## Example Request

```bash
curl -X DELETE https://api.vapi.ai/campaign/campaign_12345 \
  -H "Authorization: your_api_key_here"
```

## Notes

- The deletion is permanent and cannot be undone
- Ensure you have the correct campaign ID before executing
- Authentication via API key is required for this operation

# POST GetLeadsFromCampaign

**Endpoint:** `https://api.heyreach.io/api/public/campaign/GetLeadsFromCampaign`

Gets the leads that are in a campaign.

This request corresponds to the "Lead Analytics" screen in the UI. Remark: It shows only the "Pending" leads that are about to start executing actions in the campaign. There might be more "Pending" leads from the specified lead list, that the system will insert later for execution.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `campaignId` | integer | The ID of the campaign |
| `offset` | integer | The number of records to skip (for pagination) |
| `limit` | integer | The maximum number of records to return |
| `timeFrom` | string (ISO 8601) | The start of the time range for filtering |
| `timeTo` | string (ISO 8601) | The end of the time range for filtering |
| `timeFilter` | string | Defines the time filter for fetching leads. See values below |

### timeFilter Values

| Value | Description |
|-------|-------------|
| `CreationTime` | Filters leads by their creation time |
| `Everywhere` | No specific time filtering is applied (default behavior if omitted) |
| `LastActionTakenTime` | Filters leads that executed an action within the given time range |
| `FailedTime` | Filters leads that failed within the given time range |
| `LastActionTakenOrFailedTime` | Filters leads that executed an action OR failed within the given time range |

## Response Enums

### LeadCampaignStatus

- `Pending`
- `InSequence`
- `Finished`
- `Paused`
- `Failed`

### LeadConnectionStatus

- `None`
- `ConnectionSent`
- `ConnectionAccepted`

### LeadMessageStatus

- `None`
- `MessageSent`
- `MessageReply`

### LeadStatusMessage (string)

Usually `null`, but if the lead is in `Failed` status, this shows the reason why the lead failed.

## Body (raw JSON)

```json
{
  "campaignId": 1805,
  "offset": 0,
  "limit": 100,
  "timeFrom": "2024-10-06T17:34:00+02:00",
  "timeTo": "2024-10-07T17:36:00+02:00",
  "timeFilter": "CreationTime"
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/campaign/GetLeadsFromCampaign' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "campaignId": 1805,
  "offset": 0,
  "limit": 100,
  "timeFrom": "2024-10-06T17:34:00+02:00",
  "timeTo": "2024-10-07T17:36:00+02:00",
  "timeFilter": "CreationTime"
}'
```

## Example Response

```json
{
  "totalCount": 152,
  "items": [
    {
      "id": 62658,
      "linkedInUserProfileId": "AC9sANasasasX0Ia-q6DQxyS35UD7a8716G5c8",
      "linkedInUserProfile": {
        "linkedin_id": "58344979",
        "profileUrl": "https://www.linkedin.com/in/johndoe",
        "firstName": "John",
        "lastName": "Doe",
        "headline": "Communications and Marketing Professional",
        "imageUrl": "https://media.licdn.com/dms/image/v2/D4E03AQH0WJHn5rNRpA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1671ss497?e=173ss&",
        "location": "Princetown",
        "companyName": "ACME",
        "companyUrl": null,
        "position": "",
        "about": null,
        "connections": 0,
        "followers": 0,
        "emailAddress": null
      },
      "lastActionTime": "2024-10-01T03:28:22.414791Z",
      "failedTime": null,
      "creationTime": "2024-09-30T21:28:06.933349Z",
      "leadCampaignStatus": "Finished",
      "leadConnectionStatus": "None",
      "leadMessageStatus": "None",
      "errorCode": null,
      "leadCampaignStatusMessage": null,
      "linkedInSenderId": 1108,
      "linkedInSenderFullName": "Jane Doe"
    }
  ]
}
```
# Get Project Usage
Source: https://developers.deepgram.com/reference/manage/usage/get

**Note: This endpoint is deprecated. Use Get Project Usage Breakdown for a more comprehensive usage summary.**

## Endpoint

GET https://api.deepgram.com/v1/projects/:project_id/usage

## Description

Retrieves the usage for a specific project. Use Get Project Usage Breakdown for a more comprehensive usage summary.

## Authentication

Authorization Token
Use Authorization: Token <API_KEY>
Example: Authorization: Token 12345abcdef

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start | string (date) | Optional | Start date of the requested date range. Format accepted is YYYY-MM-DD |
| end | string (date) | Optional | End date of the requested date range. Format accepted is YYYY-MM-DD |
| accessor | string | Optional | Filter for requests where a specific accessor was used |
| alternatives | boolean | Optional | Filter for requests where alternatives were used |
| callback_method | boolean | Optional | Filter for requests where callback method was used |
| callback | boolean | Optional | Filter for requests where callback was used |
| channels | boolean | Optional | Filter for requests where channels were used |
| custom_intent_mode | boolean | Optional | Filter for requests where custom intent mode was used |
| custom_intent | boolean | Optional | Filter for requests where custom intent was used |
| custom_topic_mode | boolean | Optional | Filter for requests where custom topic mode was used |
| custom_topic | boolean | Optional | Filter for requests where custom topic was used |
| deployment | enum | Optional | Filter for requests where a specific deployment was used. Allowed values: hosted, beta, self-hosted |
| detect_entities | boolean | Optional | Filter for requests where detect entities was used |
| detect_language | boolean | Optional | Filter for requests where detect language was used |
| diarize | boolean | Optional | Filter for requests where diarize was used |
| dictation | boolean | Optional | Filter for requests where dictation was used |
| encoding | boolean | Optional | Filter for requests where encoding was used |
| endpoint | enum | Optional | Filter for requests where a specific endpoint was used. Allowed values: listen, read, speak, agent |
| extra | boolean | Optional | Filter for requests where extra was used |
| filler_words | boolean | Optional | Filter for requests where filler words was used |
| intents | boolean | Optional | Filter for requests where intents was used |
| keyterm | boolean | Optional | Filter for requests where keyterm was used |
| keywords | boolean | Optional | Filter for requests where keywords was used |
| language | boolean | Optional | Filter for requests where language was used |
| measurements | boolean | Optional | Filter for requests where measurements were used |
| method | enum | Optional | Filter for requests where a specific method was used. Allowed values: sync, async, streaming |
| model | string | Optional | Filter for requests where a specific model uuid was used |
| multichannel | boolean | Optional | Filter for requests where multichannel was used |
| numerals | boolean | Optional | Filter for requests where numerals were used |
| paragraphs | boolean | Optional | Filter for requests where paragraphs were used |
| profanity_filter | boolean | Optional | Filter for requests where profanity filter was used |
| punctuate | boolean | Optional | Filter for requests where punctuate was used |
| redact | boolean | Optional | Filter for requests where redact was used |
| replace | boolean | Optional | Filter for requests where replace was used |
| sample_rate | boolean | Optional | Filter for requests where sample rate was used |
| search | boolean | Optional | Filter for requests where search was used |
| sentiment | boolean | Optional | Filter for requests where sentiment was used |
| smart_format | boolean | Optional | Filter for requests where smart format was used |
| summarize | boolean | Optional | Filter for requests where summarize was used |
| tag | string | Optional | Filter for requests where a specific tag was used |
| topics | boolean | Optional | Filter for requests where topics was used |
| utt_split | boolean | Optional | Filter for requests where utt split was used |
| utterances | boolean | Optional | Filter for requests where utterances was used |
| version | boolean | Optional | Filter for requests where version was used |

## Response

A specific request for a specific project

| Field | Type | Description |
|-------|------|-------------|
| start | string (date) | |
| end | string (date) | |
| resolution | object | See properties below |

**resolution** object properties:
- **units** (string)
- **amount** (integer)

### Example Response (200 Retrieved)

```json
{
  "start": "2024-10-16",
  "end": "2024-10-23",
  "resolution": {
    "units": "day",
    "amount": 1
  }
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/usage"

querystring = {
    "accessor": "12345678-1234-1234-1234-123456789012",
    "alternatives": "true",
    "callback_method": "true",
    "callback": "true",
    "channels": "true",
    "deployment": "hosted",
    "endpoint": "listen",
    "method": "async",
    "model": "6f548761-c9c0-429a-9315-11a1d28499c8",
    "tag": "tag1"
}

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

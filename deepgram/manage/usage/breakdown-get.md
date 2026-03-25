# Get Project Usage Breakdown
Source: https://developers.deepgram.com/reference/manage/usage/breakdown/get

## Endpoint

GET https://api.deepgram.com/v1/projects/:project_id/usage/breakdown

## Description

Retrieves the usage breakdown for a specific project, with various filter options by API feature or by groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND logic.

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
| grouping | enum | Optional | Common usage grouping parameters (7 enum values) |
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

Usage breakdown response

| Field | Type | Description |
|-------|------|-------------|
| start | string (date) | Start date of the usage period |
| end | string (date) | End date of the usage period |
| resolution | object | See properties below |
| results | list of objects | See properties below |

**resolution** object properties:
- **units** (string)
- **amount** (integer)

**results** object properties:
- **hours** (double)
- **total_hours** (double)
- **agent_hours** (double)
- **tokens_in** (integer)
- **tokens_out** (integer)
- **tts_characters** (integer)
- **requests** (integer)
- **grouping** (object)

**grouping** object properties:
- **start** (string)
- **end** (string)
- **accessor** (string)
- **endpoint** (string)
- **feature_set** (string)
- **models** (list of strings)
- **method** (string)
- **tags** (string)
- **deployment** (string)

### Example Response (200 Retrieved)

```json
{
  "start": "2025-01-16",
  "end": "2025-01-23",
  "resolution": {
    "units": "day",
    "amount": 1
  },
  "results": [
    {
      "hours": 1619.7242069444444,
      "total_hours": 1621.7395791666668,
      "agent_hours": 41.33564388888889,
      "tokens_in": 0,
      "tokens_out": 0,
      "tts_characters": 9158866,
      "requests": 373381,
      "grouping": {
        "start": "2025-01-16",
        "end": "2025-01-16",
        "accessor": "123456789012345678901234",
        "endpoint": "listen",
        "feature_set": "punctuate",
        "models": [
          "Nova-2"
        ],
        "method": "async",
        "tags": "tag1",
        "deployment": "self-hosted"
      }
    }
  ]
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/usage/breakdown"

querystring = {
    "accessor": "12345678-1234-1234-1234-123456789012",
    "alternatives": "true",
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

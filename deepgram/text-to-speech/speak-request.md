# Single Text Request (Text-to-Speech REST API)
Source: https://developers.deepgram.com/reference/text-to-speech/speak-request

Convert text into natural-sounding speech using Deepgram's TTS REST API

## Endpoint

**POST** `https://api.deepgram.com/v1/speak`

## Authentication

### Authorization Token
Use `Authorization: Token <API_KEY>`
Example: `Authorization: Token 12345abcdef`

### Authorization Bearer
Use `Authorization: Bearer <JWT>`
Example: `Authorization: Bearer eyJhbGciOiJ...`

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| callback | string | Optional | | URL to which we'll make the callback request |
| callback_method | enum | Optional | POST | HTTP method by which the callback request will be made. Allowed values: POST, PUT |
| mip_opt_out | boolean | Optional | false | Opts out requests from the Deepgram Model Improvement Program. Refer to Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip |
| tag | string or list of strings | Optional | | Label your requests for the purpose of identification during usage reporting |
| bit_rate | enum or double | Optional | | The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type. (3 variants) |
| container | enum | Optional | | Container specifies the file format wrapper for the output audio. The available options depend on the encoding type. (5 variants) |
| encoding | enum | Optional | | Encoding allows you to specify the expected encoding of your audio output (7 variants) |
| model | enum | Optional | aura-asteria-en | AI model used to process submitted text (63 enum values) |
| sample_rate | enum | Optional | | Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable (5 variants) |

## Request Body

Transform text to speech.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| text | string | Required | The text content to be converted to speech |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/speak"

querystring = {"model": "aura-2-thalia-en"}

payload = { "text": "Hello, welcome to Deepgram!" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

## Response

### 200 Successful

Successful text-to-speech transformation.

## Errors

| Status | Description |
|--------|-------------|
| 400 | Bad Request Error |

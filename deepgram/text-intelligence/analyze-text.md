# Analyze Text (Text Intelligence API)
Source: https://developers.deepgram.com/reference/text-intelligence/analyze-text

Analyze text content using Deepgram's text analysis API

## Endpoint

**POST** `https://api.deepgram.com/v1/read`

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
| sentiment | boolean | Optional | false | Recognizes the sentiment throughout a transcript or text |
| summarize | enum or boolean | Optional | | Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only. |
| tag | string or list of strings | Optional | | Label your requests for the purpose of identification during usage reporting |
| topics | boolean | Optional | false | Detect topics throughout a transcript or text |
| custom_topic | string or list of strings | Optional | | Custom topics you want the model to detect within your input audio or text if present. Submit up to 100. |
| custom_topic_mode | enum | Optional | extended | Sets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param. Allowed values: extended, strict |
| intents | boolean | Optional | false | Recognizes speaker intent throughout a transcript or text |
| custom_intent | string or list of strings | Optional | | Custom intents you want the model to detect within your input audio if present |
| custom_intent_mode | enum | Optional | extended | Sets how the model will interpret intents submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in the custom_intent param. Allowed values: extended, strict |
| language | string | Optional | en | The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available |

## Request Body

Analyze a text file. Accepts one of:

- An object with a `url` property (string, format: uri)
- An object with a `text` property (string)

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/read"

payload = { "url": "https://example.com/audio/interview.mp3" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

## Response

### 200 Successful

```json
{
  "metadata": {
    "metadata": {
      "request_id": "d04af392-db11-4c1d-83e1-20e34f0b8999",
      "created": "2024-11-18T23:47:44.674Z",
      "language": "en",
      "summary_info": {
        "model_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "input_tokens": 3500,
        "output_tokens": 150
      },
      "sentiment_info": {
        "model_uuid": "f1e2d3c4-b5a6-7890-cdef-1234567890ab",
        "input_tokens": 3500,
        "output_tokens": 150
      },
      "topics_info": {
        "model_uuid": "123e4567-e89b-12d3-a456-426614174000",
        "input_tokens": 3500,
        "output_tokens": 150
      },
      "intents_info": {
        "model_uuid": "0a1b2c3d-4e5f-6789-abcd-ef0123456789",
        "input_tokens": 3500,
        "output_tokens": 150
      }
    }
  },
  "results": {
    "summary": {
      "results": {
        "summary": {
          "text": "This transcript highlights the significance of honoring pioneering women in space exploration and the progress made towards equality."
        }
      }
    },
    "topics": {
      "results": {
        "topics": {
          "segments": [
            {
              "text": "And, um, I think if it signifies anything, it is, uh, to honor the the women who came before us who, um, were skilled and qualified, um, and didn't get the the same opportunities that we have today.",
              "start_word": 32,
              "end_word": 69,
              "topics": [
                {
                  "topic": "Women in Space",
                  "confidence_score": 0.91581345
                }
              ]
            }
          ]
        }
      }
    },
    "intents": {
      "results": {
        "intents": {
          "segments": [
            {
              "text": "If you found this valuable, you can subscribe to the show on spotify or your favorite podcast app.",
              "start_word": 354,
              "end_word": 414,
              "intents": [
                {
                  "intent": "Promote Subscription",
                  "confidence_score": 0.0038975573
                }
              ]
            }
          ]
        }
      }
    },
    "sentiments": {
      "segments": [
        {
          "text": "Yeah. As as much as, um, it's worth celebrating, uh, the first, uh, spacewalk, um, with an all-female team, I think many of us are looking forward to it just being normal. And, um, I think if it signifies anything, it is, uh, to honor the the women who came before us who, um, were skilled and qualified, um, and didn't get the the same opportunities that we have today.",
          "start_word": 0,
          "end_word": 69,
          "sentiment": "positive",
          "sentiment_score": 0.5810546875
        }
      ],
      "average": {
        "sentiment": "positive",
        "sentiment_score": 0.5810185185185185
      }
    }
  }
}
```

### Response Schema

- **metadata** (object): Contains request metadata including request_id, created timestamp, language, and info objects for summary, sentiment, topics, and intents (with model_uuid, input_tokens, output_tokens)
- **results** (object): Contains analysis results
  - **summary**: Summarized text content
  - **topics**: Detected topic segments with confidence scores
  - **intents**: Detected intent segments with confidence scores
  - **sentiments**: Sentiment analysis per segment and average sentiment

## Errors

| Status | Description |
|--------|-------------|
| 400 | Bad Request Error |

# Pre-Recorded Audio (Speech-to-Text REST API)
Source: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded

Transcribe audio and video using Deepgram's speech-to-text REST API

## Endpoint

**POST** `https://api.deepgram.com/v1/listen`

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
| extra | string or list of strings | Optional | | Arbitrary key-value pairs that are attached to the API response for usage in downstream processing |
| sentiment | boolean | Optional | false | Recognizes the sentiment throughout a transcript or text |
| summarize | enum or boolean | Optional | | Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only. |
| tag | string or list of strings | Optional | | Label your requests for the purpose of identification during usage reporting |
| topics | boolean | Optional | false | Detect topics throughout a transcript or text |
| custom_topic | string or list of strings | Optional | | Custom topics you want the model to detect within your input audio or text if present. Submit up to 100. |
| custom_topic_mode | enum | Optional | extended | Sets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param. Allowed values: extended, strict |
| intents | boolean | Optional | false | Recognizes speaker intent throughout a transcript or text |
| custom_intent | string or list of strings | Optional | | Custom intents you want the model to detect within your input audio if present |
| custom_intent_mode | enum | Optional | extended | Sets how the model will interpret intents submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in the custom_intent param. Allowed values: extended, strict |
| detect_entities | boolean | Optional | false | Identifies and extracts key entities from content in submitted audio |
| detect_language | boolean or list of strings | Optional | | Identifies the dominant language spoken in submitted audio |
| diarize | boolean | Optional | false | Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0 |
| dictation | boolean | Optional | false | Dictation mode for controlling formatting with dictated speech |
| encoding | enum | Optional | | Specify the expected encoding of your submitted audio (8 enum values) |
| filler_words | boolean | Optional | false | Filler Words can help transcribe interruptions in your audio, like "uh" and "um" |
| keyterm | list of strings | Optional | | Key term prompting can boost or suppress specialized terminology and brands. Only compatible with Nova-3 |
| keywords | string or list of strings | Optional | | Keywords can boost or suppress specialized terminology and brands |
| language | string | Optional | en | The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available |
| measurements | boolean | Optional | false | Spoken measurements will be converted to their corresponding abbreviations |
| model | enum or string | Optional | | AI model used to process submitted audio |
| multichannel | boolean | Optional | false | Transcribe each audio channel independently |
| numerals | boolean | Optional | false | Numerals converts numbers from written format to numerical format |
| paragraphs | boolean | Optional | false | Splits audio into paragraphs to improve transcript readability |
| profanity_filter | boolean | Optional | false | Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely |
| punctuate | boolean | Optional | false | Add punctuation and capitalization to the transcript |
| redact | string or list of enums | Optional | | Redaction removes sensitive information from your transcripts |
| replace | string or list of strings | Optional | | Search for terms or phrases in submitted audio and replaces them |
| search | string or list of strings | Optional | | Search for terms or phrases in submitted audio |
| smart_format | boolean | Optional | false | Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability |
| utterances | boolean | Optional | false | Segments speech into meaningful semantic units |
| utt_split | double | Optional | 0.8 | Seconds to wait before detecting a pause between words in submitted audio |
| version | enum or string | Optional | | Version of an AI model to use |
| mip_opt_out | boolean | Optional | false | Opts out requests from the Deepgram Model Improvement Program. Refer to Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip |

## Request Body

**Content-Type:** application/json

Transcribe an audio or video file.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| url | string | Required | format: "uri" |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/listen"

payload = { "url": "https://dpgr.am/spacewalk.wav" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

## Response

Returns either transcription results, or a request_id when using a callback.

### 200 Successful

```json
{
  "metadata": {
    "transaction_key": "deprecated",
    "request_id": "a847f427-4ad5-4d67-9b95-db801e58251c",
    "sha256": "154e291ecfa8be6ab8343560bcc109008fa7853eb5372533e8efdefc9b504c33",
    "created": "2024-05-12T18:57:13.426Z",
    "duration": 25.933313,
    "channels": 1,
    "models": [
      "30089e05-99d1-4376-b32e-c263170674af"
    ],
    "model_info": {
      "30089e05-99d1-4376-b32e-c263170674af": {
        "name": "2-general-nova",
        "version": "2024-01-09.29447",
        "arch": "nova-2"
      }
    },
    "summary_info": {
      "model_uuid": "67875a7f-c9c4-48a0-aa55-5bdb8a91c34a",
      "input_tokens": 95,
      "output_tokens": 63
    },
    "sentiment_info": {
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "input_tokens": 105,
      "output_tokens": 105
    },
    "topics_info": {
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "input_tokens": 105,
      "output_tokens": 7
    },
    "intents_info": {
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "input_tokens": 105,
      "output_tokens": 4
    },
    "tags": [
      "test"
    ]
  },
  "results": {
    "channels": [
      {
        "search": [
          {
            "query": "spacewalk",
            "hits": [
              {
                "confidence": 0.98,
                "start": 5.2,
                "end": 5.7,
                "snippet": "the first all-female spacewalk"
              }
            ]
          }
        ],
        "alternatives": [
          {
            "transcript": "This historic spacewalk marks a significant milestone for women in aerospace.",
            "confidence": 0.95,
            "words": [
              {
                "word": "historic",
                "start": 0.5,
                "end": 1,
                "confidence": 0.96
              },
              {
                "word": "spacewalk",
                "start": 4.8,
                "end": 5.5,
                "confidence": 0.97
              }
            ],
            "paragraphs": {
              "transcript": "This historic spacewalk marks a significant milestone for women in aerospace.",
              "paragraphs": [
                {
                  "sentences": [
                    {
                      "text": "This historic spacewalk marks a significant milestone for women in aerospace.",
                      "start": 0,
                      "end": 25.9
                    }
                  ],
                  "speaker": 1,
                  "num_words": 12,
                  "start": 0,
                  "end": 25.9
                }
              ]
            },
            "entities": [
              {
                "label": "Event",
                "value": "spacewalk",
                "raw_value": "spacewalk",
                "confidence": 0.98,
                "start_word": 2,
                "end_word": 3
              }
            ],
            "summaries": [
              {
                "summary": "The transcript highlights the importance of the first all-female spacewalk.",
                "start_word": 0,
                "end_word": 12
              }
            ],
            "topics": [
              {
                "text": "This historic spacewalk marks a significant milestone for women in aerospace.",
                "start_word": 0,
                "end_word": 12,
                "topics": [
                  "Space Exploration"
                ]
              }
            ]
          }
        ],
        "detected_language": "en"
      }
    ],
    "utterances": [
      {
        "start": 0,
        "end": 25.9,
        "confidence": 0.95,
        "channel": 1,
        "transcript": "This historic spacewalk marks a significant milestone for women in aerospace.",
        "words": [
          {
            "word": "historic",
            "start": 0.5,
            "end": 1,
            "confidence": 0.96,
            "speaker": 1,
            "speaker_confidence": 0.99,
            "punctuated_word": "historic"
          },
          {
            "word": "spacewalk",
            "start": 4.8,
            "end": 5.5,
            "confidence": 0.97,
            "speaker": 1,
            "speaker_confidence": 0.99,
            "punctuated_word": "spacewalk"
          }
        ],
        "speaker": 1,
        "id": "utt-0001"
      }
    ],
    "summary": {
      "result": "success",
      "short": "Speaker 0 discusses the significance of the first all-female spacewalk with an all-female team, stating that it is a tribute to the skilled and qualified women who were denied opportunities in the past."
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
                  "topic": "Spacewalk",
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
                  "intent": "Encourage podcasting",
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
          "text": "Yeah. As as much as, um, it's worth celebrating, uh, the first, uh, spacewalk, um, with an all-female team, I think many of us are looking forward to it just being normal.",
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

## Errors

| Status | Description |
|--------|-------------|
| 400 | Bad Request Error |

# API Rate Limits
Source: https://developers.deepgram.com/reference/api-rate-limits

Understand the different service limits of Deepgram's APIs.

## Pay as You Go

Limits to consider if you use the Pay as You Go plan with Deepgram.

### Voice Agent

| API | Connection Limits |
|-----|-------------------|
| Voice Agent API | Up to 45 concurrent connections |

### Speech to Text

If multiple services are used in one API call (e.g Speech to Text + Sentiment Analysis), the lower of the rate limits is applied.

| Model | Service Limit |
|-------|---------------|
| Flux | Streaming Up to 150 concurrent requests |
| Nova-3 | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 150 concurrent requests |
| Nova-2 | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 150 concurrent requests |
| Nova | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 150 concurrent requests |
| Enhanced | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 150 concurrent requests |
| Base | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 150 concurrent requests |
| Whisper Cloud | Pre-Recorded Up to 3 concurrent requests |

If you include Speaker Diarization features in requests to /listen, you will be subject to the service limits noted in the table below.

| Model | Service Limit |
|-------|---------------|
| Speaker Diarization | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 50 concurrent requests |

### Text to Speech REST

| Model | Service Limit |
|-------|---------------|
| Aura | Up to 15 concurrent requests |
| Aura-2 | Up to 15 concurrent requests |

### Text to Speech Streaming

| Model | Service Limit |
|-------|---------------|
| Aura | Up to 45 concurrent requests |
| Aura-2 | Up to 45 concurrent requests |

### Audio Intelligence

If you include Audio Intelligence features in requests to /listen, you will be subject to the service limits noted in the table below.

| Model | Service Limit |
|-------|---------------|
| Intent Recognition | Up to 10 concurrent requests |
| Entity Detection | Up to 5 concurrent requests |
| Sentiment Analysis | Up to 10 concurrent requests |
| Summarization | Up to 10 concurrent requests |
| Topic Detection | Up to 10 concurrent requests |

### Text Intelligence

| Model | Service Limit |
|-------|---------------|
| Intent Recognition | Up to 10 concurrent requests |
| Sentiment Analysis | Up to 10 concurrent requests |
| Summarization | Up to 10 concurrent requests |
| Topic Detection | Up to 10 concurrent requests |

## Growth

Limits to consider if you use the Growth plan with Deepgram.

### Voice Agent

| API | Connection Limits |
|-----|-------------------|
| Voice Agent API | Up to 60 concurrent connections |

### Speech to Text

If multiple services are used in one API call (e.g Speech to Text + Sentiment Analysis), the lower of the rate limits is applied.

| Model | Service Limit |
|-------|---------------|
| Flux | Streaming Up to 225 concurrent requests |
| Nova-3 | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 225 concurrent requests |
| Nova-2 | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 225 concurrent requests |
| Nova | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 225 concurrent requests |
| Enhanced | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 225 concurrent requests |
| Base | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 225 concurrent requests |
| Whisper Cloud | Pre-Recorded Up to 3 concurrent requests |

If you include Speaker Diarization features in requests to /listen, you will be subject to the service limits noted in the table below.

| Model | Service Limit |
|-------|---------------|
| Speaker Diarization | Pre-Recorded Up to 50 concurrent requests / Streaming Up to 50 concurrent requests |

### Text to Speech REST

| Model | Service Limit |
|-------|---------------|
| Aura | Up to 15 concurrent requests |
| Aura-2 | Up to 15 concurrent requests |

### Text to Speech Streaming

| Model | Service Limit |
|-------|---------------|
| Aura | Up to 60 concurrent requests |
| Aura-2 | Up to 60 concurrent requests |

### Audio Intelligence

If you include Audio Intelligence features in requests to /listen, you will be subject to the service limits noted in the table below.

| Model | Service Limit |
|-------|---------------|
| Intent Recognition | Up to 10 concurrent requests |
| Entity Detection | Up to 5 concurrent requests |
| Sentiment Analysis | Up to 10 concurrent requests |
| Summarization | Up to 10 concurrent requests |
| Topic Detection | Up to 10 concurrent requests |

### Text Intelligence

| Model | Service Limit |
|-------|---------------|
| Intent Recognition | Up to 10 concurrent requests |
| Sentiment Analysis | Up to 10 concurrent requests |
| Summarization | Up to 10 concurrent requests |
| Topic Detection | Up to 10 concurrent requests |

## Enterprise

Starting limits to consider if you have an Enterprise Contract with Deepgram.

New and existing Enterprise customers can request a Service Limit increase by discussing your needs with the Deepgram Sales Team.

### Voice Agent

| API | Connection Limits |
|-----|-------------------|
| Voice Agent API | Starting at 100 concurrent connections |

### Speech to Text

If multiple services are used in one API call (e.g Speech to Text + Sentiment Analysis), the lower of the rate limits is applied.

| Model | Service Limit |
|-------|---------------|
| Flux | Streaming Up to 300 concurrent requests |
| Nova-3 | Pre-Recorded Starting at 200 concurrent requests / Streaming Starting at 300 concurrent requests |
| Nova-2 | Pre-Recorded Starting at 200 concurrent requests / Streaming Starting at 300 concurrent requests |
| Nova | Pre-Recorded Starting at 200 concurrent requests / Streaming Starting at 300 concurrent requests |
| Enhanced | Pre-Recorded Starting at 200 concurrent requests / Streaming Starting at 300 concurrent requests |
| Base | Pre-Recorded Starting at 200 concurrent requests / Streaming Starting at 300 concurrent requests |
| Whisper Cloud | Pre-Recorded Starting at 15 concurrent requests |

If you include Speaker Diarization features in requests to /listen, you will be subject to the service limits noted in the table below.

| Model | Service Limit |
|-------|---------------|
| Speaker Diarization | Pre-Recorded Up to 100 concurrent requests / Streaming Up to 100 concurrent requests |

### Text to Speech REST

| Model | Service Limit |
|-------|---------------|
| Aura | Starting at 25 concurrent requests |
| Aura-2 | Starting at 25 concurrent requests |

### Text to Speech Streaming

| Model | Service Limit |
|-------|---------------|
| Aura | Starting at 100 concurrent requests |
| Aura-2 | Starting at 100 concurrent requests |

### Audio Intelligence

If you include Audio Intelligence features in requests to /listen, you will be subject to the service limits noted in the table below.

| Model | Service Limit |
|-------|---------------|
| Intent Recognition | Starting at 10 concurrent requests |
| Entity Detection | Starting at 10 concurrent requests |
| Sentiment Analysis | Starting at 10 concurrent requests |
| Summarization | Starting at 20 concurrent requests |
| Topic Detection | Starting at 10 concurrent requests |

### Text Intelligence

| Model | Service Limit |
|-------|---------------|
| Intent Recognition | Starting at 10 concurrent requests |
| Sentiment Analysis | Starting at 10 concurrent requests |
| Summarization | Starting at 20 concurrent requests |
| Topic Detection | Starting at 10 concurrent requests |

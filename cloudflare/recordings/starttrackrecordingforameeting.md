# Start recording audio and video tracks

`POST /accounts/{account_id}/realtime/kit/{app_id}/recordings/track`

Starts a track recording in a meeting. Track recordings consist of "layers". Layers are used to map audio/video tracks in a meeting to output destinations. More information about track recordings is available in the [Track Recordings Guide Page](https://docs.realtime.cloudflare.com/guides/capabilities/recording/recording-overview).

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 

## Request Body

- **layers** (object, required): 
- **max_seconds** (number, optional): Maximum seconds this recording should be active for (beta)
- **meeting_id** (string, required): ID of the meeting to record.

## Response

### 200

OK

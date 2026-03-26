# Delete additional audio tracks on a video

`DELETE /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}`

Deletes additional audio tracks on a video. Deleting a default audio track is not allowed. You must assign another audio track as default prior to deletion.

## Parameters

- **account_id** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **audio_identifier** (string, required) [path]: 

## Response

### 200

Deletes additional audio tracks on a video.

- **result** (string, optional): 

### 4XX

Deletes additional audio tracks on a video response failure.

- **result** (string, optional):

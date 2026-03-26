# Edit additional audio tracks on a video

`PATCH /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}`

Edits additional audio tracks on a video. Editing the default status of an audio track to `true` will mark all other audio tracks on the video default status to `false`.

## Parameters

- **account_id** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **audio_identifier** (string, required) [path]: 

## Request Body

- **default** (boolean, optional): Denotes whether the audio track will be played by default in a player.
- **label** (string, optional): A string to uniquely identify the track amongst other audio track labels for the specified video.

## Response

### 200

Edits additional audio tracks on a video.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Edits additional audio tracks on a video response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

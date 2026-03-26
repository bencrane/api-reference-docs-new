# List additional audio tracks on a video

`GET /accounts/{account_id}/stream/{identifier}/audio`

Lists additional audio tracks on a video. Note this API will not return information for audio attached to the video upload.

## Parameters

- **account_id** (string, required) [path]: 
- **identifier** (string, required) [path]: 

## Response

### 200

Lists additional audio tracks on a video.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Lists additional audio tracks on a video response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

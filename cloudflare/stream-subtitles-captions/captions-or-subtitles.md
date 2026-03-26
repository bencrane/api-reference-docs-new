# List captions or subtitles

`GET /accounts/{account_id}/stream/{identifier}/captions`

Lists the available captions or subtitles for a specific video.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List captions or subtitles response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List captions or subtitles response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

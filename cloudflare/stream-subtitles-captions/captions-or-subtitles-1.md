# Delete captions or subtitles

`DELETE /accounts/{account_id}/stream/{identifier}/captions/{language}`

Removes the captions or subtitles from a video.

## Parameters

- **language** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete captions or subtitles response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (string, optional): 

### 4XX

Delete captions or subtitles response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

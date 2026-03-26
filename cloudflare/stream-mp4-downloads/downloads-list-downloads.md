# List downloads

`GET /accounts/{account_id}/stream/{identifier}/downloads`

Lists the downloads created for a video.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List downloads response.

- **result** (object, optional): An object with download type keys. Each key is optional and only present if that download type has been created.

### 4XX

List downloads response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

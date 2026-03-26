# Upload captions or subtitles

`PUT /accounts/{account_id}/stream/{identifier}/captions/{language}`

Uploads the caption or subtitle file to the endpoint for a specific BCP47 language. One caption or subtitle file per language is allowed.

## Parameters

- **language** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Upload captions or subtitles response.

- **result** (object, optional): 

### 4XX

Upload captions or subtitles response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

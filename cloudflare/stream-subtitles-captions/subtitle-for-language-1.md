# Generate captions or subtitles for a provided language via AI

`POST /accounts/{account_id}/stream/{identifier}/captions/{language}/generate`

Generate captions or subtitles for provided language via AI.

## Parameters

- **language** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Generate captions or subtitles response for a provided language.

- **result** (object, optional): 

### 4XX

Generate captions or subtitles response for a provided language.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# List captions or subtitles for a provided language

`GET /accounts/{account_id}/stream/{identifier}/captions/{language}`

Lists the captions or subtitles for provided language.

## Parameters

- **language** (string, required) [path]: 
- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List captions or subtitles response for a provided language.

- **result** (object, optional): 

### 4XX

List captions or subtitles response for a provided language.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

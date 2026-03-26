# Delete downloads

`DELETE /accounts/{account_id}/stream/{identifier}/downloads`

Delete the downloads for a video. Use `/downloads/{download_type}` instead for type-specific downloads. Available types are `default` and `audio`.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete downloads response.

- **result** (string, optional): 

### 4XX

Delete downloads response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

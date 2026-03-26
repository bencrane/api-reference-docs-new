# Create downloads

`POST /accounts/{account_id}/stream/{identifier}/downloads`

Creates a download for a video when a video is ready to view. Use `/downloads/{download_type}` instead for type-specific downloads. Available types are `default` and `audio`.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Create downloads response.

- **result** (object, optional): 

### 4XX

Create downloads response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

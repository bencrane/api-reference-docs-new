# Create download

`POST /accounts/{account_id}/stream/{identifier}/downloads/{download_type}`

Creates a download for a video of specified type. For backwards-compatibility, POST requests to /downloads will enable the default download.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **download_type** (string, required) [path]: 


## Response

### 200

Create download of specified type response.

- **result** (object, optional): An object with download type keys. Each key is optional and only present if that download type has been created.

### 4XX

Create downloads of specified type response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

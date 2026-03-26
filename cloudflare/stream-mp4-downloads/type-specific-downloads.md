# Delete download

`DELETE /accounts/{account_id}/stream/{identifier}/downloads/{download_type}`

Delete specific type of download. For backwards-compatibility, DELETE requests to /downloads will delete the default download.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **download_type** (string, required) [path]: 

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

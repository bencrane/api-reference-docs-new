# Download Worker

`GET /accounts/{account_id}/workers/scripts/{script_name}`

Fetch raw script content for your worker. Note this is the original script content, not JSON encoded.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Worker successfully downloaded. Returns script content as a multipart form, with no metadata part and no JSON encoding applied.

### 4XX

Download Worker response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

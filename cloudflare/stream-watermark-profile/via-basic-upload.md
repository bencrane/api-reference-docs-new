# Create watermark profiles via basic upload

`POST /accounts/{account_id}/stream/watermarks`

Creates watermark profiles using a single `HTTP POST multipart/form-data` request.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Create watermark profiles via basic upload response.

- **result** (object, optional): 

### 4XX

Create watermark profiles via basic upload response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

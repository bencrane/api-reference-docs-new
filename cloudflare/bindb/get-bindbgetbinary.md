# Retrieves a file from Binary Storage

`GET /accounts/{account_id}/cloudforce-one/binary/{hash}`



## Parameters

- **account_id** (number, required) [path]: Account ID.
- **hash** (string, required) [path]: hash of the binary

## Response

### 200

Returns file information

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

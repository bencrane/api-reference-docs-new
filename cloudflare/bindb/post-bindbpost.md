# Posts a file to Binary Storage

`POST /accounts/{account_id}/cloudforce-one/binary`



## Parameters

- **account_id** (number, required) [path]: Account ID.


## Response

### 200

Returns file information

- **content_type** (string): 
- **md5** (string): 
- **sha1** (string): 
- **sha256** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

# Storage use

`GET /accounts/{account_id}/stream/storage-usage`

Returns information about an account's storage use.

## Parameters

- **account_id** (string, required) [path]: 
- **creator** (string, optional) [query]: 

## Response

### 200

Returns information about an account's storage use response.

- **result** (object, optional): 

### 4XX

Returns information about an account's storage use response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

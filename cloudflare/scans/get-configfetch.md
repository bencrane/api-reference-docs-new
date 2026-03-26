# List Scan Configs

`GET /accounts/{account_id}/cloudforce-one/scans/config`



## Parameters

- **account_id** (string, required) [path]: Defines the Account ID.

## Response

### 200

Returns all Scan Configs.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Scan Configs failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):

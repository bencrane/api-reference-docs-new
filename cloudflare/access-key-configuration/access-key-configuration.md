# Get the Access key configuration

`GET /accounts/{account_id}/access/keys`

Gets the Access key rotation settings for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get the Access key configuration response

_Empty object_

### 4XX

Get the Access key configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

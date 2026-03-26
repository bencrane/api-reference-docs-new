# List account configuration

`GET /accounts/{account_id}/mnm/config`

Lists default sampling, router IPs and warp devices for account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List account configuration response

- **result** (object, optional): 

### 4XX

List account configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

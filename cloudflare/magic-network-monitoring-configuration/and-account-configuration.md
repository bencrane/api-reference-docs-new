# List rules and account configuration

`GET /accounts/{account_id}/mnm/config/full`

Lists default sampling, router IPs, warp devices, and rules for account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List rules and account configuration response

- **result** (object, optional): 

### 4XX

List rules and account configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

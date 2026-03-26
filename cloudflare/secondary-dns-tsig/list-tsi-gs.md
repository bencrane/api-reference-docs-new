# List TSIGs

`GET /accounts/{account_id}/secondary_dns/tsigs`

List TSIGs.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List TSIGs response.

_Empty object_

### 4XX

List TSIGs response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

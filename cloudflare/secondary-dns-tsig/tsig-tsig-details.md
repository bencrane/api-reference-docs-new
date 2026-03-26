# TSIG Details

`GET /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}`

Get TSIG.

## Parameters

- **tsig_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

TSIG Details response.

_Empty object_

### 4XX

TSIG Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

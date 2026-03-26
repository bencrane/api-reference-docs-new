# Delete TSIG

`DELETE /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}`

Delete TSIG.

## Parameters

- **tsig_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete TSIG response.

_Empty object_

### 4XX

Delete TSIG response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

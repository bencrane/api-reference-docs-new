# Update TSIG

`PUT /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}`

Modify TSIG.

## Parameters

- **tsig_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **algo** (string, required): TSIG algorithm.
- **id** (string, required): 
- **name** (string, required): TSIG key name.
- **secret** (string, required): TSIG secret.

## Response

### 200

Update TSIG response.

_Empty object_

### 4XX

Update TSIG response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

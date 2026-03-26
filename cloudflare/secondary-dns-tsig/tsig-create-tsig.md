# Create TSIG

`POST /accounts/{account_id}/secondary_dns/tsigs`

Create TSIG.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **algo** (string, required): TSIG algorithm.
- **id** (string, required): 
- **name** (string, required): TSIG key name.
- **secret** (string, required): TSIG secret.

## Response

### 200

Create TSIG response.

_Empty object_

### 4XX

Create TSIG response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

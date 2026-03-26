# Add a new SSH Certificate Authority (CA)

`POST /accounts/{account_id}/access/gateway_ca`

Adds a new SSH Certificate Authority (CA).

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 201

Add a new SSH Certificate Authority (CA) response

_Empty object_

### 4XX

Add a new SSH Certificate Authority (CA) response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

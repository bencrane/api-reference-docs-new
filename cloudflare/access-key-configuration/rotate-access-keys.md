# Rotate Access keys

`POST /accounts/{account_id}/access/keys/rotate`

Perfoms a key rotation for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Rotate Access keys response

_Empty object_

### 4XX

Rotate Access keys response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

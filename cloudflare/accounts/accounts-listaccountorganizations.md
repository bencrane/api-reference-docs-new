# List account organizations

`GET /accounts/{account_id}/organizations`

Retrieve a list of the organizations that "contain" this account or are
managing it.

The returned list will be in order from "root" to "leaf", where the "leaf"
will be the organization that _immediately_ contains the specified
account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

The request has succeeded.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **success** (boolean): 

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):

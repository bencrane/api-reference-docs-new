# Add an Access identity provider

`POST /accounts/{account_id}/access/identity_providers`

Adds a new identity provider to Access.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 201

Add an Access identity provider response

_Empty object_

### 4XX

Add an Access identity provider response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

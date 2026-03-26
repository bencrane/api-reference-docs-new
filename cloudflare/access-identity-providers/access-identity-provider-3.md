# Update an Access identity provider

`PUT /accounts/{account_id}/access/identity_providers/{identity_provider_id}`

Updates a configured identity provider.

## Parameters

- **identity_provider_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Update an Access identity provider response

_Empty object_

### 4XX

Update an Access identity provider response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Get tenant account types

`GET /tenants/{tenant_id}/account_types`

List of account types available for the Tenant to provision accounts.

## Parameters

- **tenant_id** (string, required) [path]: 

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

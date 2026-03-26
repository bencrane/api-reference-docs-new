# List tenant memberships

`GET /tenants/{tenant_id}/memberships`

List of active members (Cloudflare users) for the Tenant.

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

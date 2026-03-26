# Batch create organization members

`POST /organizations/{organization_id}/members:batchCreate`

Batch create multiple memberships that grant access to a specific Organization.

## Parameters

- **organization_id** (string, required) [path]: 

## Request Body

- **members** (array, required): 

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

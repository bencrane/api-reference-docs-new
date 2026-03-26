# Get organization profile

`GET /organizations/{organization_id}/profile`

Get an organizations profile if it exists. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **organization_id** (string, required) [path]: The ID of the organization to retrieve a profile for.

## Response

### 200

The request has succeeded.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):

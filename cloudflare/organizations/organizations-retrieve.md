# Get organization

`GET /organizations/{organization_id}`

Retrieve the details of a certain organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **organization_id** (string, required) [path]: The ID of the organization to retrieve.

## Response

### 200

The request has succeeded.

- **errors** (array): 
- **messages** (array): 
- **result** (object): References an Organization in the Cloudflare data model.
- **success** (boolean): 

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):

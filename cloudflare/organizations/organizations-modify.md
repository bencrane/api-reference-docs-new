# Modify organization.

`PUT /organizations/{organization_id}`

Modify organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **organization_id** (string, required) [path]: The ID of the organization to modify.

## Request Body

- **create_time** (string, required): 
- **id** (object, required): 
- **meta** (object, required): 
- **name** (string, required): 
- **parent** (object, optional): 
- **profile** (object, optional): 

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

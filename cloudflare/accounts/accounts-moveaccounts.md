# Move account

`POST /accounts/{account_id}/move`

Move an account within an organization hierarchy or an account outside an organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination_organization_id** (string, required): 

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

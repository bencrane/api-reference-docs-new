# Create a new share recipient

`POST /accounts/{account_id}/shares/{share_id}/recipients`

Adds a recipient to a resource share, granting them access to the shared resources.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 

## Request Body

- **account_id** (string, optional): Account identifier.
- **organization_id** (string, optional): Organization identifier.

## Response

### 201

Share recipient created.

_Empty object_

### 4XX

Create share recipient failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Create share recipient failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

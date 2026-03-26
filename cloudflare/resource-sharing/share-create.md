# Create a new share

`POST /accounts/{account_id}/shares`

Creates a new resource share for sharing Cloudflare resources with other accounts or organizations.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The name of the share.
- **recipients** (array, required): 
- **resources** (array, required): 

## Response

### 201

Share created.

_Empty object_

### 4XX

Create share failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Create share failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

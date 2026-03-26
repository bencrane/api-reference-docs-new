# Create Zero Trust account

`POST /accounts/{account_id}/gateway`

Create a Zero Trust account for an existing Cloudflare account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Create Zero Trust account response.

_Empty object_

### 4XX

Create Zero Trust account response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`

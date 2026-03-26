# Get Zero Trust account information

`GET /accounts/{account_id}/gateway`

Retrieve information about the current Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Zero Trust account information response.

_Empty object_

### 4XX

Zero Trust account information response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`

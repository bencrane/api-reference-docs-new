# Get WARP IP subnet

`GET /accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}`

Get a WARP IP assignment subnet.

## Parameters

- **account_id** (string, required) [path]: 
- **subnet_id** (string, required) [path]: 

## Response

### 200

Get subnet response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get subnet response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

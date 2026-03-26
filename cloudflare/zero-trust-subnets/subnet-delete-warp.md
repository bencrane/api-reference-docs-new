# Delete WARP IP subnet

`DELETE /accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}`

Delete a WARP IP assignment subnet. This operation is idempotent - deleting an already-deleted or non-existent subnet will return success with a null result.

## Parameters

- **account_id** (string, required) [path]: 
- **subnet_id** (string, required) [path]: 

## Response

### 200

Delete subnet response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete subnet response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

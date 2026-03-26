# Update WARP IP subnet

`PATCH /accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}`

Updates a WARP IP assignment subnet.

**Update constraints:**
- The `network` field cannot be modified for WARP subnets. Only `name`, `comment`, and `is_default_network` can be updated.
- IPv6 subnets cannot be updated


## Parameters

- **account_id** (string, required) [path]: 
- **subnet_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): An optional description of the subnet.
- **is_default_network** (boolean, optional): If `true`, this is the default subnet for the account. There can only be one default subnet per account.
- **name** (string, optional): A user-friendly name for the subnet.
- **network** (string, optional): The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

## Response

### 200

Update subnet response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update subnet response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

# Update Cloudflare Source Subnet

`PATCH /accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}`

Updates the Cloudflare Source subnet of the given address family

## Parameters

- **account_id** (string, required) [path]: 
- **address_family** (string, required) [path]: 

## Request Body

- **comment** (string, optional): An optional description of the subnet.
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

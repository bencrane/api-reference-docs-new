# Create WARP IP subnet

`POST /accounts/{account_id}/zerotrust/subnets/warp`

Create a WARP IP assignment subnet. Currently, only IPv4 subnets can be created.

**Network constraints:**
- The network must be within one of the following private IP ranges:
  - `10.0.0.0/8` (RFC 1918)
  - `172.16.0.0/12` (RFC 1918)
  - `192.168.0.0/16` (RFC 1918)
  - `100.64.0.0/10` (RFC 6598 - CGNAT)
- The subnet must have a prefix length of `/24` or larger (e.g., `/16`, `/20`, `/24` are valid; `/25`, `/28` are not)


## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): An optional description of the subnet.
- **is_default_network** (boolean, optional): If `true`, this is the default subnet for the account. There can only be one default subnet per account.
- **name** (string, required): A user-friendly name for the subnet.
- **network** (string, required): The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

## Response

### 200

Create subnet response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create subnet response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

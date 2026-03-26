# Create a new Site WAN

`POST /accounts/{account_id}/magic/sites/{site_id}/wans`

Creates a new Site WAN.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): 
- **physport** (integer, required): 
- **priority** (integer, optional): 
- **static_addressing** (object, optional): (optional) if omitted, use DHCP. Submit secondary_address when site is in high availability mode.
- **vlan_tag** (integer, optional): VLAN ID. Use zero for untagged.

## Response

### 200

Create Site WAN response

- **result** (array, optional): 

### 4XX

Create Site WAN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

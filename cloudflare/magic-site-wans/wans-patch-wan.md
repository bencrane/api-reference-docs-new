# Patch Site WAN

`PATCH /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}`

Patch a specific Site WAN.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **wan_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): 
- **physport** (integer, optional): 
- **priority** (integer, optional): 
- **static_addressing** (object, optional): (optional) if omitted, use DHCP. Submit secondary_address when site is in high availability mode.
- **vlan_tag** (integer, optional): VLAN ID. Use zero for untagged.

## Response

### 200

Patch Site WAN response

- **result** (object, optional): 

### 4XX

Patch Site WAN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

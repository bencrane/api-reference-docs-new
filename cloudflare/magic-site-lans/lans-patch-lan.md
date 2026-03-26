# Patch Site LAN

`PATCH /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}`

Patch a specific Site LAN.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **lan_id** (string, required) [path]: 

## Request Body

- **bond_id** (integer, optional): 
- **is_breakout** (boolean, optional): mark true to use this LAN for source-based breakout traffic
- **is_prioritized** (boolean, optional): mark true to use this LAN for source-based prioritized traffic
- **name** (string, optional): 
- **nat** (object, optional): 
- **physport** (integer, optional): 
- **routed_subnets** (array, optional): 
- **static_addressing** (object, optional): If the site is not configured in high availability mode, this configuration is optional (if omitted, use DHCP). However, if in high availability mode, static_address is required along with secondary and virtual address.
- **vlan_tag** (integer, optional): VLAN ID. Use zero for untagged.

## Response

### 200

Patch Site LAN response

- **result** (object, optional): 

### 4XX

Patch Site LAN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

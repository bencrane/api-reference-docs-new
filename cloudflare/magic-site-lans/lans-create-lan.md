# Create a new Site LAN

`POST /accounts/{account_id}/magic/sites/{site_id}/lans`

Creates a new Site LAN. If the site is in high availability mode, static_addressing is required along with secondary and virtual address.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Request Body

- **bond_id** (integer, optional): 
- **ha_link** (boolean, optional): mark true to use this LAN for HA probing. only works for site with HA turned on. only one LAN can be set as the ha_link.
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

Create Site LAN response

- **result** (array, optional): 

### 4XX

Create Site LAN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

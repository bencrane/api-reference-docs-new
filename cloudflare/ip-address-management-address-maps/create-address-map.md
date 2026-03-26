# Create Address Map

`POST /accounts/{account_id}/addressing/address_maps`

Create a new address map under the account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An optional description field which may be used to describe the types of IPs or zones on the map.
- **enabled** (boolean, optional): Whether the Address Map is enabled or not. Cloudflare's DNS will not respond with IP addresses on an Address Map until the map is enabled.
- **ips** (array, optional): 
- **memberships** (array, optional): Zones and Accounts which will be assigned IPs on this Address Map. A zone membership will take priority over an account membership.

## Response

### 200

Create Address Map response

- **result** (object, optional): 

### 4XX

Create Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

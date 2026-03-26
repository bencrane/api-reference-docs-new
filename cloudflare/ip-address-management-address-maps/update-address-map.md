# Update Address Map

`PATCH /accounts/{account_id}/addressing/address_maps/{address_map_id}`

Modify properties of an address map owned by the account.

## Parameters

- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **default_sni** (string, optional): If you have legacy TLS clients which do not send the TLS server name indicator, then you can specify one default SNI on the map. If Cloudflare receives a TLS handshake from a client without an SNI, it will respond with the default SNI on those IPs. The default SNI can be any valid zone or subdomain owned by the account.
- **description** (string, optional): An optional description field which may be used to describe the types of IPs or zones on the map.
- **enabled** (boolean, optional): Whether the Address Map is enabled or not. Cloudflare's DNS will not respond with IP addresses on an Address Map until the map is enabled.

## Response

### 200

Update Address Map response

- **result** (object, optional): 

### 4XX

Update Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

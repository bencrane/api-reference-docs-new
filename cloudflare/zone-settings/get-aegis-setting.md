# Get aegis setting

`GET /zones/{zone_id}/settings/aegis`

Aegis provides dedicated egress IPs (from Cloudflare to your origin) for your layer 7 WAF and CDN services. The egress IPs are reserved exclusively for your account so that you can increase your origin security by only allowing traffic from a small list of IP addresses.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get aegis setting response.

_Empty object_

### 4XX

Get aegis setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

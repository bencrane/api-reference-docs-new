# Change aegis setting

`PATCH /zones/{zone_id}/settings/aegis`

Aegis provides dedicated egress IPs (from Cloudflare to your origin) for your layer 7 WAF and CDN services. The egress IPs are reserved exclusively for your account so that you can increase your origin security by only allowing traffic from a small list of IP addresses.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (object, required): Value of the zone setting.

## Response

### 200

Change aegis setting response.

_Empty object_

### 4XX

Change aegis setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

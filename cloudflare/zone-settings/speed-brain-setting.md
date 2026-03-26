# Get Cloudflare Speed Brain setting

`GET /zones/{zone_id}/settings/speed_brain`

Speed Brain lets compatible browsers speculate on content which can be prefetched or preloaded, making website
navigation faster. Refer to the Cloudflare Speed Brain documentation for more information.


## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Cloudflare Speed Brain setting response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Get Cloudflare Speed Brain setting response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

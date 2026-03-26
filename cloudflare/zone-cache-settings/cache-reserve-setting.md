# Get Cache Reserve setting

`GET /zones/{zone_id}/cache/cache_reserve`

Increase cache lifetimes by automatically storing all cacheable files into Cloudflare's persistent object storage buckets. Requires Cache Reserve subscription. Note: using Tiered Cache with Cache Reserve is highly recommended to reduce Reserve operations costs. See the [developer docs](https://developers.cloudflare.com/cache/about/cache-reserve) for more information.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Cache Reserve setting response.

_Empty object_

### 4XX

Get Cache Reserve setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

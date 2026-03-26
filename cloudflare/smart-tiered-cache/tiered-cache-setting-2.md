# Patch Smart Tiered Cache setting

`PATCH /zones/{zone_id}/cache/tiered_cache_smart_topology_enable`

Smart Tiered Cache dynamically selects the single closest upper tier for each of your website’s origins with no configuration required, using our in-house performance and routing data. Cloudflare collects latency data for each request to an origin, and uses the latency data to determine how well any upper-tier data center is connected with an origin. As a result, Cloudflare can select the data center with the lowest latency to be the upper-tier for an origin.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Enable or disable the Smart Tiered Cache. Values: `on`, `off`

## Response

### 200

Patch Smart Tiered Cache setting response.

_Empty object_

### 4XX

Patch Smart Tiered Cache setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

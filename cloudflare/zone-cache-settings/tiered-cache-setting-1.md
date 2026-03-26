# Change Regional Tiered Cache setting

`PATCH /zones/{zone_id}/cache/regional_tiered_cache`

Instructs Cloudflare to check a regional hub data center on the way to your upper tier. This can help improve performance for smart and custom tiered cache topologies.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Value of the Regional Tiered Cache zone setting. Values: `on`, `off`

## Response

### 200

Change Regional Tiered Cache setting response.

_Empty object_

### 4XX

Change Regional Tiered Cache setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

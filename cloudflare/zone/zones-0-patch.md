# Edit Zone

`PATCH /zones/{zone_id}`

Edits a zone. Only one zone property can be changed at a time.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **paused** (boolean, optional): Indicates whether the zone is only using Cloudflare DNS services. A
true value means the zone will not receive security or performance
benefits.

- **plan** (object, optional): (Deprecated) Please use the `/zones/{zone_id}/subscription` API
to update a zone's plan. Changing this value will create/cancel
associated subscriptions. To view available plans for this zone,
see Zone Plans.

- **type** (string, optional): A full zone implies that DNS is hosted with Cloudflare. A partial
zone is typically a partner-hosted zone or a CNAME setup. This
parameter is only available to Enterprise customers or if it has
been explicitly enabled on a zone.
 Values: `full`, `partial`, `secondary`, `internal`
- **vanity_name_servers** (array, optional): An array of domains used for custom name servers. This is only
available for Business and Enterprise plans.

## Response

### 200

Edit Zone response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Edit Zone response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

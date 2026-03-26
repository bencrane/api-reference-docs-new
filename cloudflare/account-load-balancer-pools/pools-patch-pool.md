# Patch Pool

`PATCH /accounts/{account_id}/load_balancers/pools/{pool_id}`

Apply changes to an existing pool, overwriting the supplied properties.

## Parameters

- **pool_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **check_regions** (array, optional): A list of regions from which to run health checks. Null means every Cloudflare data center.
- **description** (string, optional): A human-readable description of the pool.
- **disabled_at** (string, optional): This field shows up only if the pool is disabled. This field is set with the time the pool was disabled at.
- **enabled** (boolean, optional): Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).
- **latitude** (number, optional): The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.
- **load_shedding** (object, optional): Configures load shedding policies and percentages for the pool.
- **longitude** (number, optional): The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.
- **minimum_origins** (integer, optional): The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.
- **monitor** (string, optional): The ID of the Monitor to use for checking the health of origins within this pool.
- **monitor_group** (string, optional): The ID of the Monitor Group to use for checking the health of origins within this pool.
- **name** (string, optional): A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed.
- **notification_email** (string, optional): This field is now deprecated. It has been moved to Cloudflare's Centralized Notification service https://developers.cloudflare.com/fundamentals/notifications/. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.
- **notification_filter** (object, optional): Filter pool and origin health notifications by resource type or health status. Use null to reset.
- **origin_steering** (object, optional): Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity.
- **origins** (array, optional): The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy.

## Response

### 200

Patch Pool response.

- **result** (object, optional): 

### 4XX

Patch Pool response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

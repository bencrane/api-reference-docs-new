# Update zone-level Waiting Room settings

`PUT /zones/{zone_id}/waiting_rooms/settings`



## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **search_engine_crawler_bypass** (boolean, optional): Whether to allow verified search engine crawlers to bypass all waiting rooms on this zone.
Verified search engine crawlers will not be tracked or counted by the waiting room system,
and will not appear in waiting room analytics.


## Response

### 200

The updated zone-level Waiting Room settings

_Empty object_

### 4XX

The zone-level Waiting Room settings response failure

_Empty object_

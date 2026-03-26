# Get Cache Reserve Clear

`GET /zones/{zone_id}/cache/cache_reserve_clear`

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Cache Reserve Clear response.

_Empty object_

### 4XX

Get Cache Reserve Clear failure response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

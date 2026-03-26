# List events

`GET /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events`

Lists events for a waiting room.

## Parameters

- **waiting_room_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: Page number of paginated results.
- **per_page** (number, optional) [query]: Maximum number of results per page. Must be a multiple of 5.

## Response

### 200

List events response

_Empty object_

### 4XX

List events response failure

_Empty object_

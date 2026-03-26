# Preview active event details

`GET /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details`

Previews an event's configuration as if it was active. Inherited fields from the waiting room will be displayed with their current values.

## Parameters

- **event_id** (string, required) [path]: 
- **waiting_room_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Preview active event details response

_Empty object_

### 4XX

Preview active event details response failure

_Empty object_

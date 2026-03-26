# Get waiting room status

`GET /zones/{zone_id}/waiting_rooms/{waiting_room_id}/status`

Fetches the status of a configured waiting room. Response fields include:
1. `status`: String indicating the status of the waiting room. The possible status are:
	- **not_queueing** indicates that the configured thresholds have not been met and all users are going through to the origin.
	- **queueing** indicates that the thresholds have been met and some users are held in the waiting room.
	- **event_prequeueing** indicates that an event is active and is currently prequeueing users before it starts.
	- **suspended** indicates that the room is suspended.
2. `event_id`: String of the current event's `id` if an event is active, otherwise an empty string.
3. `estimated_queued_users`: Integer of the estimated number of users currently waiting in the queue.
4. `estimated_total_active_users`: Integer of the estimated number of users currently active on the origin.
5. `max_estimated_time_minutes`: Integer of the maximum estimated time currently presented to the users.

## Parameters

- **waiting_room_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get waiting room status response

_Empty object_

### 4XX

Get waiting room status response failure

_Empty object_

# Create Waiting Room Rule

`POST /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules`

Only available for the Waiting Room Advanced subscription. Creates a rule for a waiting room.

## Parameters

- **waiting_room_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **action** (string, required): The action to take when the expression matches. Values: `bypass_waiting_room`
- **description** (string, optional): The description of the rule.
- **enabled** (boolean, optional): When set to true, the rule is enabled.
- **expression** (string, required): Criteria defining when there is a match for the current rule.

## Response

### 200

Create Waiting Room Rule response

_Empty object_

### 4XX

Create Waiting Room Rule response failure

_Empty object_

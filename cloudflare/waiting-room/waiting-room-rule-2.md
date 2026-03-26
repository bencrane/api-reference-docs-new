# Patch Waiting Room Rule

`PATCH /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}`

Patches a rule for a waiting room.

## Parameters

- **rule_id** (string, required) [path]: 
- **waiting_room_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **action** (string, required): The action to take when the expression matches. Values: `bypass_waiting_room`
- **description** (string, optional): The description of the rule.
- **enabled** (boolean, optional): When set to true, the rule is enabled.
- **expression** (string, required): Criteria defining when there is a match for the current rule.
- **position** (object, optional): Reorder the position of a rule

## Response

### 200

Patch Waiting Room Rule response

_Empty object_

### 4XX

Patch Waiting Room Rule response failure

_Empty object_

# Create a User Agent Blocking rule

`POST /zones/{zone_id}/firewall/ua_rules`

Creates a new User Agent Blocking rule in a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **configuration** (object, required): 
- **description** (string, optional): An informative summary of the rule. This value is sanitized and any tags will be removed.
- **mode** (string, required): The action to apply to a matched request. Values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`
- **paused** (boolean, optional): When true, indicates that the rule is currently paused.

## Response

### 200

Create a User Agent Blocking rule response

- **result** (object, optional): 

### 4XX

Create a User Agent Blocking rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`

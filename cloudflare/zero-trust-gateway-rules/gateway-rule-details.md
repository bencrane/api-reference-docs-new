# Get Zero Trust Gateway rule details.

`GET /accounts/{account_id}/gateway/rules/{rule_id}`

Get a single Zero Trust Gateway rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get Zero Trust Gateway rule details response.

_Empty object_

### 4XX

Get Zero Trust Gateway rule details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`

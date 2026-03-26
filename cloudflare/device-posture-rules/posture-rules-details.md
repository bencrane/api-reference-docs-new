# Get device posture rule details

`GET /accounts/{account_id}/devices/posture/{rule_id}`

Fetches a single device posture rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get device posture rule details response.

- **result** (object, optional): 

### 4XX

Get device posture rule details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

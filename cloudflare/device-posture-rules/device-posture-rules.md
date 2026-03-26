# List device posture rules

`GET /accounts/{account_id}/devices/posture`

Fetches device posture rules for a Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List device posture rules response.

- **result** (array, optional): 

### 4XX

List device posture rules response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

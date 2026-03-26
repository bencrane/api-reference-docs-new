# Get device settings profile by ID

`GET /accounts/{account_id}/devices/policy/{policy_id}`

Fetches a device settings profile by ID.

## Parameters

- **policy_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get device settings profile by ID response.

- **result** (object, optional): 

### 4XX

Get device settings profile by ID response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

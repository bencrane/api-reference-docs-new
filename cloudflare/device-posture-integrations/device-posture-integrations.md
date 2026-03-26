# List your device posture integrations

`GET /accounts/{account_id}/devices/posture/integration`

Fetches the list of device posture integrations for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List your device posture integrations response.

- **result** (array, optional): 

### 4XX

List your device posture integrations response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Get risk event/score information for a specific user

`GET /accounts/{account_id}/zt_risk_scoring/{user_id}`

Retrieves the detailed risk score breakdown for a specific user, including contributing factors.

## Parameters

- **account_id** (string, required) [path]: 
- **user_id** (string, required) [path]: 

## Response

### 200

Risk events.

- **result** (object, optional): 

### 4XX

Failed to get risk events.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

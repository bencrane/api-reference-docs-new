# Get all behaviors and associated configuration

`GET /accounts/{account_id}/zt_risk_scoring/behaviors`

Retrieves configured risk score behaviors that define how user actions affect their overall risk score.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Risk scoring behaviors.

- **result** (object, optional): 

### 4XX

Failed to get risk scoring behaviors.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

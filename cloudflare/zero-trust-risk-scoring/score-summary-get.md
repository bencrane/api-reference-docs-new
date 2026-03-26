# Get risk score info for all users in the account

`GET /accounts/{account_id}/zt_risk_scoring/summary`

Gets an aggregate summary of risk scores across the account, including distribution and trends.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Risk score for all users in the account.

- **result** (object, optional): 

### 4XX

Failed to get risk scores.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

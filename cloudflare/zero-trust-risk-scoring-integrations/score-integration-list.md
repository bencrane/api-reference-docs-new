# List all risk score integrations for the account.

`GET /accounts/{account_id}/zt_risk_scoring/integrations`

Lists all configured Zero Trust risk score integrations for the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List response.

- **result** (array, optional): 

### 4XX

List failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

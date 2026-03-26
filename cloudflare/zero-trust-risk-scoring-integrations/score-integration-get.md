# Get risk score integration by id.

`GET /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **integration_id** (string, required) [path]: 

## Response

### 200

Get response.

- **result** (object, optional): 

### 4XX

Get failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

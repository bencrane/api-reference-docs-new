# Get risk score integration by reference id.

`GET /accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}`

Retrieves a Zero Trust risk score integration using its external reference ID.

## Parameters

- **account_id** (string, required) [path]: 
- **reference_id** (string, required) [path]: 

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

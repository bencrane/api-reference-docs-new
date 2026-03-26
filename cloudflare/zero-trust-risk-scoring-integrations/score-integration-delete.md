# Delete a risk score integration.

`DELETE /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}`

Removes a Zero Trust risk score integration, disconnecting the external risk signal source.

## Parameters

- **account_id** (string, required) [path]: 
- **integration_id** (string, required) [path]: 

## Response

### 200

Delete response.

- **result** (object, optional): 

### 4XX

Delete failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

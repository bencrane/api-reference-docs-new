# Update configuration for risk behaviors

`PUT /accounts/{account_id}/zt_risk_scoring/behaviors`

Updates risk score behavior configurations, defining weights and thresholds for risk calculation.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **behaviors** (object, required): 

## Response

### 200

Dataset created successfully.

- **result** (object, optional): 

### 4XX

Dataset creation failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

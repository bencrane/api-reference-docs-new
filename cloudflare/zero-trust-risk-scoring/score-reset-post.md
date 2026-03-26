# Clear the risk score for a particular user

`POST /accounts/{account_id}/zt_risk_scoring/{user_id}/reset`

Resets risk scores for specified users, clearing their accumulated risk history.

## Parameters

- **account_id** (string, required) [path]: 
- **user_id** (string, required) [path]: 

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

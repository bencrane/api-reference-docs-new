# Monitor Details

`GET /accounts/{account_id}/load_balancers/monitors/{monitor_id}`

List a single configured monitor for an account.

## Parameters

- **monitor_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Monitor Details response.

- **result** (object, optional): 

### 4XX

Monitor Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Connect PagerDuty

`GET /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}`

Links PagerDuty with the account using the integration token.

## Parameters

- **account_id** (string, required) [path]: 
- **token_id** (string, required) [path]: 

## Response

### 200

Create a Notification policy response

- **result** (object, optional): 

### 4XX

Create a Notification policy response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

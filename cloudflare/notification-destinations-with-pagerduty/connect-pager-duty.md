# Create PagerDuty integration token

`POST /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect`

Creates a new token for integrating with PagerDuty.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 201

Token for PagerDuty integration

- **result** (object, optional): 

### 4XX

Create a token for PagerDuty integration failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

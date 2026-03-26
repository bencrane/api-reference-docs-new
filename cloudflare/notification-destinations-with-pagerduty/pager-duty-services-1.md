# List PagerDuty services

`GET /accounts/{account_id}/alerting/v3/destinations/pagerduty`

Get a list of all configured PagerDuty services.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List PagerDuty services response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (array, optional): 

### 4XX

List PagerDuty services response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

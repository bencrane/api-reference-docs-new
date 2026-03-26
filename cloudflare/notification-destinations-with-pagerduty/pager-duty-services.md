# Delete PagerDuty Services

`DELETE /accounts/{account_id}/alerting/v3/destinations/pagerduty`

Deletes all the PagerDuty Services connected to the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Delete PagerDuty Services response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful

### 4XX

Delete PagerDuty Services response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

# Get delivery mechanism eligibility

`GET /accounts/{account_id}/alerting/v3/destinations/eligible`

Get a list of all delivery mechanism types for which an account is eligible.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get delivery mechanism eligibility response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (object, optional): 

### 4XX

Get delivery mechanism eligibility response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

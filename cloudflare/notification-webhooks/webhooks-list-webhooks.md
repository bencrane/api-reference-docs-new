# List webhooks

`GET /accounts/{account_id}/alerting/v3/destinations/webhooks`

Gets a list of all configured webhook destinations.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List webhooks response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (array, optional): 

### 4XX

List webhooks response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

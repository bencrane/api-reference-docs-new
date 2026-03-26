# Get a webhook

`GET /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}`

Get details for a single webhooks destination.

## Parameters

- **account_id** (string, required) [path]: 
- **webhook_id** (string, required) [path]: 

## Response

### 200

Get a webhook response

- **result** (object, optional): 

### 4XX

Get a webhook response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

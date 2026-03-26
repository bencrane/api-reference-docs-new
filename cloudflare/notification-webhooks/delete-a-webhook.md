# Delete a webhook

`DELETE /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}`

Delete a configured webhook destination.

## Parameters

- **webhook_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete a webhook response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful

### 4XX

Delete a webhook response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

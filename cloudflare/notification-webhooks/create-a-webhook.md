# Create a webhook

`POST /accounts/{account_id}/alerting/v3/destinations/webhooks`

Creates a new webhook destination.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The name of the webhook destination. This will be included in the request body when you receive a webhook notification.
- **secret** (string, optional): Optional secret that will be passed in the `cf-webhook-auth` header when dispatching generic webhook notifications or formatted for supported destinations. Secrets are not returned in any API response body.
- **url** (string, required): The POST endpoint to call when dispatching a notification.

## Response

### 201

Create a webhook response

- **result** (object, optional): 

### 4XX

Create a webhook response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

# Create webhooks

`PUT /accounts/{account_id}/stream/webhook`

Creates a webhook notification.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **notificationUrl** (string, required): The URL where webhooks will be sent.

## Response

### 200

Create webhooks response.

- **result** (object, optional): 

### 4XX

Create webhooks response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

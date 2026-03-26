# Add a webhook

`POST /accounts/{account_id}/realtime/kit/{app_id}/webhooks`

Adds a new webhook to an App.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): Set whether or not the webhook should be active when created
- **events** (array, required): Events that this webhook will get triggered by
- **name** (string, required): Name of the webhook
- **url** (string, required): URL this webhook will send events to

## Response

### 201

Webhook registered successfully

- **data** (object): 
- **success** (boolean): 

### 400

Error - malformed request

- **error** (object): Object containing details of the error that occurred
- **success** (boolean): Whether the operation succeeded or not

### 401

Invalid credentials

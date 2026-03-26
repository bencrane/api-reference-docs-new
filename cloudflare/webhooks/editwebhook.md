# Edit a webhook

`PATCH /accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}`

Edits the webhook details for the given webhook ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **webhook_id** (string, required) [path]: ID of the webhook

## Request Body

- **enabled** (boolean, optional): 
- **events** (array, optional): Events that the webhook will get triggered by
- **name** (string, optional): Name of the webhook
- **url** (string, optional): URL the webhook will send events to

## Response

### 200

Operation successful

- **data** (object): 
- **success** (boolean): 

### 400

Error - malformed request

- **error** (object): Object containing details of the error that occurred
- **success** (boolean): Whether the operation succeeded or not

### 401

Invalid credentials

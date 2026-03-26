# Fetch details of a webhook

`GET /accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}`

Returns webhook details for the given webhook ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **webhook_id** (string, required) [path]: ID of the webhook

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

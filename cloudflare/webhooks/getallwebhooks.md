# Fetch all webhooks details

`GET /accounts/{account_id}/realtime/kit/{app_id}/webhooks`

Returns details of all webhooks for an App.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 

## Response

### 200

Operation successful

- **data** (array): 
- **success** (boolean): 

### 401

Invalid credentials

# Retrieve app details

`GET /accounts/{account_id}/calls/apps/{app_id}`

Fetches details for a single Calls app.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Retrieve app details response

- **result** (object, optional): 

### 4XX

Retrieve app details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

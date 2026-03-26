# Get a short-lived certificate CA

`GET /accounts/{account_id}/access/apps/{app_id}/ca`

Fetches a short-lived certificate CA and its public key.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get a short-lived certificate CA response

_Empty object_

### 4XX

Get a short-lived certificate CA response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Create a short-lived certificate CA

`POST /accounts/{account_id}/access/apps/{app_id}/ca`

Generates a new short-lived certificate CA and public key.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Create a short-lived certificate CA response

_Empty object_

### 4XX

Create a short-lived certificate CA response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

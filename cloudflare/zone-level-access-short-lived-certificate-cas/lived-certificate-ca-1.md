# Get a short-lived certificate CA

`GET /zones/{zone_id}/access/apps/{app_id}/ca`

Fetches a short-lived certificate CA and its public key.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

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

# Get an Access application

`GET /accounts/{account_id}/access/apps/{app_id}`

Fetches information about an Access application.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get an Access application response

_Empty object_

### 4XX

Get an Access application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

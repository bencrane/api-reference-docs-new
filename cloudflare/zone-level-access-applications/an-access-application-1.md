# Get an Access application

`GET /zones/{zone_id}/access/apps/{app_id}`

Fetches information about an Access application.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

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

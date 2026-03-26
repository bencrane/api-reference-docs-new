# List Access policies

`GET /zones/{zone_id}/access/apps/{app_id}/policies`

Lists Access policies configured for an application.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

List Access policies response

_Empty object_

### 4XX

List Access policies response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

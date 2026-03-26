# Delete Spectrum application

`DELETE /zones/{zone_id}/spectrum/apps/{app_id}`

Deletes a previously existing application.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete Spectrum application response.

_Empty object_

### 4XX

Delete Spectrum application response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

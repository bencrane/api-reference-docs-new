# Get RUM status for a zone

`GET /zones/{zone_id}/settings/rum`

Retrieves RUM status for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Rum Status.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

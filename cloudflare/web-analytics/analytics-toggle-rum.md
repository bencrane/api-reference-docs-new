# Toggle RUM on/off for a zone

`PATCH /zones/{zone_id}/settings/rum`

Toggles RUM on/off for an existing zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, optional): Value can either be On or Off.

## Response

### 200

Rum toggled on/off for an existing zone.

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

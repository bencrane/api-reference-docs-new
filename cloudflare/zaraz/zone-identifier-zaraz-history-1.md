# Restore Zaraz historical configuration by ID

`PUT /zones/{zone_id}/settings/zaraz/history`

Restores a historical published Zaraz configuration by ID for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

integer

## Response

### 200

Restore Zaraz historical configuration by ID response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Restore Zaraz historical configuration by ID failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

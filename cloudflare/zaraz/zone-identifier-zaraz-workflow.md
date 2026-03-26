# Get Zaraz workflow

`GET /zones/{zone_id}/settings/zaraz/workflow`

Gets Zaraz workflow for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Zaraz workflow response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (string, optional): Zaraz workflow. Values: `realtime`, `preview`

### 4XX

Get Zaraz workflow response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

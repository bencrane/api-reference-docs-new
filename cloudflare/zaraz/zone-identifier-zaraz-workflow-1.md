# Update Zaraz workflow

`PUT /zones/{zone_id}/settings/zaraz/workflow`

Updates Zaraz workflow for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

string

## Response

### 200

Update Zaraz workflow response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (string, optional): Zaraz workflow. Values: `realtime`, `preview`

### 4XX

Update Zaraz workflow response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

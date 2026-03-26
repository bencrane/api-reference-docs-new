# List Regional Hostnames

`GET /zones/{zone_id}/addressing/regional_hostnames`

List all Regional Hostnames within a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List hostnames response

- **result** (array, optional): 

### 4XX

Failure to list hostnames

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

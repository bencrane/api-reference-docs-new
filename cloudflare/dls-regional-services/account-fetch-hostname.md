# Fetch Regional Hostname

`GET /zones/{zone_id}/addressing/regional_hostnames/{hostname}`

Fetch the configuration for a specific Regional Hostname, within a zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **hostname** (string, required) [path]: 

## Response

### 200

Fetch hostname response

- **result** (object, optional): 

### 4XX

Failure to fetch hostname

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

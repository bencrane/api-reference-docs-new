# Update Regional Hostname

`PATCH /zones/{zone_id}/addressing/regional_hostnames/{hostname}`

Update the configuration for a specific Regional Hostname. Only the region_key of a hostname is mutable.

## Parameters

- **zone_id** (string, required) [path]: 
- **hostname** (string, required) [path]: 

## Request Body

- **region_key** (string, required): Identifying key for the region

## Response

### 200

Update hostname response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Failure to update hostname

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

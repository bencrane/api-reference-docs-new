# Secondary Zone Configuration Details

`GET /zones/{zone_id}/secondary_dns/incoming`

Get secondary zone configuration for incoming zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Secondary Zone Configuration Details response.

_Empty object_

### 4XX

Secondary Zone Configuration Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Delete Secondary Zone Configuration

`DELETE /zones/{zone_id}/secondary_dns/incoming`

Delete secondary zone configuration for incoming zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Secondary Zone Configuration response.

_Empty object_

### 4XX

Delete Secondary Zone Configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Delete Primary Zone Configuration

`DELETE /zones/{zone_id}/secondary_dns/outgoing`

Delete primary zone configuration for outgoing zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Primary Zone Configuration response.

_Empty object_

### 4XX

Delete Primary Zone Configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

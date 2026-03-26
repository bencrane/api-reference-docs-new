# Primary Zone Configuration Details

`GET /zones/{zone_id}/secondary_dns/outgoing`

Get primary zone configuration for outgoing zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Primary Zone Configuration Details response.

_Empty object_

### 4XX

Primary Zone Configuration Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

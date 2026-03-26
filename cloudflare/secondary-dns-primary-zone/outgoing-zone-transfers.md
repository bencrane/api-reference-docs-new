# Disable Outgoing Zone Transfers

`POST /zones/{zone_id}/secondary_dns/outgoing/disable`

Disable outgoing zone transfers for primary zone and clears IXFR backlog of primary zone.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Disable Outgoing Zone Transfers response.

_Empty object_

### 4XX

Disable Outgoing Zone Transfers response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

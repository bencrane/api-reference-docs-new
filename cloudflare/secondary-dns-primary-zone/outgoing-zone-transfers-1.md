# Enable Outgoing Zone Transfers

`POST /zones/{zone_id}/secondary_dns/outgoing/enable`

Enable outgoing zone transfers for primary zone.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Enable Outgoing Zone Transfers response.

_Empty object_

### 4XX

Enable Outgoing Zone Transfers response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Get Outgoing Zone Transfer Status

`GET /zones/{zone_id}/secondary_dns/outgoing/status`

Get primary zone transfer status.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Outgoing Zone Transfer Status response.

_Empty object_

### 4XX

Get Outgoing Zone Transfer Status response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Force DNS NOTIFY

`POST /zones/{zone_id}/secondary_dns/outgoing/force_notify`

Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Force DNS NOTIFY response.

_Empty object_

### 4XX

Force DNS NOTIFY response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

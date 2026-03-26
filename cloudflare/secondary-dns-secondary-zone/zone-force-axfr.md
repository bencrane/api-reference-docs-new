# Force AXFR

`POST /zones/{zone_id}/secondary_dns/force_axfr`

Sends AXFR zone transfer request to primary nameserver(s).

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Force AXFR response.

_Empty object_

### 4XX

Force AXFR response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Delete Certificate

`DELETE /zones/{zone_id}/origin_tls_client_auth/{certificate_id}`

Removes a client certificate used for zone-level authenticated origin pulls.

## Parameters

- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Certificate response

- **result** (object, optional): 

### 4XX

Delete Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

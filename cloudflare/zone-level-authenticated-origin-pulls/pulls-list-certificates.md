# List Certificates

`GET /zones/{zone_id}/origin_tls_client_auth`

Lists all client certificates configured for zone-level authenticated origin pulls.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Certificates response

- **result** (array, optional): 

### 4XX

List Certificates response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

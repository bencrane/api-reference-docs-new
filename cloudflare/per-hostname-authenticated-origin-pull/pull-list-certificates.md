# List Certificates

`GET /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates`

Lists all client certificates configured for per-hostname authenticated origin pulls on the zone.

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

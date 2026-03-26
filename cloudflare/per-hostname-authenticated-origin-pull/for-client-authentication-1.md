# Get the Hostname Status for Client Authentication

`GET /zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}`

Retrieves the client certificate authentication status for a specific hostname, showing whether authenticated origin pulls are enabled.

## Parameters

- **hostname** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get the Hostname Status for Client Authentication response

- **result** (object, optional): 

### 4XX

Get the Hostname Status for Client Authentication response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

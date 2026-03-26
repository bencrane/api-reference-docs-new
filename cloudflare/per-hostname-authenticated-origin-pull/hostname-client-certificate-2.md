# Get the Hostname Client Certificate

`GET /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}`

Get the certificate by ID to be used for client authentication on a hostname.

## Parameters

- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get the Hostname Client Certificate response

- **result** (object, optional): 

### 4XX

Get the Hostname Client Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

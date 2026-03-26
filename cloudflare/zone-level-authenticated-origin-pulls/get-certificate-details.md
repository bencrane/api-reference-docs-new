# Get Certificate Details

`GET /zones/{zone_id}/origin_tls_client_auth/{certificate_id}`

Retrieves details for a specific client certificate used in zone-level authenticated origin pulls.

## Parameters

- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get Certificate Details response

- **result** (object, optional): 

### 4XX

Get Certificate Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

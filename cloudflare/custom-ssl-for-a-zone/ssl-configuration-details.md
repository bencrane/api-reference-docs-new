# SSL Configuration Details

`GET /zones/{zone_id}/custom_certificates/{custom_certificate_id}`

Retrieves details for a specific custom SSL certificate, including certificate metadata, bundle method, geographic restrictions, and associated keyless server configuration.

## Parameters

- **custom_certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

SSL Configuration Details response

- **result** (object, optional): 

### 4XX

SSL Configuration Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

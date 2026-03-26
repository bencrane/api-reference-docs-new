# Get Keyless SSL Configuration

`GET /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}`

Get details for one Keyless SSL configuration.

## Parameters

- **keyless_certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get Keyless SSL Configuration response

- **result** (object, optional): 

### 4XX

Get Keyless SSL Configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

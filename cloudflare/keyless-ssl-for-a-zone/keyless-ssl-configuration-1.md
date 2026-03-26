# Delete Keyless SSL Configuration

`DELETE /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}`

Removes a Keyless SSL configuration. SSL connections will no longer use the keyless server for cryptographic operations.

## Parameters

- **keyless_certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Keyless SSL Configuration response

- **result** (object, optional): 

### 4XX

Delete Keyless SSL Configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

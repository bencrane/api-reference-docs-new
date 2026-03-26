# Delete SSL Configuration

`DELETE /zones/{zone_id}/custom_certificates/{custom_certificate_id}`

Remove a SSL certificate from a zone.

## Parameters

- **custom_certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete SSL Configuration response

- **result** (object, optional): 

### 4XX

Delete SSL Configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

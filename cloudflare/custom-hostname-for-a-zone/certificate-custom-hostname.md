# Replace Custom Certificate and Custom Key In Custom Hostname

`PUT /zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}`

Replace a single custom certificate within a certificate pack that contains two bundled certificates. The replacement must adhere to the following constraints. You can only replace an RSA certificate with another RSA certificate or an ECDSA certificate with another ECDSA certificate.

## Parameters

- **custom_hostname_id** (string, required) [path]: 
- **certificate_pack_id** (string, required) [path]: 
- **certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **custom_certificate** (string, required): If a custom uploaded certificate is used.
- **custom_key** (string, required): The key for a custom uploaded certificate.

## Response

### 202

Edit Custom Certificate In a Custom Hostname response

- **result** (object, optional): 

### 4XX

Edit Custom Certificate In a Custom Hostname response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

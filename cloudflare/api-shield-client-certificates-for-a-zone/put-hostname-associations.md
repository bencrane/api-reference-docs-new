# Replace Hostname Associations

`PUT /zones/{zone_id}/certificate_authorities/hostname_associations`

Replace Hostname Associations

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **hostnames** (array, optional): 
- **mtls_certificate_id** (string, optional): The UUID for a certificate that was uploaded to the mTLS Certificate Management endpoint. If no mtls_certificate_id is given, the hostnames will be associated to your active Cloudflare Managed CA.

## Response

### 200

Replace Hostname Associations Response

- **result** (object, optional): 

### 4XX

Replace Hostname Associations Response Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

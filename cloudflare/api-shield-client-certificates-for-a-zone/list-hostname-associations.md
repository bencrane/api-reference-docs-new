# List Hostname Associations

`GET /zones/{zone_id}/certificate_authorities/hostname_associations`

List Hostname Associations

## Parameters

- **zone_id** (string, required) [path]: 
- **mtls_certificate_id** (string, optional) [query]: 

## Response

### 200

List Hostname Associations Response

- **result** (object, optional): 

### 4XX

List Hostname Associations Response Failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

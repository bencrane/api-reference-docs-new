# Re-prioritize SSL Certificates

`PUT /zones/{zone_id}/custom_certificates/prioritize`

If a zone has multiple SSL certificates, you can set the order in which they should be used during a request. The higher priority will break ties across overlapping 'legacy_custom' certificates.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **certificates** (array, required): Array of ordered certificates.

## Response

### 200

Re-prioritize SSL Certificates response

- **result** (array, optional): 

### 4XX

Re-prioritize SSL Certificates response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

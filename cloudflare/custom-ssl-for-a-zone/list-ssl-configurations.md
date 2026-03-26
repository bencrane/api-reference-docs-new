# List SSL Configurations

`GET /zones/{zone_id}/custom_certificates`

List, search, and filter all of your custom SSL certificates. The higher priority will break ties across overlapping 'legacy_custom' certificates, but 'legacy_custom' certificates will always supercede 'sni_custom' certificates.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **match** (string, optional) [query]: 
- **status** (string, optional) [query]: 

## Response

### 200

List SSL Configurations response

- **result** (array, optional): 

### 4XX

List SSL Configurations response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

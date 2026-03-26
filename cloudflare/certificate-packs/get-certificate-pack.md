# Get Certificate Pack

`GET /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}`

For a given zone, get a certificate pack.

## Parameters

- **certificate_pack_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get Certificate Pack response

- **result** (object, optional): A certificate pack with all its properties.

### 4XX

Get Certificate Pack response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

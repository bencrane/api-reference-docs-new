# Get Certificate Pack Quotas

`GET /zones/{zone_id}/ssl/certificate_packs/quota`

For a given zone, list certificate pack quotas.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Certificate Pack Quotas response

- **result** (object, optional): 

### 4XX

Get Certificate Pack Quotas response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

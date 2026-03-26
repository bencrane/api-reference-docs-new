# List Certificate Packs

`GET /zones/{zone_id}/ssl/certificate_packs`

For a given zone, list all active certificate packs.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **status** (string, optional) [query]: 
- **deploy** (string, optional) [query]: 

## Response

### 200

List Certificate Packs response

- **result** (array, optional): 

### 4XX

List Certificate Packs response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

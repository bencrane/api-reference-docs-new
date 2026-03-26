# SSL Verification Details

`GET /zones/{zone_id}/ssl/verification`

Get SSL Verification Info for a Zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **retry** (string, optional) [query]: 

## Response

### 200

SSL Verification Details response

- **result** (array, optional): 

### 4XX

SSL Verification Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

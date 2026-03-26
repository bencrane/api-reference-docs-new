# Delete Advanced Certificate Manager Certificate Pack

`DELETE /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}`

For a given zone, delete an advanced certificate pack.

## Parameters

- **certificate_pack_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Advanced Certificate Manager Certificate Pack response

- **result** (object, optional): 

### 4XX

Delete Advanced Certificate Manager Certificate Pack response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Edit SSL Certificate Pack Validation Method

`PATCH /zones/{zone_id}/ssl/verification/{certificate_pack_id}`

Edit SSL validation method for a certificate pack. A PATCH request will request an immediate validation check on any certificate, and return the updated status. If a validation method is provided, the validation will be immediately attempted using that method.

## Parameters

- **certificate_pack_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **validation_method** (string, required): Desired validation method. Values: `http`, `cname`, `txt`, `email`

## Response

### 200

Edit SSL Certificate Pack Validation Method response

- **result** (object, optional): 

### 4XX

Edit SSL Certificate Pack Validation Method response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

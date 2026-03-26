# Edit zone setting

`PATCH /zones/{zone_id}/settings/{setting_id}`

Updates a single zone setting by the identifier

## Parameters

- **zone_id** (string, required) [path]: 
- **setting_id** (string, required) [path]: 

## Request Body

One of: object, object

## Response

### 200

Edit zone setting response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful
- **result** (object, optional): 

### 4XX

Edit zone settings info response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

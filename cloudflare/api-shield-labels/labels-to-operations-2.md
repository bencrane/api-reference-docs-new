# Bulk replace label(s) on operation(s) in endpoint management

`PUT /zones/{zone_id}/api_gateway/operations/labels`

Bulk replace label(s) on operation(s) in endpoint management

## Request Body

- **managed** (object, required): Managed labels to replace for all affected operations
- **selector** (object, required): Operation IDs selector
- **user** (object, required): User labels to replace for all affected operations

## Response

### 200

Bulk replace label(s) on operation(s) in endpoint management response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Bulk replace label(s) on operation(s) in endpoint management response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

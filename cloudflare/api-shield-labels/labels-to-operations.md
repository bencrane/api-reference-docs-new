# Bulk remove label(s) on operation(s) in endpoint management

`DELETE /zones/{zone_id}/api_gateway/operations/labels`

Bulk remove label(s) on operation(s) in endpoint management

## Request Body

- **managed** (object, optional): 
- **selector** (object, required): Operation IDs selector
- **user** (object, optional): 

## Response

### 200

Bulk remove label(s) on operation(s) in endpoint management response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Bulk remove label(s) on operation(s) in endpoint management response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

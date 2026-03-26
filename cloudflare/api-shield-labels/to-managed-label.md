# Replace operation(s) attached to a managed label

`PUT /zones/{zone_id}/api_gateway/labels/managed/{name}/resources/operation`

Replace all operations(s) attached to a managed label

## Request Body

- **selector** (object, required): Operation IDs selector

## Response

### 200

Replace all operations(s) attached to a managed label response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Replace all operations(s) attached to a managed label failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

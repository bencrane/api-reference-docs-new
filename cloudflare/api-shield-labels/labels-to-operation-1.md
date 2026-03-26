# Replace label(s) on an operation in endpoint management

`PUT /zones/{zone_id}/api_gateway/operations/{operation_id}/labels`

Replace label(s) on an operation in endpoint management

## Request Body

- **managed** (array, optional): List of managed label names. Omitting this property or passing an empty array will result in all managed labels being removed from the operation
- **user** (array, optional): List of user label names. Omitting this property or passing an empty array will result in all user labels being removed from the operation

## Response

### 200

Replace label(s) on an operation in endpoint management response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Replace label(s) on an operation in endpoint management response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

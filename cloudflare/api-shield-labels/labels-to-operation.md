# Attach label(s) on an operation in endpoint management

`POST /zones/{zone_id}/api_gateway/operations/{operation_id}/labels`

Attach label(s) on an operation in endpoint management

## Request Body

- **managed** (array, optional): List of managed label names.
- **user** (array, optional): List of user label names.

## Response

### 200

Attach label(s) on an operation in endpoint management response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Attach label(s) on an operation in endpoint management response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Patch discovered operation

`PATCH /zones/{zone_id}/api_gateway/discovery/operations/{operation_id}`

Update the `state` on a discovered operation

## Request Body

- **state** (object, optional): 

## Response

### 200

Patch discovered operation response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch discovered operation response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

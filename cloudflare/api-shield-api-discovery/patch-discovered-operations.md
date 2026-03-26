# Patch discovered operations

`PATCH /zones/{zone_id}/api_gateway/discovery/operations`

Update the `state` on one or more discovered operations

## Request Body

_Empty object_

## Response

### 200

Patch discovered operations response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch discovered operations response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Update a tag

`PUT /accounts/{account_id}/access/tags/{tag_name}`

Update a tag

## Parameters

- **account_id** (string, required) [path]: 
- **tag_name** (string, required) [path]: 

## Request Body

- **created_at** (object, optional): 
- **name** (string, required): The name of the tag
- **updated_at** (object, optional): 

## Response

### 200

Update a tag response

_Empty object_

### 4XX

Update a tag response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

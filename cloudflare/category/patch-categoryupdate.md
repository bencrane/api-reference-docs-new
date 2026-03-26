# Updates a category

`PATCH /accounts/{account_id}/cloudforce-one/events/categories/{category_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **category_id** (string, required) [path]: Category UUID.

## Request Body

- **killChain** (number, optional): 
- **mitreAttack** (array, optional): 
- **mitreCapec** (array, optional): 
- **name** (string, optional): 
- **shortname** (string, optional): 

## Response

### 200

Returns the updated category.

- **killChain** (number): 
- **mitreAttack** (array): 
- **mitreCapec** (array): 
- **name** (string): 
- **shortname** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

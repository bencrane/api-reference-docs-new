# Reads a category

`GET /accounts/{account_id}/cloudforce-one/events/categories/{category_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **category_id** (string, required) [path]: Category UUID.

## Response

### 200

Returns a category.

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

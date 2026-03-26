# Creates a new category

`POST /accounts/{account_id}/cloudforce-one/events/categories/create`



## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **killChain** (number, required): 
- **mitreAttack** (array, optional): 
- **mitreCapec** (array, optional): 
- **name** (string, required): 
- **shortname** (string, optional): 

## Response

### 200

Returns the created category.

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

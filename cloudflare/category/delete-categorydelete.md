# Deletes a category

`DELETE /accounts/{account_id}/cloudforce-one/events/categories/{category_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **category_id** (string, required) [path]: Category UUID.

## Response

### 200

Returns the uuid of the deleted category.

- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

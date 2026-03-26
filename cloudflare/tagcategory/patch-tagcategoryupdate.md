# Updates a tag category (SoT)

`PATCH /accounts/{account_id}/cloudforce-one/events/tags/categories/{category_uuid}`

Updates a Source-of-Truth tag category by UUID.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **category_uuid** (string, required) [path]: Tag Category UUID.

## Request Body

- **description** (string, optional): 
- **name** (string, optional): 

## Response

### 200

Returns the updated tag category.

- **createdAt** (string): 
- **description** (string): 
- **name** (string): 
- **updatedAt** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 409

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

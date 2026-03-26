# Deletes a tag category (SoT)

`DELETE /accounts/{account_id}/cloudforce-one/events/tags/categories/{category_uuid}`

Deletes a Source-of-Truth tag category by UUID.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **category_uuid** (string, required) [path]: Tag Category UUID.

## Response

### 200

Returns the uuid of the deleted tag category.

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

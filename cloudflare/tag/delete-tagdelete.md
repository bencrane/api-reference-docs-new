# Deletes a tag (SoT)

`DELETE /accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}`

Deletes a Source-of-Truth tag by UUID.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **tag_uuid** (string, required) [path]: Tag UUID.

## Response

### 200

Returns the uuid of the deleted tag.

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

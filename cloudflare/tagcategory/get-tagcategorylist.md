# Lists all tag categories (SoT)

`GET /accounts/{account_id}/cloudforce-one/events/tags/categories`

Returns all Source-of-Truth tag categories for an account.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **search** (string, optional) [query]: 

## Response

### 200

Returns a list of tag categories.

- **categories** (array): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

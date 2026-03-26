# Lists all tags (SoT)

`GET /accounts/{account_id}/cloudforce-one/events/tags`

Returns all Source-of-Truth tags for an account.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **page** (number, optional) [query]: 
- **pageSize** (number, optional) [query]: 
- **search** (string, optional) [query]: 
- **categoryUuid** (string, optional) [query]: 

## Response

### 200

Returns a paginated list of tags.

- **pagination** (object): 
- **tags** (array): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

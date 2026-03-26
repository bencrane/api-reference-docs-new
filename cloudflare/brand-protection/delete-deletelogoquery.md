# Delete logo query

`DELETE /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries/{query_id}`

Delete a saved brand protection logo query. Returns 404 if the query ID doesn't exist.

## Parameters

- **account_id** (string, required) [path]: 
- **query_id** (string, required) [path]: 

## Response

### 200

Logo query deleted successfully

- **message** (string): 
- **success** (boolean):

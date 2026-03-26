# Delete Scripts in Namespace

`DELETE /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts`

Delete multiple scripts from a Workers for Platforms namespace based on optional tag filters.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **tags** (string, optional) [query]: Filter scripts by tags before deletion. Format: comma-separated list of tag:allowed pairs where allowed is 'yes' or 'no'.
- **limit** (integer, optional) [query]: Limit the number of scripts to delete.

## Response

### 200

Delete scripts in namespace response.

- **deleted** (array): 
- **deleted_count** (integer): 
- **has_more** (boolean): 

### 4XX

Delete scripts in namespace response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

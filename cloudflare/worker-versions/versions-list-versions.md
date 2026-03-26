# List Versions

`GET /accounts/{account_id}/workers/scripts/{script_name}/versions`

List of Worker Versions. The first version in the list is the latest version.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **deployable** (boolean, optional) [query]: Only return versions that can be used in a deployment. Ignores pagination.
- **page** (integer, optional) [query]: Current page.
- **per_page** (integer, optional) [query]: Items per-page.

## Response

### 200

List Versions response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

List Versions response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

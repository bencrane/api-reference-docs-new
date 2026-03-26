# List namespaces in catalog

`GET /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces`

Returns a list of namespaces in the specified R2 catalog.
Supports hierarchical filtering and pagination for efficient traversal
of large namespace hierarchies.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name.
- **page_token** (string, optional) [query]: Opaque pagination token from a previous response.
Use this to fetch the next page of results.

- **page_size** (integer, optional) [query]: Maximum number of namespaces to return per page.
Defaults to 100, maximum 1000.

- **parent** (string, optional) [query]: Parent namespace to filter by. Only returns direct children of this namespace.
For nested namespaces, use %1F as separator (e.g., "bronze%1Fanalytics").
Omit this parameter to list top-level namespaces.

- **return_uuids** (boolean, optional) [query]: Whether to include namespace UUIDs in the response.
Set to true to receive the namespace_uuids array.

- **return_details** (boolean, optional) [query]: Whether to include additional metadata (timestamps).
When true, response includes created_at and updated_at arrays.


## Response

### 200

List of namespaces retrieved successfully.

- **errors** (array, optional): Contains errors if the API call was unsuccessful.
- **messages** (array, optional): Contains informational messages.
- **success** (boolean, optional): Indicates whether the API call was successful.
- **result** (object, optional): Contains the list of namespaces with optional pagination.

### 400

Bad request (e.g., invalid page_size, malformed parent namespace).

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 401

Authentication failed.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 403

Forbidden.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 404

Catalog not found.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal server error.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):

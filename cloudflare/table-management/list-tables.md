# List tables in namespace

`GET /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables`

Returns a list of tables in the specified namespace within an R2 catalog.
Supports pagination for efficient traversal of large table collections.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name.
- **namespace** (string, required) [path]: The namespace identifier.
For nested namespaces, use %1F as separator (e.g., "bronze%1Fanalytics").

- **page_token** (string, optional) [query]: Opaque pagination token from a previous response.
Use this to fetch the next page of results.

- **page_size** (integer, optional) [query]: Maximum number of tables to return per page.
Defaults to 100, maximum 1000.

- **return_uuids** (boolean, optional) [query]: Whether to include table UUIDs in the response.
Set to true to receive the table_uuids array.

- **return_details** (boolean, optional) [query]: Whether to include additional metadata (timestamps, locations).
When true, response includes created_at, updated_at, metadata_locations, and locations arrays.


## Response

### 200

List of tables retrieved successfully.

- **errors** (array, optional): Contains errors if the API call was unsuccessful.
- **messages** (array, optional): Contains informational messages.
- **success** (boolean, optional): Indicates whether the API call was successful.
- **result** (object, optional): Contains the list of tables with optional pagination.

### 400

Bad request (e.g., invalid page_size, malformed namespace).

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

Catalog or namespace not found.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal server error.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):

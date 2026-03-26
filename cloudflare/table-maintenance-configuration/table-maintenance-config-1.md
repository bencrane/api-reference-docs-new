# Update table maintenance configuration

`POST /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs`

Update the maintenance configuration for a specific table. This allows you to
enable or disable compaction and adjust target file sizes for optimization.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name.
- **namespace** (string, required) [path]: The namespace identifier (use %1F as separator for nested namespaces).
- **table_name** (string, required) [path]: The table name.

## Request Body

- **compaction** (object, optional): Updates compaction configuration (all fields optional).
- **snapshot_expiration** (object, optional): Updates snapshot expiration configuration (all fields optional).

## Response

### 200

Table maintenance configuration updated successfully.

- **errors** (array, optional): Contains errors if the API call was unsuccessful.
- **messages** (array, optional): Contains informational messages.
- **success** (boolean, optional): Indicates whether the API call was successful.
- **result** (object, optional): Configures maintenance for the table.

### 400

Bad request.

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

Table not found.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal server error.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):

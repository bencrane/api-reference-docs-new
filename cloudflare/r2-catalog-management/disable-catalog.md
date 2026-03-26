# Disable R2 catalog

`POST /accounts/{account_id}/r2-catalog/{bucket_name}/disable`

Disable an R2 bucket as a catalog. This operation deactivates the catalog
but preserves existing metadata and data files. The catalog can be
re-enabled later.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name to disable as catalog.

## Response

### 204

Catalog disabled successfully.

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

Catalog not found.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal server error.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):

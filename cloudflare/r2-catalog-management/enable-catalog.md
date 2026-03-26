# Enable R2 bucket as a catalog

`POST /accounts/{account_id}/r2-catalog/{bucket_name}/enable`

Enable an R2 bucket as an Apache Iceberg catalog. This operation creates
the necessary catalog infrastructure and activates the bucket for storing
Iceberg metadata and data files.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name to enable as catalog.

## Response

### 200

Catalog enabled successfully.

- **errors** (array, optional): Contains errors if the API call was unsuccessful.
- **messages** (array, optional): Contains informational messages.
- **success** (boolean, optional): Indicates whether the API call was successful.
- **result** (object, optional): Contains response from activating an R2 bucket as a catalog.

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

### 409

Catalog already enabled.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal server error.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):

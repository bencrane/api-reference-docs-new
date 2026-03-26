# Store catalog credentials

`POST /accounts/{account_id}/r2-catalog/{bucket_name}/credential`

Store authentication credentials for a catalog. These credentials are used
to authenticate with R2 storage when performing catalog operations.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name.

## Request Body

- **token** (string, required): Provides the Cloudflare API token for accessing R2.

## Response

### 200

Credentials stored successfully.

- **errors** (array, optional): Contains errors if the API call was unsuccessful.
- **messages** (array, optional): Contains informational messages.
- **success** (boolean, optional): Indicates whether the API call was successful.
- **result** (object, optional): 

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

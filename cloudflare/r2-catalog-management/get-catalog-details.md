# Get R2 catalog details

`GET /accounts/{account_id}/r2-catalog/{bucket_name}`

Retrieve detailed information about a specific R2 catalog by bucket name.
Returns catalog status, maintenance configuration, and credential status.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **bucket_name** (string, required) [path]: Specifies the R2 bucket name.

## Response

### 200

R2 catalog details.

- **errors** (array, optional): Contains errors if the API call was unsuccessful.
- **messages** (array, optional): Contains informational messages.
- **success** (boolean, optional): Indicates whether the API call was successful.
- **result** (object, optional): Contains R2 Data Catalog information.

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

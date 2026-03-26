# Creates a new tag category (SoT)

`POST /accounts/{account_id}/cloudforce-one/events/tags/categories/create`

Creates a new Source-of-Truth tag category for an account.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **description** (string, optional): 
- **name** (string, required): 

## Response

### 200

Returns the created tag category.

- **createdAt** (string): 
- **description** (string): 
- **name** (string): 
- **updatedAt** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 409

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

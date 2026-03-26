# Creates a dataset

`POST /accounts/{account_id}/cloudforce-one/events/dataset/create`



## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **isPublic** (boolean, required): If true, then anyone can search the dataset. If false, then its limited to the account.
- **name** (string, required): Used to describe the dataset within the account context.

## Response

### 200

Returns dataset information.

- **isPublic** (boolean): 
- **name** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

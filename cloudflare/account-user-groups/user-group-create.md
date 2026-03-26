# Create User Group

`POST /accounts/{account_id}/iam/user_groups`

Create a new user group under the specified account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): Name of the User group.
- **policies** (array, required): Policies attached to the User group

## Response

### 200

Add User Group response

- **result** (object, optional): A group of policies resources.

### 4XX

Add User Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

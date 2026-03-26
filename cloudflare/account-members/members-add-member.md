# Add Member

`POST /accounts/{account_id}/members`

Add a user to the list of members for this account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

One of: Add Member with Account Roles, Add Member with Policies

## Response

### 200

Add Member response

- **result** (object, optional): 

### 4XX

Add Member response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

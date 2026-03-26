# Update Member

`PUT /accounts/{account_id}/members/{member_id}`

Modify an account member.

## Parameters

- **member_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

One of: Update Member with Account Roles, Update Member with Policies

## Response

### 200

Update Member response

- **result** (object, optional): 

### 4XX

Update Member response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

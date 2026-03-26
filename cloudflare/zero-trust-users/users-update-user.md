# Update a user

`PUT /accounts/{account_id}/access/users/{user_id}`

Updates a specific user's name for an account. Requires the user's current email as confirmation (email cannot be changed).

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **email** (string, required): The email of the user.
- **name** (string, required): The name of the user.

## Response

### 200

Update user response

_Empty object_

### 4XX

Update user response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

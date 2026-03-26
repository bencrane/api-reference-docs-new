# Create a user

`POST /accounts/{account_id}/access/users`

Creates a new user.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **email** (string, required): The email of the user.
- **name** (string, optional): The name of the user.

## Response

### 201

Create user response

_Empty object_

### 4XX

Create user response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

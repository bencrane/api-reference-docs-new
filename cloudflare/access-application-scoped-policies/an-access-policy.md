# Create an Access application policy

`POST /accounts/{account_id}/access/apps/{app_id}/policies`

Creates a policy applying exclusive to a single application that defines the users or groups who can reach it. We recommend creating a reusable policy instead and subsequently referencing its ID in the application's 'policies' array.

## Parameters

- **app_id** (string, required) [path]: The application ID.
- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 201

Create an Access application policy response.

_Empty object_

### 4XX

Create an Access application policy response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

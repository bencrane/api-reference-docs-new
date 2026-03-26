# Start Access policy test

`POST /accounts/{account_id}/access/policy-tests`

Starts an Access policy test.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **policies** (array, optional): 

## Response

### 200

Start Access policy test response.

_Empty object_

### 400

Start Access policy test response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Create Silences

`POST /accounts/{account_id}/alerting/v3/silences`

Creates a new silence for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Create Silences response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful

### 4XX

Create Silences response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

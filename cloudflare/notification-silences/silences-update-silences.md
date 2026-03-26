# Update Silences

`PUT /accounts/{account_id}/alerting/v3/silences`

Updates existing silences for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Update Silences response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (array, optional): 

### 4XX

Update Silences response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`

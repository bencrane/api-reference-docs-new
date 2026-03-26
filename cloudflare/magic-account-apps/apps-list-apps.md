# List Apps

`GET /accounts/{account_id}/magic/apps`

Lists Apps associated with an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Apps response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

List Apps response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

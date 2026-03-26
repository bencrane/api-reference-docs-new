# Delete Account App

`DELETE /accounts/{account_id}/magic/apps/{account_app_id}`

Deletes specific Account App.

## Parameters

- **account_id** (string, required) [path]: 
- **account_app_id** (string, required) [path]: 

## Response

### 200

Delete App response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Custom app defined for an account.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete App response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

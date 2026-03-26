# Fetch Worker Account Settings

`GET /accounts/{account_id}/workers/account-settings`

Fetches Worker account settings for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Fetch Worker Account Settings response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Fetch Worker Account Settings response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

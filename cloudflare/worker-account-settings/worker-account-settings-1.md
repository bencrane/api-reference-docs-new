# Create Worker Account Settings

`PUT /accounts/{account_id}/workers/account-settings`

Creates Worker account settings for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **default_usage_model** (string, optional): 
- **green_compute** (boolean, optional): 

## Response

### 200

Create Worker Account Settings response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create Worker Account Settings response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

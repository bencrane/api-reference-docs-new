# Returns account commands usage, quota, and reset time

`GET /accounts/{account_id}/dex/commands/quota`

Retrieves the current quota usage and limits for device commands within a specific account, including the time when the quota will reset

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path

## Response

### 200

Get commands quota response

- **result** (object, optional): 

### 4XX

Get commands quota failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

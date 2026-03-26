# List all profiles

`GET /accounts/{account_id}/dlp/profiles`

Lists all DLP profiles in an account.

## Parameters

- **all** (boolean, optional) [query]: Return all profiles, including those that current account does not have access to.
- **account_id** (string, required) [path]: 

## Response

### 200

List all profiles response.

- **result** (array, optional): 

### 4XX

List all profiles failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

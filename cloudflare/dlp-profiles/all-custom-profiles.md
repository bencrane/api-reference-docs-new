# List all custom profiles

`GET /accounts/{account_id}/dlp/profiles/custom`

Lists all DLP custom profiles in an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List all custom profiles response.

- **result** (array, optional): 

### 4XX

List all profiles failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

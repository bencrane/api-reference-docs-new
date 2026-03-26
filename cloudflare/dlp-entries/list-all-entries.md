# List all entries

`GET /accounts/{account_id}/dlp/entries`

Lists all DLP entries in an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List all entries response.

- **result** (array, optional): 

### 4XX

List all entries failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

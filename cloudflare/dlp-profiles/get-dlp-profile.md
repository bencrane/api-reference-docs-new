# Get DLP Profile

`GET /accounts/{account_id}/dlp/profiles/{profile_id}`

Fetches a DLP profile by ID.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Response

### 200

Get profile response.

- **result** (object, optional): 

### 4XX

Get profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

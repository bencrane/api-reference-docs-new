# Get custom profile

`GET /accounts/{account_id}/dlp/profiles/custom/{profile_id}`

Fetches a custom DLP profile by id.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Response

### 200

Custom profile response.

- **result** (object, optional): 

### 4XX

Custom profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

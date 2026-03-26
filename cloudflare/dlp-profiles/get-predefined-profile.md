# Get predefined profile

`GET /accounts/{account_id}/dlp/profiles/predefined/{profile_id}`

Fetches a predefined DLP profile by id.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Response

### 200

Predefined profile response.

- **result** (object, optional): 

### 4XX

Predefined profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

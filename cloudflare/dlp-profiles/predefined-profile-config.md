# Get predefined profile config

`GET /accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config`

This is similar to `get_predefined` but only returns entries that are enabled.
This is needed for our terraform API
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

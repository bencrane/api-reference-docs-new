# Update predefined profile config

`PUT /accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config`

This is similar to `update_predefined` but only returns entries that are enabled.
This is needed for our terraform API
Updates a DLP predefined profile. Only supports enabling/disabling entries.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Request Body

- **ai_context_enabled** (boolean, optional): 
- **allowed_match_count** (integer, optional): 
- **confidence_threshold** (string, optional): 
- **enabled_entries** (array, optional): 
- **entries** (array, optional): 
- **ocr_enabled** (boolean, optional): 

## Response

### 200

Update predefined profile response.

- **result** (object, optional): 

### 4XX

Update predefined profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

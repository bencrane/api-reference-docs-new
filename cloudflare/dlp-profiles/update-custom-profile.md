# Update custom profile

`PUT /accounts/{account_id}/dlp/profiles/custom/{profile_id}`

Updates a DLP custom profile.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Request Body

- **ai_context_enabled** (boolean, optional): 
- **allowed_match_count** (integer, optional): 
- **confidence_threshold** (string, optional): 
- **context_awareness** (object, optional): Scan the context of predefined entries to only return matches surrounded by keywords.
- **data_classes** (array, optional): Data class IDs to associate with the profile. If omitted, existing associations are unchanged.
- **data_tags** (array, optional): Data tag IDs to associate with the profile. If omitted, existing associations are unchanged.
- **description** (string, optional): The description of the profile.
- **entries** (array, optional): Custom entries from this profile.
If this field is omitted, entries owned by this profile will not be changed.
- **name** (string, required): 
- **ocr_enabled** (boolean, optional): 
- **sensitivity_levels** (array, optional): Sensitivity levels to associate with the profile. If omitted, existing associations are unchanged.
- **shared_entries** (array, optional): Other entries, e.g. predefined or integration.

## Response

### 200

Update custom profile response.

- **result** (object, optional): 

### 4XX

Update custom profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Create custom profile

`POST /accounts/{account_id}/dlp/profiles/custom`

Creates a DLP custom profile.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ai_context_enabled** (boolean, optional): 
- **allowed_match_count** (integer, optional): Related DLP policies will trigger when the match count exceeds the number set.
- **confidence_threshold** (string, optional): 
- **context_awareness** (object, optional): Scan the context of predefined entries to only return matches surrounded by keywords.
- **data_classes** (array, optional): Data class IDs to associate with the profile.
- **data_tags** (array, optional): Data tag IDs to associate with the profile.
- **description** (string, optional): The description of the profile.
- **entries** (array, optional): 
- **name** (string, required): 
- **ocr_enabled** (boolean, optional): 
- **sensitivity_levels** (array, optional): Sensitivity levels to associate with the profile as (group_id, level_id) tuples.
- **shared_entries** (array, optional): Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).

## Response

### 200

New custom profile response.

- **result** (object, optional): 

### 4XX

New custom profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

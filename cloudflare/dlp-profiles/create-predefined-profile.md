# Create predefined profile

`POST /accounts/{account_id}/dlp/profiles/predefined`

Creates a DLP predefined profile. Only supports enabling/disabling entries.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ai_context_enabled** (boolean, optional): 
- **allowed_match_count** (integer, optional): 
- **confidence_threshold** (string, optional): 
- **context_awareness** (object, optional): Scan the context of predefined entries to only return matches surrounded by keywords.
- **entries** (array, optional): 
- **ocr_enabled** (boolean, optional): 
- **profile_id** (string, optional): 

## Response

### 200

Create predefined profile response.

- **result** (object, optional): 

### 4XX

Create predefined profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

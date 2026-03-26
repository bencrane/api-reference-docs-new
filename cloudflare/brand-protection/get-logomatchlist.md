# List logo matches

`GET /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/matches`

Get paginated list of logo matches for a specific brand protection logo query

## Parameters

- **account_id** (string, required) [path]: 
- **offset** (string, optional) [query]: 
- **limit** (string, optional) [query]: 
- **query_id** (string, required) [query]: 
- **download** (string, optional) [query]: 
- **orderBy** (string, optional) [query]: 
- **order** (string, optional) [query]: 

## Response

### 200

Successfully retrieved logo matches

- **matches** (array): 
- **total** (integer):

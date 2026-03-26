# List saved query matches

`GET /accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/matches`

Get paginated list of domain matches for a specific brand protection query

## Parameters

- **account_id** (string, required) [path]: 
- **offset** (string, optional) [query]: 
- **limit** (string, optional) [query]: 
- **query_id** (string, required) [query]: 
- **include_domain_id** (string, optional) [query]: 
- **include_dismissed** (string, optional) [query]: 
- **orderBy** (string, optional) [query]: 
- **order** (string, optional) [query]: 

## Response

### 200

Successfully retrieved query matches

- **matches** (array): 
- **total** (integer):

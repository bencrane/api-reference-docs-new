# Retrieve all labels

`GET /zones/{zone_id}/api_gateway/labels`

Retrieve all labels

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **source** (string, optional) [query]: Filter for labels with source
- **filter** (string, optional) [query]: Filter for labels where the name or description matches using substring match
- **with_mapped_resource_counts** (boolean, optional) [query]: Include `mapped_resources` for each label

## Response

### 200

Retrieve all labels response

- **result** (array, optional): 

### 4XX

Retrieve all labels response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

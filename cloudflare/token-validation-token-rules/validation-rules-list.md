# List token validation rules

`GET /zones/{zone_id}/token_validation/rules`

List token validation rules

## Parameters

- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **page** (integer, optional) [query]: Page number of paginated results.
- **token_configuration** (array, optional) [query]: Select rules using any of these token configurations.
- **action** (string, optional) [query]: 
- **enabled** (string, optional) [query]: 
- **id** (string, optional) [query]: Select rules with these IDs.
- **rule_id** (string, optional) [query]: Select rules with these IDs.
- **host** (string, optional) [query]: Select rules with this host in `include`.
- **hostname** (string, optional) [query]: Select rules with this host in `include`.

## Response

### 200

OK

- **result** (array, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

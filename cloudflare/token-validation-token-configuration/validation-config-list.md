# List token validation configurations

`GET /zones/{zone_id}/token_validation/config`

Lists all token validation configurations for this zone

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.

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

# Retrieve information about all operations on a zone

`GET /zones/{zone_id}/api_gateway/operations`

Lists all API operations tracked by API Shield for a zone with pagination. Returns operation details including method, path, and feature configurations.

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **host** (array, optional) [query]: 
- **method** (array, optional) [query]: 
- **endpoint** (string, optional) [query]: 
- **feature** (array, optional) [query]: Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.

## Response

### 200

Retrieve information about all operations on a zone response

- **result** (array, optional): 

### 4XX

Retrieve information about all operations on a zone response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

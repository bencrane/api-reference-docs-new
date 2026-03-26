# Retrieve discovered operations on a zone

`GET /zones/{zone_id}/api_gateway/discovery/operations`

Retrieve the most up to date view of discovered operations

## Parameters

- **page** (integer, optional) [query]: Page number of paginated results.
- **per_page** (integer, optional) [query]: Maximum number of results per page.
- **host** (array, optional) [query]: 
- **method** (array, optional) [query]: 
- **endpoint** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **order** (string, optional) [query]: 
- **diff** (boolean, optional) [query]: 
- **origin** (string, optional) [query]: Filter results to only include discovery results sourced from a particular discovery engine
  * `ML` - Discovered operations that were sourced using ML API Discovery
  * `SessionIdentifier` - Discovered operations that were sourced using Session Identifier API Discovery

- **state** (string, optional) [query]: Filter results to only include discovery results in a particular state. States are as follows
  * `review` - Discovered operations that are not saved into API Shield Endpoint Management
  * `saved` - Discovered operations that are already saved into API Shield Endpoint Management
  * `ignored` - Discovered operations that have been marked as ignored


## Response

### 200

Retrieve discovered operations on a zone response

- **result** (array, optional): 

### 4XX

Retrieve discovered operations on a zone response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

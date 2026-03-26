# Search for locations, ASes, reports, and more

`GET /radar/search/global`

Searches for locations, autonomous systems, reports, bots, certificate logs, certificate authorities, industries and verticals. Location names can be localized by sending an `Accept-Language` HTTP header with a BCP 47 language tag (e.g., `Accept-Language: pt-PT`). The full quality-value chain is supported (e.g., `pt-PT,pt;q=0.9,en;q=0.8`).

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **limitPerGroup** (number, optional) [query]: Limits the number of objects per search category.
- **query** (string, required) [query]: String used to perform the search operation.
- **include** (array, optional) [query]: Search types included in results.
- **exclude** (array, optional) [query]: Search types excluded from results.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

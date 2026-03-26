# Get domain rank details

`GET /radar/ranking/domain/{domain}`

Retrieves domain rank details. Cloudflare provides an ordered rank for the top 100 domains, but for the remainder it only provides ranking buckets like top 200 thousand, top one million, etc.. These are available through Radar datasets endpoints.

## Parameters

- **domain** (string, required) [path]: Domain name.
- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **rankingType** (string, optional) [query]: The ranking type.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **includeTopLocations** (boolean, optional) [query]: Includes top locations in the response.
- **date** (array, optional) [query]: Filters results by the specified array of dates.
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

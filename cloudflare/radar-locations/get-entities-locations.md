# List locations

`GET /radar/entities/locations`

Retrieves a list of locations.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **location** (string, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 location codes.
- **region** (string, optional) [query]: Filters results by region.
- **subregion** (string, optional) [query]: Filters results by subregion.
- **continent** (string, optional) [query]: Filters results by continent code.
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

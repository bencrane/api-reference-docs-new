# List Geolocations

`GET /radar/geolocations`

Retrieves a list of geolocations. Geolocation names can be localized by sending an `Accept-Language` HTTP header with a BCP 47 language tag (e.g., `Accept-Language: pt-PT`). The full quality-value chain is supported (e.g., `pt-PT,pt;q=0.9,en;q=0.8`).

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **geoId** (string, optional) [query]: Filters results by geolocation. Specify a comma-separated list of GeoNames IDs.
- **location** (string, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 location codes.
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

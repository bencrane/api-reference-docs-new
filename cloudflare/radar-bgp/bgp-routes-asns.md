# List ASes from global routing tables

`GET /radar/bgp/routes/ases`

Retrieves all ASes in the current global routing tables with routing statistics.

## Parameters

- **location** (string, optional) [query]: Filters results by location. Specify an alpha-2 location code.
- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **sortBy** (string, optional) [query]: Sorts results by the specified field.
- **sortOrder** (string, optional) [query]: Sort order.
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

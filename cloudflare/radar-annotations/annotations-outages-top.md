# Get the number of outages by location

`GET /radar/annotations/outages/locations`

Retrieves the number of outages by location.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **dateRange** (string, optional) [query]: Filters results by date range.
- **dateStart** (string, optional) [query]: Start of the date range (inclusive).
- **dateEnd** (string, optional) [query]: End of the date range (inclusive).
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

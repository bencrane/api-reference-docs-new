# List autonomous systems

`GET /radar/entities/asns`

Retrieves a list of autonomous systems.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **asn** (string, optional) [query]: Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
- **location** (string, optional) [query]: Filters results by location. Specify an alpha-2 location code.
- **orderBy** (string, optional) [query]: Specifies the metric to order the ASNs by.
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

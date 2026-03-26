# Get top ASes by prefix count

`GET /radar/bgp/top/ases/prefixes`

Retrieves the full list of autonomous systems on the global routing table ordered by announced prefixes count. The data comes from public BGP MRT data archives and updates every 2 hours.

## Parameters

- **country** (string, optional) [query]: Alpha-2 country code.
- **limit** (integer, optional) [query]: Maximum number of ASes to return.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

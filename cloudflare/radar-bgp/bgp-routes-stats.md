# Get BGP routing table stats 

`GET /radar/bgp/routes/stats`

Retrieves the BGP routing table stats.

## Parameters

- **asn** (integer, optional) [query]: Filters results by Autonomous System. Specify a single Autonomous System Number (ASN) as integer.
- **location** (string, optional) [query]: Filters results by location. Specify an alpha-2 location code.
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

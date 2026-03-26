# Get ASPA changes over time

`GET /radar/bgp/rpki/aspa/changes`

Retrieves ASPA (Autonomous System Provider Authorization) changes over time. Returns daily aggregated changes including additions, removals, and modifications of ASPA objects.

## Parameters

- **dateStart** (string, optional) [query]: Start of the date range (inclusive).
- **dateEnd** (string, optional) [query]: End of the date range (inclusive).
- **asn** (integer, optional) [query]: Filter changes involving this ASN (as customer or provider).
- **includeAsnInfo** (boolean, optional) [query]: Include ASN metadata (name, country) in response.
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

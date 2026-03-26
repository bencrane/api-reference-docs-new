# Get prefix-to-ASN mapping

`GET /radar/bgp/routes/pfx2as`

Retrieves the prefix-to-ASN mapping from global routing tables.

## Parameters

- **prefix** (string, optional) [query]: 
- **origin** (integer, optional) [query]: Lookup prefixes originated by the given ASN.
- **rpkiStatus** (string, optional) [query]: Return only results with matching rpki status: valid, invalid or unknown.
- **longestPrefixMatch** (boolean, optional) [query]: Return only results with the longest prefix match for the given prefix. For example, specify a /32 prefix to lookup the origin ASN for an IPv4 address.
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

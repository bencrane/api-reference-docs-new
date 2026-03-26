# Get Multi-Origin AS (MOAS) prefixes

`GET /radar/bgp/routes/moas`

Retrieves all Multi-Origin AS (MOAS) prefixes in the global routing tables.

## Parameters

- **origin** (integer, optional) [query]: Lookup MOASes originated by the given ASN.
- **prefix** (string, optional) [query]: 
- **invalid_only** (boolean, optional) [query]: Lookup only RPKI invalid MOASes.
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

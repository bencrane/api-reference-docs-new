# Get ASPA objects snapshot

`GET /radar/bgp/rpki/aspa/snapshot`

Retrieves current or historical ASPA (Autonomous System Provider Authorization) objects. ASPA objects define which ASNs are authorized upstream providers for a customer ASN.

## Parameters

- **customerAsn** (integer, optional) [query]: Filter by customer ASN (the ASN publishing the ASPA object).
- **providerAsn** (integer, optional) [query]: Filter by provider ASN (an authorized upstream provider in ASPA objects).
- **date** (string, optional) [query]: Filters results by the specified datetime (ISO 8601).
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

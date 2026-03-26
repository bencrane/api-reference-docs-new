# Get AS-level relationships by ASN

`GET /radar/entities/asns/{asn}/rel`

Retrieves AS-level relationship for given networks.

## Parameters

- **asn** (integer, required) [path]: Retrieves all ASNs with provider-customer or peering relationships with the given ASN.
- **asn2** (integer, optional) [query]: Retrieves the AS relationship of ASN2 with respect to the given ASN.
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

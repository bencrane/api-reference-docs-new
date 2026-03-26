# Get IRR AS-SETs that an AS is a member of

`GET /radar/entities/asns/{asn}/as_set`

Retrieves Internet Routing Registry AS-SETs that an AS is a member of.

## Parameters

- **asn** (integer, required) [path]: Retrieves all AS-SETs that the given AS is a member of.
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

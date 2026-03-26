# Get Origin details

`GET /radar/origins/{slug}`

Retrieves the requested origin information with its regions.

## Parameters

- **slug** (string, required) [path]: Origin slug.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

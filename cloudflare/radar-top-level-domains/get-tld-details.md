# Get TLD details

`GET /radar/tlds/{tld}`

Retrieves the requested TLD information.

## Parameters

- **tld** (string, required) [path]: Top-level domain.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

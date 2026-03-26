# List TLDs

`GET /radar/tlds`

Retrieves a list of TLDs.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **tldManager** (string, optional) [query]: Filters results by TLD manager.
- **tldType** (string, optional) [query]: Filters results by TLD type.
- **tld** (string, optional) [query]: Filters results by top-level domain. Specify a comma-separated list of TLDs.
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

# Get bot details

`GET /radar/bots/{bot_slug}`

Retrieves the requested bot information.

## Parameters

- **bot_slug** (string, required) [path]: Bot slug.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

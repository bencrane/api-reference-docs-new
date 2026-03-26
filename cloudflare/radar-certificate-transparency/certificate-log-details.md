# Get certificate log details

`GET /radar/ct/logs/{log_slug}`

Retrieves the requested certificate log information.

## Parameters

- **log_slug** (string, required) [path]: Certificate log slug.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

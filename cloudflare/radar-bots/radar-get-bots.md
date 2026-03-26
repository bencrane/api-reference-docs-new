# List bots

`GET /radar/bots`

Retrieves a list of bots.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **botCategory** (string, optional) [query]: Filters results by bot category.
- **botOperator** (string, optional) [query]: Filters results by bot operator.
- **kind** (string, optional) [query]: Filters results by bot kind.
- **botVerificationStatus** (string, optional) [query]: Filters results by bot verification status.
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

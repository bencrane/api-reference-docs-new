# List Internet services categories

`GET /radar/ranking/internet_services/categories`

Retrieves the list of Internet services categories.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **date** (array, optional) [query]: Filters results by the specified array of dates.
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

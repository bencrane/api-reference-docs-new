# Get top domain categories by robots.txt files parsed

`GET /radar/robots_txt/top/domain_categories`

Retrieves the top domain categories by the number of robots.txt files parsed.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **userAgentCategory** (string, optional) [query]: Filters results by user agent category.
- **date** (array, optional) [query]: Filters results by the specified array of dates.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

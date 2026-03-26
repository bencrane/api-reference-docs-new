# Get top user agents on robots.txt files

`GET /radar/robots_txt/top/user_agents/directive`

Retrieves the top user agents on robots.txt files.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **userAgentCategory** (string, optional) [query]: Filters results by user agent category.
- **date** (array, optional) [query]: Filters results by the specified array of dates.
- **domainCategory** (array, optional) [query]: Filters results by domain category.
- **directive** (string, optional) [query]: Filters results by robots.txt directive.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

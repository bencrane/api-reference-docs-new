# Get domains rank time series

`GET /radar/ranking/timeseries_groups`

Retrieves domains rank over time.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **rankingType** (string, optional) [query]: The ranking type.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 location codes.
- **domains** (array, optional) [query]: Filters results by domain name. Specify a comma-separated list of domain names.
- **domainCategory** (array, optional) [query]: Filters results by domain category.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
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

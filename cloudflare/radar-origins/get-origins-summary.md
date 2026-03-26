# Get origin metrics distribution by dimension

`GET /radar/origins/summary/{dimension}`

Retrieves an aggregated summary of origin metrics grouped by the specified dimension.

## Parameters

- **dimension** (string, required) [path]: Specifies the origin attribute by which to group the results.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **limitPerGroup** (integer, optional) [query]: Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.
- **origin** (array, required) [query]: Filters results by origin.
- **metric** (string, required) [query]: Specifies the metric to retrieve.
- **region** (array, optional) [query]: Filters results by origin region.
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

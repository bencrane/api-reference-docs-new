# Get AS112 time series grouped by dimension

`GET /radar/as112/timeseries_groups/{dimension}`

Retrieves the distribution of AS112 queries grouped by dimension over time.

## Parameters

- **dimension** (string, required) [path]: Specifies the attribute by which to group the results.
- **aggInterval** (string, optional) [query]: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude locations from results. For example, `-US,PT` excludes results from the US, but includes results from PT.
- **continent** (array, optional) [query]: Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.
- **queryType** (array, optional) [query]: Filters results by DNS query type.
- **protocol** (array, optional) [query]: Filters results by DNS transport protocol.
- **responseCode** (array, optional) [query]: Filters results by DNS response code.
- **limitPerGroup** (integer, optional) [query]: Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.
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

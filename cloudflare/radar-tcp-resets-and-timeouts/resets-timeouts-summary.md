# Get TCP resets and timeouts summary

`GET /radar/tcp_resets_timeouts/summary`

Retrieves the distribution of connection stage by TCP connections terminated within the first 10 packets by a reset or timeout.

## Parameters

- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **asn** (array, optional) [query]: Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude locations from results. For example, `-US,PT` excludes results from the US, but includes results from PT.
- **continent** (array, optional) [query]: Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.
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

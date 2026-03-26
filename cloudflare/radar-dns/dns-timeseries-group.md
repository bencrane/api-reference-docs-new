# Get DNS time series grouped by dimension

`GET /radar/dns/timeseries_groups/{dimension}`

Retrieves the distribution of DNS queries grouped by dimension over time.

## Parameters

- **dimension** (string, required) [path]: Specifies the attribute by which to group the results.
- **aggInterval** (string, optional) [query]: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **asn** (array, optional) [query]: Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude locations from results. For example, `-US,PT` excludes results from the US, but includes results from PT.
- **continent** (array, optional) [query]: Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.
- **cacheHit** (array, optional) [query]: Filters results based on cache status.
- **nodata** (array, optional) [query]: Specifies whether the response includes empty DNS responses (NODATA).
- **protocol** (array, optional) [query]: Filters results by DNS transport protocol.
- **queryType** (array, optional) [query]: Filters results by DNS query type.
- **responseCode** (array, optional) [query]: Filters results by DNS response code.
- **responseTtl** (array, optional) [query]: Filters results by DNS response TTL.
- **dnssec** (array, optional) [query]: Filters results based on DNSSEC (DNS Security Extensions) support.
- **dnssecAware** (array, optional) [query]: Filters results based on DNSSEC (DNS Security Extensions) client awareness.
- **dnssecE2e** (array, optional) [query]: Filters results based on DNSSEC-validated answers by end-to-end security status.
- **ipVersion** (array, optional) [query]: Filters results by IP version (Ipv4 vs. IPv6).
- **limitPerGroup** (integer, optional) [query]: Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.
- **matchingAnswer** (array, optional) [query]: Filters results based on whether the queries have a matching answer.
- **tld** (array, optional) [query]: Filters results by top-level domain.
- **normalization** (string, optional) [query]: Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
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

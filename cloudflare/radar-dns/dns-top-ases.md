# Get top ASes by DNS queries

`GET /radar/dns/top/ases`

Retrieves the top autonomous systems by DNS queries made to 1.1.1.1 DNS resolver.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **asn** (array, optional) [query]: Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude locations from results. For example, `-US,PT` excludes results from the US, but includes results from PT.
- **continent** (array, optional) [query]: Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.
- **domain** (array, optional) [query]: Filters results by domain name.
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
- **matchingAnswer** (array, optional) [query]: Filters results based on whether the queries have a matching answer.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

# Get top locations by HTTP requests for an OS

`GET /radar/http/top/locations/os/{os}`

Retrieves the top locations, by HTTP requests, of the requested operating system.

## Parameters

- **os** (string, required) [path]: Operating system.
- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **asn** (array, optional) [query]: Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude locations from results. For example, `-US,PT` excludes results from the US, but includes results from PT.
- **continent** (array, optional) [query]: Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.
- **geoId** (array, optional) [query]: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs. Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689` excludes results from the 2267056 (Lisbon), but includes results from 5128638 (New York).
- **botClass** (array, optional) [query]: Filters results by bot class. Refer to [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).
- **deviceType** (array, optional) [query]: Filters results by device type.
- **httpProtocol** (array, optional) [query]: Filters results by HTTP protocol (HTTP vs. HTTPS).
- **httpVersion** (array, optional) [query]: Filters results by HTTP version.
- **ipVersion** (array, optional) [query]: Filters results by IP version (Ipv4 vs. IPv6).
- **tlsVersion** (array, optional) [query]: Filters results by TLS version.
- **browserFamily** (array, optional) [query]: Filters results by browser family.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 404

Not found.

- **error** (string):

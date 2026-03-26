# Get certificates time series

`GET /radar/ct/timeseries`

Retrieves certificate volume over time.

## Parameters

- **aggInterval** (string, optional) [query]: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **ca** (array, optional) [query]: Filters results by certificate authority.
- **caOwner** (array, optional) [query]: Filters results by certificate authority owner.
- **duration** (array, optional) [query]: Filters results by certificate duration.
- **entryType** (array, optional) [query]: Filters results by entry type (certificate vs. pre-certificate).
- **expirationStatus** (array, optional) [query]: Filters results by expiration status (expired vs. valid).
- **hasIps** (array, optional) [query]: Filters results based on whether the certificates are bound to specific IP addresses.
- **hasWildcards** (array, optional) [query]: Filters results based on whether the certificates contain wildcard domains.
- **log** (array, optional) [query]: Filters results by certificate log.
- **logApi** (array, optional) [query]: Filters results by certificate log API (RFC6962 vs. static).
- **logOperator** (array, optional) [query]: Filters results by certificate log operator.
- **publicKeyAlgorithm** (array, optional) [query]: Filters results by public key algorithm.
- **signatureAlgorithm** (array, optional) [query]: Filters results by signature algorithm.
- **tld** (array, optional) [query]: Filters results by top-level domain.
- **validationLevel** (array, optional) [query]: Filters results by validation level.
- **uniqueEntries** (array, optional) [query]: Specifies whether to filter out duplicate certificates and pre-certificates. Set to true for unique entries only.
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

# Get certificate distribution by dimension

`GET /radar/ct/summary/{dimension}`

Retrieves an aggregated summary of certificates grouped by the specified dimension.

## Parameters

- **dimension** (string, required) [path]: Specifies the certificate attribute by which to group the results.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **limitPerGroup** (integer, optional) [query]: Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.
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

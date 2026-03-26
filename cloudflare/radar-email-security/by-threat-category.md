# Get email threat category summary

`GET /radar/email/security/summary/threat_category`

> **Deprecated**

Retrieves the distribution of emails by threat categories.

## Parameters

- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **arc** (array, optional) [query]: Filters results by ARC (Authenticated Received Chain) validation.
- **dkim** (array, optional) [query]: Filters results by DKIM (DomainKeys Identified Mail) validation status.
- **dmarc** (array, optional) [query]: Filters results by DMARC (Domain-based Message Authentication, Reporting and Conformance) validation status.
- **spf** (array, optional) [query]: Filters results by SPF (Sender Policy Framework) validation status.
- **tlsVersion** (array, optional) [query]: Filters results by TLS version.
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

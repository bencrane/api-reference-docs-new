# Get latest Internet traffic anomalies

`GET /radar/traffic_anomalies`

Retrieves the latest Internet traffic anomalies, which are signals that might indicate an outage. These alerts are automatically detected by Radar and manually verified by our team.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **dateRange** (string, optional) [query]: Filters results by date range.
- **dateStart** (string, optional) [query]: Start of the date range (inclusive).
- **dateEnd** (string, optional) [query]: End of the date range (inclusive).
- **status** (string, optional) [query]: 
- **type** (array, optional) [query]: Filters results by entity type (LOCATION, AS, or ORIGIN).
- **asn** (integer, optional) [query]: Filters results by Autonomous System. Specify a single Autonomous System Number (ASN) as integer.
- **location** (string, optional) [query]: Filters results by location. Specify an alpha-2 location code.
- **origin** (string, optional) [query]: Filters results by origin.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

List of Internet traffic anomalies.

- **result** (object): 
- **success** (boolean): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

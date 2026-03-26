# Get top locations by total traffic anomalies

`GET /radar/traffic_anomalies/locations`

Retrieves the sum of Internet traffic anomalies, grouped by location. These anomalies are signals that might indicate an outage, automatically detected by Radar and manually verified by our team.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **dateRange** (string, optional) [query]: Filters results by date range.
- **dateStart** (string, optional) [query]: Start of the date range (inclusive).
- **dateEnd** (string, optional) [query]: End of the date range (inclusive).
- **status** (string, optional) [query]: 
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

List of locations with number of traffic anomalies.

- **result** (object): 
- **success** (boolean): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

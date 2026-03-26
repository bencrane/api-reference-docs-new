# Get ASPA count time series

`GET /radar/bgp/rpki/aspa/timeseries`

Retrieves ASPA (Autonomous System Provider Authorization) object count over time. Supports filtering by RIR or location (country code) to generate multiple named series. If no RIR or location filter is specified, returns total count.

## Parameters

- **dateStart** (string, optional) [query]: Start of the date range (inclusive).
- **dateEnd** (string, optional) [query]: End of the date range (inclusive).
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **rir** (array, optional) [query]: Filter by Regional Internet Registry (RIR). Multiple RIRs generate multiple series.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 location codes.
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

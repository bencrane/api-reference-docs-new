# Get AS rankings by botnet threat feed activity

`GET /radar/entities/asns/botnet_threat_feed`

Retrieves a ranked list of Autonomous Systems based on their presence in the Cloudflare Botnet Threat Feed. Rankings can be sorted by offense count or number of bad IPs. Optionally compare to a previous date to see rank changes.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **offset** (integer, optional) [query]: Skips the specified number of objects before fetching the results.
- **metric** (string, optional) [query]: Metric to rank ASNs by.
- **date** (string, optional) [query]: The date to retrieve (YYYY-MM-DD format). If not specified, returns the most recent available data. Note: This is the date the report was generated. The report is generated from information collected from the previous day (e.g., the 2026-02-23 entry contains data from 2026-02-22).
- **compareDateRange** (string, optional) [query]: Relative date range for rank change comparison (e.g., "1d", "7d", "30d").
- **location** (string, optional) [query]: Filters results by location. Specify an alpha-2 location code.
- **asn** (array, optional) [query]: Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.
- **sortOrder** (string, optional) [query]: Sort order.
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

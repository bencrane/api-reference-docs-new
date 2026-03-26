# Get percentiles for a traceroute test

`GET /accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles`

Get percentiles for a traceroute test for a given time period between 1 hour and 7 days.

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path.
- **test_id** (string, required) [path]: unique identifier for a specific test
- **deviceId** (array, optional) [query]: Optionally filter result stats to a specific device(s). Cannot be used in combination with colo param.
- **from** (string, required) [query]: Start time for the query in ISO (RFC3339 - ISO 8601) format
- **to** (string, required) [query]: End time for the query in ISO (RFC3339 - ISO 8601) format
- **colo** (string, optional) [query]: Optionally filter result stats to a Cloudflare colo. Cannot be used in combination with deviceId param.

## Response

### 200

DEX Traceroute test percentiles response

- **result** (object, optional): 

### 4XX

DEX Traceroute test percentiles failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

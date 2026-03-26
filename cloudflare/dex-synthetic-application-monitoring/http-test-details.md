# Get details and aggregate metrics for an http test

`GET /accounts/{account_id}/dex/http-tests/{test_id}`

Get test details and aggregate performance metrics for an http test for a given time period between 1 hour and 7 days.

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path.
- **test_id** (string, required) [path]: unique identifier for a specific test
- **deviceId** (array, optional) [query]: Optionally filter result stats to a specific device(s). Cannot be used in combination with colo param.
- **from** (string, required) [query]: Start time for aggregate metrics in ISO ms
- **to** (string, required) [query]: End time for aggregate metrics in ISO ms
- **interval** (string, required) [query]: Time interval for aggregate time slots.
- **colo** (string, optional) [query]: Optionally filter result stats to a Cloudflare colo. Cannot be used in combination with deviceId param.

## Response

### 200

DEX HTTP test details response

- **result** (object, optional): 

### 4XX

DEX HTTP test details failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

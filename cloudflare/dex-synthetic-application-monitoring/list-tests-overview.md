# List DEX test analytics

`GET /accounts/{account_id}/dex/tests/overview`

List DEX tests with overview metrics

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path.
- **colo** (string, optional) [query]: Optionally filter result stats to a Cloudflare colo. Cannot be used in combination with deviceId param.
- **testName** (string, optional) [query]: Optionally filter results by test name
- **deviceId** (array, optional) [query]: Optionally filter result stats to a specific device(s). Cannot be used in combination with colo param.
- **page** (number, optional) [query]: Page number of paginated results
- **per_page** (number, optional) [query]: Number of items per page
- **kind** (string, optional) [query]: Filter by test type

## Response

### 200

success response

- **result** (object, optional): 

### 4XX

failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Get count of devices targeted

`GET /accounts/{account_id}/dex/tests/unique-devices`

Returns unique count of devices that have run synthetic application monitoring tests in the past 7 days.

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path.
- **testName** (string, optional) [query]: Optionally filter results by test name
- **deviceId** (array, optional) [query]: Optionally filter result stats to a specific device(s). Cannot be used in combination with colo param.

## Response

### 200

DEX unique devices targeted response

- **result** (object, optional): 

### 4XX

DEX unique devices targeted failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

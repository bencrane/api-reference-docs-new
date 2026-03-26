# List Device DEX tests

`GET /accounts/{account_id}/dex/devices/dex_tests`

Fetch all DEX tests

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: Page number of paginated results
- **per_page** (number, optional) [query]: Number of items per page
- **testName** (string, optional) [query]: Filter by test name
- **kind** (string, optional) [query]: Filter by test type

## Response

### 200

Device DEX test details response

- **result** (array, optional): 

### 4XX

Device DEX test response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Get Device DEX test

`GET /accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}`

Fetch a single DEX test.

## Parameters

- **account_id** (string, required) [path]: 
- **dex_test_id** (string, required) [path]: 

## Response

### 200

Device DEX test details response

- **result** (object, optional): 

### 4XX

Device DEX test response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

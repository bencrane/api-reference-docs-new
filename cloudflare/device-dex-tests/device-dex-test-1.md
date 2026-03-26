# Delete Device DEX test

`DELETE /accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}`

Delete a Device DEX test. Returns the remaining device dex tests for the account.

## Parameters

- **account_id** (string, required) [path]: 
- **dex_test_id** (string, required) [path]: 

## Response

### 200

Delete Device DEX test response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Delete DEX test response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

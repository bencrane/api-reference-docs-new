# Update Device DEX test

`PUT /accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}`

Update a DEX test.

## Parameters

- **account_id** (string, required) [path]: 
- **dex_test_id** (string, required) [path]: 

## Request Body

- **data** (object, required): The configuration object which contains the details for the WARP client to conduct the test.
- **description** (string, optional): Additional details about the test.
- **enabled** (boolean, required): Determines whether or not the test is active.
- **interval** (string, required): How often the test will run.
- **name** (string, required): The name of the DEX test. Must be unique.
- **target_policies** (array, optional): DEX rules targeted by this test
- **targeted** (boolean, optional): 
- **test_id** (string, optional): The unique identifier for the test.

## Response

### 200

Update Dex test response

- **result** (object, optional): 

### 4XX

Update Dex test response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

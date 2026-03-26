# Get details for a specific traceroute test run

`GET /accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path`

Get a breakdown of hops and performance metrics for a specific traceroute test run

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account
- **test_result_id** (string, required) [path]: unique identifier for a specific traceroute test

## Response

### 200

DEX traceroute test result network path response

- **result** (object, optional): 

### 4XX

DEX traceroute test result network path failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

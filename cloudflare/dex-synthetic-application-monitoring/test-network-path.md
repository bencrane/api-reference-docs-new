# Get network path breakdown for a traceroute test

`GET /accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path`

Get a breakdown of metrics by hop for individual traceroute test runs

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account
- **test_id** (string, required) [path]: unique identifier for a specific test
- **deviceId** (string, required) [query]: Device to filter tracroute result runs to
- **from** (string, required) [query]: Start time for aggregate metrics in ISO ms
- **to** (string, required) [query]: End time for aggregate metrics in ISO ms
- **interval** (string, required) [query]: Time interval for aggregate time slots.

## Response

### 200

DEX traceroute test network path response

- **result** (object, optional): 

### 4XX

DEX traceroute test network path failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

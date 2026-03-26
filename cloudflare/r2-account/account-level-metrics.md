# Get Account-Level Metrics

`GET /accounts/{account_id}/r2/metrics`

Get Storage/Object Count Metrics across all buckets in your account. Note that Account-Level Metrics may not immediately reflect the latest data.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get Account-Level Metrics response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Metrics based on the class they belong to.
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Get Account-Level Metrics response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

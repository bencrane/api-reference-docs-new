# List Request Assets

`POST /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 

## Request Body

- **page** (integer, required): Page number of results.
- **per_page** (integer, required): Number of results per page.

## Response

### 200

List request assets response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List request assets response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):

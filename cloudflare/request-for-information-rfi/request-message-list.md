# List Request Messages

`POST /accounts/{account_id}/cloudforce-one/requests/{request_id}/message`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 

## Request Body

- **after** (object, optional): Retrieve mes  ges created after this time.
- **before** (object, optional): Retrieve messages created before this time.
- **page** (integer, required): Page number of results.
- **per_page** (integer, required): Number of results per page.
- **sort_by** (string, optional): Field to sort results by.
- **sort_order** (string, optional): Sort order (asc or desc). Values: `asc`, `desc`

## Response

### 200

List request messages response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List request messages response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):

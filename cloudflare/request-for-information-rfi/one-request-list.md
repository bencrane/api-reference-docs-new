# List Requests

`POST /accounts/{account_id}/cloudforce-one/requests`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **completed_after** (object, optional): Retrieve requests completed after this time.
- **completed_before** (object, optional): Retrieve requests completed before this time.
- **created_after** (object, optional): Retrieve requests created after this time.
- **created_before** (object, optional): Retrieve requests created before this time.
- **page** (integer, required): Page number of results.
- **per_page** (integer, required): Number of results per page.
- **request_type** (string, optional): Requested information from request.
- **sort_by** (string, optional): Field to sort results by.
- **sort_order** (string, optional): Sort order (asc or desc). Values: `asc`, `desc`
- **status** (string, optional): Request Status. Values: `open`, `accepted`, `reported`, `approved`, `completed`, `declined`

## Response

### 200

List requests response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Create response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):

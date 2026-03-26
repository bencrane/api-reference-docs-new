# List Web Analytics sites

`GET /accounts/{account_id}/rum/site_info/list`

Lists all Web Analytics sites of an account.

## Parameters

- **account_id** (string, required) [path]: 
- **per_page** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **order_by** (string, optional) [query]: 

## Response

### 200

List of Web Analytics sites.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

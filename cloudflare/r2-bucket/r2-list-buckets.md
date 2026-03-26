# List Buckets

`GET /accounts/{account_id}/r2/buckets`

Lists all R2 buckets on your account.

## Parameters

- **account_id** (string, required) [path]: 
- **name_contains** (string, optional) [query]: 
- **start_after** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **cursor** (string, optional) [query]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

List Buckets response.

- **result** (object, optional): 

### 4XX

List Buckets response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

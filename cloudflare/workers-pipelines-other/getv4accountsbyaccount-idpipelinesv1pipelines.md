# List Pipelines

`GET /accounts/{account_id}/pipelines/v1/pipelines`

List/Filter Pipelines in Account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

Indicates a successfully listed Pipelines.

- **result** (array): 
- **result_info** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in listing Pipelines.

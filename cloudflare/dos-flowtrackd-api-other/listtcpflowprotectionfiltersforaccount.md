# List all TCP Flow Protection filters.

`GET /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters`

List all TCP Flow Protection filters for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **mode** (string, optional) [query]: The mode of the filters to get. Optional. Valid values: 'enabled', 'disabled', 'monitoring'.
- **page** (integer, optional) [query]: The page number for pagination. Defaults to 1.
- **per_page** (integer, optional) [query]: The number of items per page. Must be between 10 and 1000. Defaults to 25.
- **order** (string, optional) [query]: The field to order by. Defaults to 'prefix'.
- **direction** (string, optional) [query]: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

## Response

### 200

List all TCP Flow Protection filters response.

- **result** (array, optional): 

### 4XX

List all TCP Flow Protection filters failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

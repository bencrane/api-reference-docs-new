# List DEX Rules

`GET /accounts/{account_id}/dex/rules`

List DEX Rules

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **page** (number, required) [query]: Page number of paginated results
- **per_page** (number, required) [query]: Number of items per page
- **sort_order** (string, optional) [query]: Sort direction for sort_by property
- **sort_by** (string, optional) [query]: Which property to sort results by
- **name** (string, optional) [query]: Filter results by rule name

## Response

### 200

success response

- **result** (object, optional): 

### 4XX

List DEX Rules failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# List Tokens

`GET /user/tokens`

List all access tokens you created.

## Parameters

- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List Tokens response

- **result** (array, optional): 

### 4XX

List Tokens response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

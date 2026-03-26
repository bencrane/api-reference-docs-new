# Search Resources

`GET /accounts/{account_id}/load_balancers/search`

Search for Load Balancing resources.

## Parameters

- **account_id** (string, required) [path]: 
- **query** (string, optional) [query]: 
- **references** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

Search Resources response.

- **result** (object, optional): 

### 4XX

Search Resources response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

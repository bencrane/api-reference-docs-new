# List virtual networks

`GET /accounts/{account_id}/teamnet/virtual_networks`

Lists and filters virtual networks in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: 
- **name** (string, optional) [query]: 
- **is_default** (boolean, optional) [query]: 
- **is_default_network** (boolean, optional) [query]: 
- **is_deleted** (boolean, optional) [query]: 

## Response

### 200

List virtual networks response

- **result** (array, optional): 

### 4XX

List virtual networks response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

# List tunnel routes

`GET /accounts/{account_id}/teamnet/routes`

Lists and filters private network routes in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **comment** (string, optional) [query]: 
- **is_deleted** (boolean, optional) [query]: 
- **network_subset** (string, optional) [query]: 
- **network_superset** (string, optional) [query]: 
- **existed_at** (string, optional) [query]: 
- **tunnel_id** (string, optional) [query]: 
- **route_id** (string, optional) [query]: 
- **tun_types** (string, optional) [query]: 
- **virtual_network_id** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 
- **page** (string, optional) [query]: 

## Response

### 200

List tunnel routes response

- **result** (array, optional): 

### 4XX

List tunnel routes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

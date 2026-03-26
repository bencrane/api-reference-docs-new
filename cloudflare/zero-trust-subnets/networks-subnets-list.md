# List Subnets

`GET /accounts/{account_id}/zerotrust/subnets`

Lists and filters subnets in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: If set, only list subnets with the given name
- **comment** (string, optional) [query]: 
- **network** (string, optional) [query]: 
- **existed_at** (string, optional) [query]: 
- **address_family** (string, optional) [query]: If set, only include subnets in the given address family - `v4` or `v6`
- **is_default_network** (boolean, optional) [query]: 
- **is_deleted** (boolean, optional) [query]: 
- **sort_order** (string, optional) [query]: 
- **subnet_types** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 
- **page** (string, optional) [query]: 

## Response

### 200

List subnets response

- **result** (array, optional): 

### 4XX

List subnets response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

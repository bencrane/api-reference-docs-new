# List a Namespace's Keys

`GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys`

Lists a namespace's keys.

## Parameters

- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **limit** (number, optional) [query]: 
- **prefix** (string, optional) [query]: 
- **cursor** (string, optional) [query]: 

## Response

### 200

List a Namespace's Keys response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List a Namespace's Keys response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

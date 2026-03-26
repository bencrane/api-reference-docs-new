# List Objects

`GET /accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects`

Returns the Durable Objects in a given namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 
- **limit** (number, optional) [query]: 
- **cursor** (string, optional) [query]: 

## Response

### 200

List Objects response.

- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List Objects response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

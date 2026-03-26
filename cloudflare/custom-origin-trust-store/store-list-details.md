# List Custom Origin Trust Store Details

`GET /zones/{zone_id}/acm/custom_trust_store`

Get Custom Origin Trust Store for a Zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **offset** (integer, optional) [query]: 

## Response

### 200

Custom Origin Trust Store Details response

- **result** (array, optional): 

### 4XX

Custom Origin Trust Store response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

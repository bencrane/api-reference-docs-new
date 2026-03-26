# List Certificates

`GET /certificates`

List all existing Origin CA certificates for a given zone. You can use an Origin CA Key as your User Service Key or an API token when calling this endpoint ([see above](#requests)).

## Parameters

- **zone_id** (string, required) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **offset** (integer, optional) [query]: 

## Response

### 200

List Certificates response

- **result** (array, optional): 

### 4XX

List Certificates response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

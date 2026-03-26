# Get hostname route

`GET /accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}`

Get a hostname route.

## Parameters

- **account_id** (string, required) [path]: 
- **hostname_route_id** (string, required) [path]: 

## Response

### 200

Get hostname route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get hostname route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

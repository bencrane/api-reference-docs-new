# Update hostname route

`PATCH /accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}`

Updates a hostname route.

## Parameters

- **account_id** (string, required) [path]: 
- **hostname_route_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): An optional description of the hostname route.
- **hostname** (string, optional): The hostname of the route.
- **tunnel_id** (string, optional): UUID of the tunnel.

## Response

### 200

Update hostname route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update hostname route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

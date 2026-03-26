# Create hostname route

`POST /accounts/{account_id}/zerotrust/routes/hostname`

Create a hostname route.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): An optional description of the hostname route.
- **hostname** (string, optional): The hostname of the route.
- **tunnel_id** (string, optional): UUID of the tunnel.

## Response

### 200

Create hostname route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create hostname route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

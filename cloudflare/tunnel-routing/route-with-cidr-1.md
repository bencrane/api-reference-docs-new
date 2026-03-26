# Update a tunnel route (CIDR Endpoint)

`PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`

> **Deprecated**

Updates an existing private network route in an account. The CIDR in `ip_network_encoded` must be written in URL-encoded format.

## Parameters

- **ip_network_encoded** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Update a tunnel route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update a tunnel route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

# List IPsec tunnels

`GET /accounts/{account_id}/magic/ipsec_tunnels`

Lists IPsec tunnels associated with an account.

## Parameters

- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the response body will be presented using the new object format. Defaults to false.

## Response

### 200

List IPsec tunnels response

- **result** (object, optional): 

### 4XX

List IPsec tunnels response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

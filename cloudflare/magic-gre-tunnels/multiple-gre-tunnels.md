# Update multiple GRE tunnels

`PUT /accounts/{account_id}/magic/gre_tunnels`

Updates multiple GRE tunnels. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

## Parameters

- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the request and response bodies will be presented using the new object format. Defaults to false.

## Request Body

_Unknown type_

## Response

### 200

Update multiple GRE tunnels response

- **result** (object, optional): 

### 4XX

Update multiple GRE tunnels response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

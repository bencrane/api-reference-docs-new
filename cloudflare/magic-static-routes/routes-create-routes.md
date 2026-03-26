# Create a Route

`POST /accounts/{account_id}/magic/routes`

Creates a new Magic static route. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An optional human provided description of the static route.
- **nexthop** (string, required): The next-hop IP Address for the static route.
- **prefix** (string, required): IP Prefix in Classless Inter-Domain Routing format.
- **priority** (integer, required): Priority of the static route.
- **scope** (object, optional): Used only for ECMP routes.
- **weight** (integer, optional): Optional weight of the ECMP scope - if provided.

## Response

### 200

Create Routes response

- **result** (object, optional): 

### 4XX

Create Routes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

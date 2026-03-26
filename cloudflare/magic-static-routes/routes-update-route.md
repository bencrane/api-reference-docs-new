# Update Route

`PUT /accounts/{account_id}/magic/routes/{route_id}`

Update a specific Magic static route. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes.

## Parameters

- **route_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An optional human provided description of the static route.
- **nexthop** (string, optional): The next-hop IP Address for the static route.
- **prefix** (string, optional): IP Prefix in Classless Inter-Domain Routing format.
- **priority** (integer, optional): Priority of the static route.
- **scope** (object, optional): Used only for ECMP routes.
- **weight** (integer, optional): Optional weight of the ECMP scope - if provided.

## Response

### 200

Update Route response

- **result** (object, optional): 

### 4XX

Update Route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

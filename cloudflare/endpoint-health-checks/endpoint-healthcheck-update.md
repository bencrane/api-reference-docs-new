# Update Endpoint Health Check

`PUT /accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}`

Update a Endpoint Health Check.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Request Body

- **check_type** (string, required): type of check to perform Values: `icmp`
- **endpoint** (string, required): the IP address of the host to perform checks against
- **name** (string, optional): Optional name associated with this check

## Response

### 200

Endpoint Health Checks response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Endpoint Health Check failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Endpoint Health Check

`POST /accounts/{account_id}/diagnostics/endpoint-healthchecks`

Create Endpoint Health Check.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **check_type** (string, required): type of check to perform Values: `icmp`
- **endpoint** (string, required): the IP address of the host to perform checks against
- **name** (string, optional): Optional name associated with this check

## Response

### 201

Endpoint Health Check response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Endpoint Health Check response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

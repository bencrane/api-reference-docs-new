# Create a new Provider Configs

`POST /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs`

Creates a new AI Gateway.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 

## Request Body

- **alias** (string, required): 
- **default_config** (boolean, required): 
- **provider_slug** (string, required): 
- **rate_limit** (number, optional): 
- **rate_limit_period** (number, optional): 
- **secret** (string, required): 
- **secret_id** (string, required): 

## Response

### 200

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):

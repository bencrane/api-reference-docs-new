# Create a new Gateway

`POST /accounts/{account_id}/ai-gateway/gateways`

Creates a new AI Gateway.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **authentication** (boolean, optional): 
- **cache_invalidate_on_update** (boolean, required): 
- **cache_ttl** (integer, required): 
- **collect_logs** (boolean, required): 
- **id** (string, required): gateway id
- **log_management** (integer, optional): 
- **log_management_strategy** (string, optional):  Values: `STOP_INSERTING`, `DELETE_OLDEST`
- **logpush** (boolean, optional): 
- **logpush_public_key** (string, optional): 
- **rate_limiting_interval** (integer, required): 
- **rate_limiting_limit** (integer, required): 
- **rate_limiting_technique** (string, optional):  Values: `fixed`, `sliding`
- **retry_backoff** (string, optional): Backoff strategy for retry delays Values: `constant`, `linear`, `exponential`
- **retry_delay** (integer, optional): Delay between retry attempts in milliseconds (0-5000)
- **retry_max_attempts** (integer, optional): Maximum number of retry attempts for failed requests (1-5)
- **workers_ai_billing_mode** (string, optional): Controls how Workers AI inference calls routed through this gateway are billed. Only 'postpaid' is currently supported. Values: `postpaid`
- **zdr** (boolean, optional): 

## Response

### 200

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):

# Update an email domain

`PATCH /accounts/{account_id}/email-security/settings/domains/{domain_id}`

Updates configuration for a domain in email security.

## Parameters

- **account_id** (string, required) [path]: 
- **domain_id** (integer, required) [path]: 

## Request Body

- **allowed_delivery_modes** (array, optional): 
- **domain** (string, optional): 
- **drop_dispositions** (array, optional): 
- **folder** (object, optional): 
- **integration_id** (string, optional): 
- **ip_restrictions** (array, required): 
- **lookback_hops** (integer, optional): 
- **regions** (array, optional): 
- **require_tls_inbound** (boolean, optional): 
- **require_tls_outbound** (boolean, optional): 
- **transport** (string, optional): 

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):

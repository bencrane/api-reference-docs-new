# Create TCP Flow Protection rule.

`POST /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules`

Create a TCP Flow Protection rule for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Request Body

- **burst_sensitivity** (string, required): The burst sensitivity. Must be one of 'low', 'medium', 'high'.
- **mode** (string, required): The mode for the TCP Flow Protection. Must be one of 'enabled', 'disabled', 'monitoring'.
- **name** (string, required): The name of the TCP Flow Protection rule. Value is relative to the 'scope' setting. For 'global' scope, name should be 'global'. For either the 'region' or 'datacenter' scope, name should be the actual name of the region or datacenter, e.g., 'wnam' or 'lax'.
- **rate_sensitivity** (string, required): The rate sensitivity. Must be one of 'low', 'medium', 'high'.
- **scope** (string, required): The scope for the TCP Flow Protection rule.

## Response

### 200

Create TCP Flow Protection rule response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create TCP Flow Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

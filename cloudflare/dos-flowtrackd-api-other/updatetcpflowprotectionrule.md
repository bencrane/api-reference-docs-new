# Update TCP Flow Protection rule.

`PATCH /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}`

Update a TCP Flow Protection rule specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **rule_id** (string, required) [path]: The UUID of the TCP Flow Protection rule to update.

## Request Body

- **burst_sensitivity** (string, optional): The new burst sensitivity. Optional. Must be one of 'low', 'medium', 'high'.
- **mode** (string, optional): The new mode for TCP Flow Protection. Optional. Must be one of 'enabled', 'disabled', 'monitoring'.
- **rate_sensitivity** (string, optional): The new rate sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

## Response

### 200

Update TCP Flow Protection rule response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update TCP Flow Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

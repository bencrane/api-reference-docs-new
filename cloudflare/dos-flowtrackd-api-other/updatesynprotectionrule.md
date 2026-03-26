# Update SYN Protection rule.

`PATCH /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}`

Update a SYN Protection rule specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **rule_id** (string, required) [path]: The UUID of the SYN Protection rule to update.

## Request Body

- **burst_sensitivity** (string, optional): The new burst sensitivity. Optional. Must be one of 'low', 'medium', 'high'.
- **mitigation_type** (string, optional): The new mitigation type. Optional. Must be one of 'challenge' or 'retransmit'.
- **mode** (string, optional): The new mode for SYN Protection. Optional. Must be one of 'enabled', 'disabled', 'monitoring'.
- **rate_sensitivity** (string, optional): The new rate sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

## Response

### 200

Update SYN Protection rule response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update SYN Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

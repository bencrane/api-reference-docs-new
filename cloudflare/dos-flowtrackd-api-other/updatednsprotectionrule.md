# Update DNS Protection rule.

`PATCH /accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}`

Update a DNS Protection rule specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **rule_id** (string, required) [path]: The UUID of the DNS Protection rule to update.

## Request Body

- **burst_sensitivity** (string, optional): The new burst sensitivity. Optional. Must be one of 'low', 'medium', 'high'.
- **mode** (string, optional): The new mode for DNS Protection. Optional. Must be one of 'enabled', 'disabled', 'monitoring'.
- **profile_sensitivity** (string, optional): The new profile sensitivity. Optional. Recommended setting is 'low'. Must be one of 'low', 'medium', 'high', or 'very_high'.
- **rate_sensitivity** (string, optional): The new rate sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

## Response

### 200

Update DNS Protection rule response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update DNS Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

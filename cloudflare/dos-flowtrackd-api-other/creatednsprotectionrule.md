# Create DNS Protection rule.

`POST /accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules`

Create a DNS Protection rule for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Request Body

- **burst_sensitivity** (string, required): The burst sensitivity. Must be one of 'low', 'medium', 'high'.
- **mode** (string, required): The mode for DNS Protection. Must be one of 'enabled', 'disabled', 'monitoring'.
- **name** (string, required): The name of the DNS Protection rule. Value is relative to the 'scope' setting. For 'global' scope, name should be 'global'. For either the 'region' or 'datacenter' scope, name should be the actual name of the region or datacenter, e.g., 'wnam' or 'lax'.
- **profile_sensitivity** (string, required): The profile sensitivity. Recommended setting is 'low'. Must be one of 'low', 'medium', 'high', or 'very_high'.
- **rate_sensitivity** (string, required): The rate sensitivity. Must be one of 'low', 'medium', 'high'.
- **scope** (string, required): The scope for the DNS Protection rule. Must be one of 'global', 'region', or 'datacenter'.

## Response

### 200

Create DNS Protection rule response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create DNS Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

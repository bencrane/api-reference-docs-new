# Get the Local Domain Fallback list for a device settings profile

`GET /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains`

Fetches the list of domains to bypass Gateway DNS resolution from a specified device settings profile. These domains will use the specified local DNS resolver instead.

## Parameters

- **policy_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get the Local Domain Fallback list for a device settings profile response.

- **result** (array, optional): 

### 4XX

Get the Local Domain Fallback list for a device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

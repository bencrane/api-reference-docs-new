# Set the Local Domain Fallback list for a device settings profile

`PUT /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains`

Sets the list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead. This will only apply to the specified device settings profile.

## Parameters

- **policy_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Set the Local Domain Fallback list for a device settings profile response.

- **result** (array, optional): 

### 4XX

Set the Local Domain Fallback list for a device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

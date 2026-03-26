# Set your Local Domain Fallback list

`PUT /accounts/{account_id}/devices/policy/fallback_domains`

Sets the list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Set your Local Domain Fallback list response.

- **result** (array, optional): 

### 4XX

Set your Local Domain Fallback list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

# Get your Local Domain Fallback list

`GET /accounts/{account_id}/devices/policy/fallback_domains`

Fetches a list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get your Local Domain Fallback list response.

- **result** (array, optional): 

### 4XX

Get your Local Domain Fallback list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

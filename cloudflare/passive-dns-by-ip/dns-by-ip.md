# Get Passive DNS by IP

`GET /accounts/{account_id}/intel/dns`

Gets a list of all the domains that have resolved to a specific IP address.

## Parameters

- **account_id** (string, required) [path]: 
- **start_end_params** (string, optional) [query]: 
- **ipv4** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

Get Passive DNS by IP response.

_Empty object_

### 4XX

Get Passive DNS by IP response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

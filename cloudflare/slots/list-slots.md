# Retrieve a list of all slots matching the specified parameters

`GET /accounts/{account_id}/cni/slots`



## Parameters

- **address_contains** (string, optional) [query]: If specified, only show slots with the given text in their address field
- **site** (string, optional) [query]: If specified, only show slots located at the given site
- **speed** (string, optional) [query]: If specified, only show slots that support the given speed
- **occupied** (boolean, optional) [query]: If specified, only show slots with a specific occupied/unoccupied state
- **cursor** (integer, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List of matching slots

- **items** (array): 
- **next** (integer): 

### 400

Bad request

### 500

Internal server error

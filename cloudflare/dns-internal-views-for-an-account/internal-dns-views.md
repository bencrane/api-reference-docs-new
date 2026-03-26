# List Internal DNS Views

`GET /accounts/{account_id}/dns_settings/views`

List DNS Internal Views for an Account

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **name.exact** (string, optional) [query]: 
- **name.contains** (string, optional) [query]: 
- **name.startswith** (string, optional) [query]: 
- **name.endswith** (string, optional) [query]: 
- **zone_id** (string, optional) [query]: 
- **zone_name** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List Internal DNS Views response

_Empty object_

### 4XX

List Internal DNS Views response failure

_Empty object_

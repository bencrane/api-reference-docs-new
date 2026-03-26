# List Page Shield Cookies

`GET /zones/{zone_id}/page_shield/cookies`

Lists all cookies collected by Page Shield.

## Parameters

- **zone_id** (string, required) [path]: 
- **hosts** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order_by** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **page_url** (string, optional) [query]: 
- **export** (string, optional) [query]: 
- **name** (string, optional) [query]: 
- **secure** (boolean, optional) [query]: 
- **http_only** (boolean, optional) [query]: 
- **same_site** (string, optional) [query]: 
- **type** (string, optional) [query]: 
- **path** (string, optional) [query]: 
- **domain** (string, optional) [query]: 

## Response

### 200

List Page Shield cookies response

- **result** (array, optional): 

### 4XX

List Page Shield cookies response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

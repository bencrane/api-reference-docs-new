# List Page Shield connections

`GET /zones/{zone_id}/page_shield/connections`

Lists all connections detected by Page Shield.

## Parameters

- **zone_id** (string, required) [path]: 
- **exclude_urls** (string, optional) [query]: 
- **urls** (string, optional) [query]: 
- **hosts** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order_by** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **prioritize_malicious** (boolean, optional) [query]: 
- **exclude_cdn_cgi** (boolean, optional) [query]: 
- **status** (string, optional) [query]: 
- **page_url** (string, optional) [query]: 
- **export** (string, optional) [query]: 

## Response

### 200

List Page Shield connections response

- **result** (array, optional): 

### 4XX

List Page Shield connections response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

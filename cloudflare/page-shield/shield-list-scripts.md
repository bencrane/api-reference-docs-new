# List Page Shield scripts

`GET /zones/{zone_id}/page_shield/scripts`

Lists all scripts detected by Page Shield.

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
- **exclude_duplicates** (boolean, optional) [query]: 
- **status** (string, optional) [query]: 
- **page_url** (string, optional) [query]: 
- **export** (string, optional) [query]: 

## Response

### 200

List Page Shield scripts response

- **result** (array, optional): 

### 4XX

List Page Shield scripts response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

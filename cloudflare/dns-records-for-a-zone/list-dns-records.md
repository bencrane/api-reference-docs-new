# List DNS Records

`GET /zones/{zone_id}/dns_records`

List, search, sort, and filter a zones' DNS records.

## Parameters

- **zone_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **name.exact** (string, optional) [query]: 
- **name.contains** (string, optional) [query]: 
- **name.startswith** (string, optional) [query]: 
- **name.endswith** (string, optional) [query]: 
- **type** (string, optional) [query]: 
- **content** (string, optional) [query]: 
- **content.exact** (string, optional) [query]: 
- **content.contains** (string, optional) [query]: 
- **content.startswith** (string, optional) [query]: 
- **content.endswith** (string, optional) [query]: 
- **proxied** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **comment** (string, optional) [query]: 
- **comment.present** (string, optional) [query]: 
- **comment.absent** (string, optional) [query]: 
- **comment.exact** (string, optional) [query]: 
- **comment.contains** (string, optional) [query]: 
- **comment.startswith** (string, optional) [query]: 
- **comment.endswith** (string, optional) [query]: 
- **tag** (string, optional) [query]: 
- **tag.present** (string, optional) [query]: 
- **tag.absent** (string, optional) [query]: 
- **tag.exact** (string, optional) [query]: 
- **tag.contains** (string, optional) [query]: 
- **tag.startswith** (string, optional) [query]: 
- **tag.endswith** (string, optional) [query]: 
- **search** (string, optional) [query]: 
- **tag_match** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List DNS Records response

_Empty object_

### 4XX

List DNS Records response failure

_Empty object_

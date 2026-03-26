# List images V2

`GET /accounts/{account_id}/images/v2`

List up to 10000 images with up to 1000 results per page. Use the optional parameters below to get a specific range of images.
Pagination is supported via continuation_token.

**Metadata Filtering (Optional):**

You can optionally filter images by custom metadata fields using the `meta.<field>[<operator>]=<value>` syntax.

**Supported Operators:**
- `eq` / `eq:string` / `eq:number` / `eq:boolean` - Exact match
- `in` / `in:string` / `in:number` - Match any value in list (pipe-separated)

**Metadata Filter Constraints:**
- Maximum 5 metadata filters per request
- Maximum 5 levels of nesting (e.g., `meta.first.second.third.fourth.fifth`)
- Maximum 10 elements for list operators (`in`)
- Supports string, number, and boolean value types

**Examples:**
```
# List all images
/images/v2

# Filter by metadata [eq]
/images/v2?meta.status[eq:string]=active

# Filter by metadata [in]
/images/v2?meta.status[in]=pending|deleted|flagged

# Filter by metadata [in:number]
/images/v2?meta.ratings[in:number]=4|5

# Filter by nested metadata
/images/v2?meta.region.name[eq]=eu-west

# Combine metadata filters with creator
/images/v2?meta.status[eq]=active&creator=user123

# Multiple metadata filters (AND logic)
/images/v2?meta.status[eq]=active&meta.priority[eq:number]=5
```


## Parameters

- **account_id** (string, required) [path]: 
- **continuation_token** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **sort_order** (string, optional) [query]: 
- **creator** (string, optional) [query]: 
- **meta.<field>[<operator>]** (string, optional) [query]: Optional metadata filter(s). Multiple filters can be combined with AND logic.

**Operators:**
- `eq`, `eq:string`, `eq:number`, `eq:boolean` - Exact match
- `in`, `in:string`, `in:number` - Match any value in pipe-separated list

**Examples:**
- `meta.status[eq]=active`
- `meta.priority[eq:number]=5`
- `meta.enabled[eq:boolean]=true`
- `meta.region[in]=us-east|us-west|eu-west`


## Response

### 200

List images response

- **result** (object, optional): 

### 400

Bad request

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

### 4XX

List images response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

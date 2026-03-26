# List tagged resources

`GET /accounts/{account_id}/tags/resources`

Lists all tagged resources for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **type** (array, optional) [query]: Filter by resource type. Can be repeated to filter by multiple types (OR logic). Example: ?type=zone&type=worker
- **tag** (array, optional) [query]: Filter resources by tag criteria. This parameter can be repeated multiple times, with AND logic between parameters.

Supported syntax:
- **Key-only**: `tag=<key>` - Resource must have the tag key (e.g., `tag=production`)
- **Key-value**: `tag=<key>=<value>` - Resource must have the tag with specific value (e.g., `tag=env=prod`)
- **Multiple values (OR)**: `tag=<key>=<v1>,<v2>` - Resource must have tag with any of the values (e.g., `tag=env=prod,staging`)
- **Negate key-only**: `tag=!<key>` - Resource must not have the tag key (e.g., `tag=!archived`)
- **Negate key-value**: `tag=<key>!=<value>` - Resource must not have the tag with specific value (e.g., `tag=region!=us-west-1`)

Multiple tag parameters are combined with AND logic.

- **cursor** (string, optional) [query]: Cursor for pagination.

## Response

### 200

List tagged resources response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List tagged resources response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 5XX

List tagged resources response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

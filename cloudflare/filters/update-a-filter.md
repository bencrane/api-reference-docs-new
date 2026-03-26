# Update a filter

`PUT /zones/{zone_id}/filters/{filter_id}`

> **Deprecated**

Updates an existing filter.

## Parameters

- **filter_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An informative summary of the filter.
- **expression** (string, optional): The filter expression. For more information, refer to [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
- **id** (string, optional): The unique identifier of the filter.
- **paused** (boolean, optional): When true, indicates that the filter is currently paused.
- **ref** (string, optional): A short reference tag. Allows you to select related filters.

## Response

### 200

Update a filter response

- **result** (object, optional): 

### 4XX

Update a filter response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`

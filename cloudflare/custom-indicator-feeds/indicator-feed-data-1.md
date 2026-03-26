# Download indicator feed data

`GET /accounts/{account_id}/intel/indicator-feeds/{feed_id}/download`

Downloads the content of a custom threat indicator feed.

## Parameters

- **account_id** (string, required) [path]: 
- **feed_id** (string, required) [path]: 

## Response

### 200

Get indicator feed metadata

- **result** (object, optional): 

### 4XX

Get indicator feeds response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

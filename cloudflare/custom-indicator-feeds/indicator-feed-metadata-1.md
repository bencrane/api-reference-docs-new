# Update indicator feed metadata

`PUT /accounts/{account_id}/intel/indicator-feeds/{feed_id}`

Revises details for a specific custom threat indicator feed.

## Parameters

- **account_id** (string, required) [path]: 
- **feed_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): The new description of the feed
- **is_attributable** (boolean, optional): The new is_attributable value of the feed
- **is_downloadable** (boolean, optional): The new is_downloadable value of the feed
- **is_public** (boolean, optional): The new is_public value of the feed
- **name** (string, optional): The new name of the feed

## Response

### 200

Get update public field response

- **result** (object, optional): 

### 4XX

Get update public field response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`

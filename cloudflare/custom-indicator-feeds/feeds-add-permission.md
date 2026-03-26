# Grant permission to indicator feed

`PUT /accounts/{account_id}/intel/indicator-feeds/permissions/add`

Grants access permissions for a custom threat indicator feed to other accounts.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **account_tag** (string, optional): The Cloudflare account tag of the account to change permissions on
- **feed_id** (integer, optional): The ID of the feed to add/remove permissions on

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

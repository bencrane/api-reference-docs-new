# Delete webhooks

`DELETE /accounts/{account_id}/stream/webhook`

Deletes a webhook.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Delete webhooks response.

- **result** (string, optional): 

### 4XX

Delete webhooks response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Removes a tag from an event

`DELETE /accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **event_id** (string, required) [path]: Event UUID.

## Request Body

- **tags** (array, required): 

## Response

### 200

Returns success if operation succeeded.

- **result** (object): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

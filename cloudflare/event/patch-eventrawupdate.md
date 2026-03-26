# Updates a raw event

`PATCH /accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **event_id** (string, required) [path]: Event UUID.
- **raw_id** (string, required) [path]: Raw Event UUID.

## Request Body

- **data** (object, optional): 
- **source** (string, optional): 
- **tlp** (string, optional): 

## Response

### 200

Returns the uuid of the updated raw event and its data.

- **data** (object): 
- **id** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

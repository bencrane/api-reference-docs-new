# Reads data for a raw event

`GET /accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **event_id** (string, required) [path]: Event UUID.
- **raw_id** (string, required) [path]: Raw Event UUID.

## Response

### 200

Returns the raw event.

- **accountId** (number): 
- **created** (string): 
- **data** (object): 
- **id** (string): 
- **source** (string): 
- **tlp** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

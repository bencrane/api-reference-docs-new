# Reads raw data for an event by UUID

`GET /accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}`

Retrieves the raw data associated with an event. Searches across all shards in the dataset.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **event_id** (string, required) [path]: Event ID.
- **dataset_id** (string, required) [path]: Dataset ID.

## Response

### 200

Returns the raw event data.

- **accountId** (number): 
- **created** (string): 
- **data** (string): 
- **id** (number): 
- **source** (string): 
- **tlp** (string): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

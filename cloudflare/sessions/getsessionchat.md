# Fetch all chat messages of a session

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat`

Returns a URL to download all chat messages of the session ID in CSV format.


## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **session_id** (string, required) [path]: ID of the session

## Response

### 200

Returns all chat messages of a session.

- **data** (object): 
- **success** (boolean):

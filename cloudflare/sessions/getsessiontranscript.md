# Fetch the complete transcript for a session

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript`

Returns a URL to download the transcript for the session ID in CSV format.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **session_id** (string, required) [path]: ID of the session

## Response

### 200

Returns the complete transcript of a session.

- **data** (object): 
- **success** (boolean):

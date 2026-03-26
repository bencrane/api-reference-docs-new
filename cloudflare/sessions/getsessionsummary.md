# Fetch summary of transcripts for a session

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary`

Returns a Summary URL to download the Summary of Transcripts for the session ID as plain text.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **session_id** (string, required) [path]: 

## Response

### 200

Returns a complete summary of transcripts of a session.

- **data** (object): 
- **success** (boolean):

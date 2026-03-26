# Fetch details of a session

`GET /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}`

Returns data of the given session ID including recording details.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **include_breakout_rooms** (boolean, optional) [query]: List all breakout rooms
- **session_id** (string, required) [path]: ID of the session

## Response

### 200

Get details about a particular session

- **data** (object): 
- **success** (boolean):

# Kick all participants

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all`

Kicks all participants from an active session for the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting

## Response

### 200

Kick all participants from a meeting

- **data** (object): 
- **success** (boolean):

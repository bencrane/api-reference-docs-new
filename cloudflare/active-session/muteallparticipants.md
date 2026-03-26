# Mute all participants

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/mute-all`

Mutes all participants of an active session for the given meeting ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting

## Request Body

- **allow_unmute** (boolean, required): if false, participants won't be able to unmute themselves after they are muted

## Response

### 200

Mute all participants of a meeting

- **data** (object): 
- **success** (boolean):

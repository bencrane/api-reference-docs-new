# Mute participants of an active session

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/mute`

Mutes one or more participants from an active session using user ID or custom participant ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting

## Request Body

- **custom_participant_ids** (array, required): 
- **participant_ids** (array, required): 

## Response

### 200

Mute one or more participants of a meeting

- **data** (object): 
- **success** (boolean):

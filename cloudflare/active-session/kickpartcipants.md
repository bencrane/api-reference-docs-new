# Kick participants from an active session

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick`

Kicks one or more participants from an active session using user ID or custom participant ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **meeting_id** (string, required) [path]: ID of the meeting

## Request Body

- **custom_participant_ids** (array, required): 
- **participant_ids** (array, required): 

## Response

### 200

Kick participants success response

- **data** (object): 
- **success** (boolean): 

### 404

No participant found for the given `participant_id` or `custom_participant_id`

- **error** (object): 
- **success** (boolean): Success status of the request.

# Fetch details of an active session

`GET /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session`

Returns details of an ongoing active session for the given meeting ID.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting

## Response

### 200

Active Session Success response

- **data** (object): 
- **success** (boolean): 

### 404

Active Session is not found for the given meetingId

- **error** (object): 
- **success** (boolean): Success status of the request.

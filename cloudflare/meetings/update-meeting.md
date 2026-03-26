# Update a meeting

`PATCH /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}`

Updates a meeting in an App for the given meeting ID.

## Parameters

- **meeting_id** (string, required) [path]: ID of the meeting. Fetch the meeting ID using the create a meeting API.

## Request Body

- **ai_config** (object, optional): The AI Config allows you to customize the behavior of meeting transcriptions and summaries
- **live_stream_on_start** (boolean, optional): Specifies if the meeting should start getting livestreamed on start.
- **persist_chat** (boolean, optional): If a meeting is updated to persist_chat, meeting chat would remain for a week within the meeting space.
- **record_on_start** (boolean, optional): Specifies if the meeting should start getting recorded as soon as someone joins the meeting.
- **session_keep_alive_time_in_secs** (number, optional): Time in seconds, for which a session remains active, after the last participant has left the meeting.
- **status** (string, optional): Whether the meeting is `ACTIVE` or `INACTIVE`. Users will not be able to join an `INACTIVE` meeting. Values: `ACTIVE`, `INACTIVE`
- **summarize_on_end** (boolean, optional): Automatically generate summary of meetings using transcripts. Requires Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.
- **title** (string, optional): Title of the meeting

## Response

### 200

Success Response

- **data** (object, optional): Data returned by the operation
- **success** (boolean, optional): Success status of the operation

### 500

Failure response

- **error** (object): 
- **success** (boolean): Success status of the request.

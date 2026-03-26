# Create a meeting

`POST /accounts/{account_id}/realtime/kit/{app_id}/meetings`

Create a meeting for the given App ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 

## Request Body

- **ai_config** (object, optional): The AI Config allows you to customize the behavior of meeting transcriptions and summaries
- **live_stream_on_start** (boolean, optional): Specifies if the meeting should start getting livestreamed on start.
- **persist_chat** (boolean, optional): If a meeting is set to persist_chat, meeting chat would remain for a week within the meeting space.
- **record_on_start** (boolean, optional): Specifies if the meeting should start getting recorded as soon as someone joins the meeting.
- **recording_config** (object, optional): Recording Configurations to be used for this meeting. This level of configs takes higher preference over App level configs on the RealtimeKit developer portal.

- **session_keep_alive_time_in_secs** (number, optional): Time in seconds, for which a session remains active, after the last participant has left the meeting.
- **summarize_on_end** (boolean, optional): Automatically generate summary of meetings using transcripts. Requires Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.
- **title** (string, optional): Title of the meeting

## Response

### 201

Success Response

- **data** (object, optional): Data returned by the operation
- **success** (boolean, optional): Success status of the operation

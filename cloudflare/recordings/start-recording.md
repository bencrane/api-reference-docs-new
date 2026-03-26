# Start recording a meeting

`POST /accounts/{account_id}/realtime/kit/{app_id}/recordings`

Starts recording a meeting. The meeting can be started by an App admin directly, or a participant with permissions to start a recording, based on the type of authorization used.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 

## Request Body

- **allow_multiple_recordings** (boolean, optional): By default, a meeting allows only one recording to run at a time. Enabling the `allow_multiple_recordings` parameter to true allows you to initiate multiple recordings concurrently in the same meeting. This allows you to record separate videos of the same meeting with different configurations, such as portrait mode or landscape mode.
- **audio_config** (object, optional): Object containing configuration regarding the audio that is being recorded.
- **file_name_prefix** (string, optional): Update the recording file name.
- **interactive_config** (object, optional): Allows you to add timed metadata to your recordings, which are digital markers inserted into a video file to provide contextual information at specific points in the content range. The ID3 tags containing this information are available to clients on the playback timeline in HLS format. The output files are generated in a compressed .tar format.
- **max_seconds** (integer, optional): Specifies the maximum duration for recording in seconds, ranging from a minimum of 60 seconds to a maximum of 24 hours.
- **meeting_id** (string, optional): ID of the meeting to record.
- **realtimekit_bucket_config** (object, optional): 
- **rtmp_out_config** (object, optional): 
- **storage_config** (object, optional): 
- **url** (string, optional): Pass a custom url to record arbitary screen
- **video_config** (object, optional): 

## Response

### 200

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation

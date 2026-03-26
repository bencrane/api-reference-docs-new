# Update a live input

`PUT /accounts/{account_id}/stream/live_inputs/{live_input_identifier}`

Updates a specified live input.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **defaultCreator** (string, optional): Sets the creator ID asssociated with this live input.
- **deleteRecordingAfterDays** (number, optional): Indicates the number of days after which the live inputs recordings will be deleted. When a stream completes and the recording is ready, the value is used to calculate a scheduled deletion date for that recording. Omit the field to indicate no change, or include with a `null` value to remove an existing scheduled deletion.
- **enabled** (boolean, optional): Indicates whether the live input is enabled and can accept streams.
- **meta** (object, optional): A user modifiable key-value store used to reference other systems of record for managing live inputs.
- **recording** (object, optional): Records the input to a Cloudflare Stream video. Behavior depends on the mode. In most cases, the video will initially be viewable as a live video and transition to on-demand after a condition is satisfied.

## Response

### 200

Update a live input response.

- **result** (object, optional): Details about a live input.

### 4XX

Update a live input response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

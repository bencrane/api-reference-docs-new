# Create a new output, connected to a live input

`POST /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs`

Creates a new output that can be used to simulcast or restream live video to other RTMP or SRT destinations. Outputs are always linked to a specific live input — one live input can have many outputs.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): When enabled, live video streamed to the associated live input will be sent to the output URL. When disabled, live video will not be sent to the output URL, even when streaming to the associated live input. Use this to control precisely when you start and stop simulcasting to specific destinations like YouTube and Twitch.
- **streamKey** (string, required): The streamKey used to authenticate against an output's target.
- **url** (string, required): The URL an output uses to restream.

## Response

### 200

Create a new output, connected to a live input response.

- **result** (object, optional): 

### 4XX

Create a new output, connected to a live input response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

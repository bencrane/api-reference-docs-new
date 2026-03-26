# Clip videos given a start and end time

`POST /accounts/{account_id}/stream/clip`

Clips a video based on the specified start and end times provided in seconds.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **allowedOrigins** (array, optional): Lists the origins allowed to display the video. Enter allowed origin domains in an array and use `*` for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.
- **clippedFromVideoUID** (string, required): The unique video identifier (UID).
- **creator** (string, optional): A user-defined identifier for the media creator.
- **endTimeSeconds** (integer, required): Specifies the end time for the video clip in seconds.
- **maxDurationSeconds** (integer, optional): The maximum duration in seconds for a video upload. Can be set for a video that is not yet uploaded to limit its duration. Uploads that exceed the specified duration will fail during processing. A value of `-1` means the value is unknown.
- **requireSignedURLs** (boolean, optional): Indicates whether the video can be a accessed using the UID. When set to `true`, a signed token must be generated with a signing key to view the video.
- **startTimeSeconds** (integer, required): Specifies the start time for the video clip in seconds.
- **thumbnailTimestampPct** (number, optional): The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video.  If this value is not set, the default thumbnail image is taken from 0s of the video.
- **watermark** (object, optional): 

## Response

### 200

Clip videos given a start and end time response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Clip videos given a start and end time response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

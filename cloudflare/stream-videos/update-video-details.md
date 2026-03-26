# Edit video details

`POST /accounts/{account_id}/stream/{identifier}`

Edit details for a single video.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **allowedOrigins** (array, optional): Lists the origins allowed to display the video. Enter allowed origin domains in an array and use `*` for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.
- **creator** (string, optional): A user-defined identifier for the media creator.
- **maxDurationSeconds** (integer, optional): The maximum duration in seconds for a video upload. Can be set for a video that is not yet uploaded to limit its duration. Uploads that exceed the specified duration will fail during processing. A value of `-1` means the value is unknown.
- **meta** (object, optional): A user modifiable key-value store used to reference other systems of record for managing videos.
- **requireSignedURLs** (boolean, optional): Indicates whether the video can be a accessed using the UID. When set to `true`, a signed token must be generated with a signing key to view the video.
- **scheduledDeletion** (string, optional): Indicates the date and time at which the video will be deleted. Omit the field to indicate no change, or include with a `null` value to remove an existing scheduled deletion. If specified, must be at least 30 days from upload time.
- **thumbnailTimestampPct** (number, optional): The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video.  If this value is not set, the default thumbnail image is taken from 0s of the video.
- **uploadExpiry** (string, optional): The date and time when the video upload URL is no longer valid for direct user uploads.

## Response

### 200

Edit video details response.

- **result** (object, optional): 

### 4XX

Edit video details response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Add audio tracks to a video

`POST /accounts/{account_id}/stream/{identifier}/audio/copy`

Adds an additional audio track to a video using the provided audio track URL.

## Parameters

- **account_id** (string, required) [path]: 
- **identifier** (string, required) [path]: 

## Request Body

- **label** (string, required): A string to uniquely identify the track amongst other audio track labels for the specified video.
- **url** (string, optional): An audio track URL. The server must be publicly routable and support `HTTP HEAD` requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD` requests with a `content-range` header that includes the size of the file.

## Response

### 200

Add audio tracks to a video.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Add audio tracks to a video response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

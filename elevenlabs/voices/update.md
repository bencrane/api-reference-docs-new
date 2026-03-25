# Edit Voice

**POST** `https://api.elevenlabs.io/v1/voices/{voice_id}/edit`
**Content-Type:** `multipart/form-data`

Edit a voice created by you.

## Path Parameters

- **voice_id** (string, required): ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint to list all available voices.

## Header Parameters

- **xi-api-key** (string, optional): API authentication key

## Request Body

The request accepts multipart form data with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | The name that identifies this voice. This will be displayed in the dropdown of the website. |
| files | array of binary | No | Audio files to add to the voice |
| remove_background_noise | boolean | No | If set will remove background noise for voice samples using the audio isolation model. If the samples do not include background noise, it can make the quality worse. Default: false |
| description | string | No | A description of the voice. |
| labels | object or string | No | Labels for the voice. Keys can be language, accent, gender, or age. |

## Response

### 200 - Successful Response

Returns an `EditVoiceResponseModel`:

```json
{
  "status": "string"
}
```

The status will be "ok" if the request was successful. Otherwise an error message with status 500 will be returned.

### 422 - Validation Error

Returns HTTP validation error details.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Code Examples

### TypeScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.update("21m00Tcm4TlvDq8ikWAM", {});
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.update(
    voice_id="21m00Tcm4TlvDq8ikWAM",
    files=["example_files"],
)
```

### Go
```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {
	url := "https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/edit"
	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nname\r\n-----011000010111000001101001--\r\n")
	req, _ := http.NewRequest("POST", url, payload)
	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)
	fmt.Println(res)
	fmt.Println(string(body))
}
```

### Ruby
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/edit")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nname\r\n-----011000010111000001101001--\r\n"
response = http.request(request)
puts response.read_body
```

### Java
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/edit")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nname\r\n-----011000010111000001101001--\r\n")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();
$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/edit', [
  'multipart' => [
    [
        'name' => 'name',
        'contents' => 'name'
    ]
  ]
]);
echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/edit");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nname\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/edit")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

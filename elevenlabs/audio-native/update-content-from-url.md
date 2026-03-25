# Update Audio-Native Content From Url

POST https://api.elevenlabs.io/v1/audio-native/content
Content-Type: application/json

Finds an AudioNative project matching the provided URL, extracts content from the URL, updates the project content, and queues it for conversion and auto-publishing.

Reference: https://elevenlabs.io/docs/api-reference/audio-native/update-content-from-url

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/audio-native/content:
    post:
      operationId: update-content-from-url
      summary: Update Audio-Native Content From Url
      description: >-
        Finds an AudioNative project matching the provided URL, extracts content
        from the URL, updates the project content, and queues it for conversion
        and auto-publishing.
      tags:
        - subpackage_audioNative
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:AudioNativeEditContentResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: URL of the page to extract content from.
                author:
                  type: string
                  description: >-
                    Author used in the player and inserted at the start of the
                    uploaded article. If not provided, the default author set in
                    the Player settings is used.
                title:
                  type: string
                  description: >-
                    Title used in the player and inserted at the top of the
                    uploaded article. If not provided, the default title set in
                    the Player settings is used.
              required:
                - url
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_:AudioNativeEditContentResponseModel:
      type: object
      properties:
        project_id:
          type: string
          description: The ID of the project.
        converting:
          type: boolean
          description: Whether the project is currently being converted.
        publishing:
          type: boolean
          description: Whether the project is currently being published.
        html_snippet:
          type: string
          description: The HTML snippet to embed the Audio Native player.
      required:
        - project_id
        - converting
        - publishing
        - html_snippet
      title: AudioNativeEditContentResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.audioNative.updateContentFromUrl({
        url: "https://elevenlabs.io/blog/the_first_ai_that_can_laugh/",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_native.update_content_from_url(
    url="https://elevenlabs.io/blog/the_first_ai_that_can_laugh/",
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/audio-native/content"

	payload := strings.NewReader("{\n  \"url\": \"https://elevenlabs.io/blog/the_first_ai_that_can_laugh/\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/audio-native/content")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://elevenlabs.io/blog/the_first_ai_that_can_laugh/\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/audio-native/content")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://elevenlabs.io/blog/the_first_ai_that_can_laugh/\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/audio-native/content', [
  'body' => '{
  "url": "https://elevenlabs.io/blog/the_first_ai_that_can_laugh/"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-native/content");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://elevenlabs.io/blog/the_first_ai_that_can_laugh/\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["url": "https://elevenlabs.io/blog/the_first_ai_that_can_laugh/"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-native/content")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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

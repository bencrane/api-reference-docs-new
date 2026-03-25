# Get Audio Native Project Settings

GET https://api.elevenlabs.io/v1/audio-native/{project_id}/settings

Get player settings for the specific project.

Reference: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/audio-native/{project_id}/settings:
    get:
      operationId: get-settings
      summary: Get Audio Native Project Settings
      description: Get player settings for the specific project.
      tags:
        - subpackage_audioNative
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
          required: true
          schema:
            type: string
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
                $ref: >-
                  #/components/schemas/type_:GetAudioNativeProjectSettingsResponseModel
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_:AudioNativeProjectSettingsResponseModelStatus:
      type: string
      enum:
        - processing
        - ready
      default: ready
      description: Current state of the project
      title: AudioNativeProjectSettingsResponseModelStatus
    type_:AudioNativeProjectSettingsResponseModel:
      type: object
      properties:
        title:
          type: string
          description: The title of the project.
        image:
          type: string
          description: The image of the project.
        author:
          type: string
          description: The author of the project.
        small:
          type: boolean
          description: Whether the project is small.
        text_color:
          type: string
          description: The text color of the project.
        background_color:
          type: string
          description: The background color of the project.
        sessionization:
          type: integer
          description: >-
            The sessionization of the project. Specifies for how many minutes to
            persist the session across page reloads.
        audio_path:
          type: string
          description: The path of the audio file.
        audio_url:
          type: string
          description: The URL of the audio file.
        status:
          $ref: >-
            #/components/schemas/type_:AudioNativeProjectSettingsResponseModelStatus
          description: Current state of the project
      required:
        - title
        - image
        - author
        - small
        - text_color
        - background_color
        - sessionization
      title: AudioNativeProjectSettingsResponseModel
    type_:GetAudioNativeProjectSettingsResponseModel:
      type: object
      properties:
        enabled:
          type: boolean
          description: Whether the project is enabled.
        snapshot_id:
          type: string
          description: The ID of the latest snapshot of the project.
        settings:
          $ref: '#/components/schemas/type_:AudioNativeProjectSettingsResponseModel'
          description: The settings of the project.
      required:
        - enabled
      title: GetAudioNativeProjectSettingsResponseModel
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
    await client.audioNative.getSettings("21m00Tcm4TlvDq8ikWAM");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_native.get_settings(
    project_id="21m00Tcm4TlvDq8ikWAM",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/audio-native/21m00Tcm4TlvDq8ikWAM/settings"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/audio-native/21m00Tcm4TlvDq8ikWAM/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/audio-native/21m00Tcm4TlvDq8ikWAM/settings")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/audio-native/21m00Tcm4TlvDq8ikWAM/settings');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-native/21m00Tcm4TlvDq8ikWAM/settings");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-native/21m00Tcm4TlvDq8ikWAM/settings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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

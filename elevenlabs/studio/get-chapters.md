# List Chapters

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters

Returns a list of a Studio project's chapters.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-chapters

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/chapters:
    get:
      operationId: list
      summary: List Chapters
      description: Returns a list of a Studio project's chapters.
      tags:
        - >-
          subpackage_studio.subpackage_studio/projects.subpackage_studio/projects/chapters
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
                $ref: '#/components/schemas/type_:GetChaptersResponse'
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
    type_:ChapterState:
      type: string
      enum:
        - default
        - converting
      description: The state of the chapter.
      title: ChapterState
    type_:VoiceStatisticsResponseModel:
      type: object
      properties:
        voice_id:
          type: string
          description: The voice ID.
        characters_unconverted:
          type: integer
          description: The number of unconverted characters for this voice.
        characters_converted:
          type: integer
          description: The number of converted characters for this voice.
      required:
        - voice_id
        - characters_unconverted
        - characters_converted
      title: VoiceStatisticsResponseModel
    type_:ChapterStatisticsResponse:
      type: object
      properties:
        characters_unconverted:
          type: integer
          description: The number of unconverted characters.
        characters_converted:
          type: integer
          description: The number of converted characters.
        paragraphs_converted:
          type: integer
          description: The number of converted paragraphs.
        paragraphs_unconverted:
          type: integer
          description: The number of unconverted paragraphs.
        voice_statistics:
          type: array
          items:
            $ref: '#/components/schemas/type_:VoiceStatisticsResponseModel'
          description: Per-voice breakdown of character counts.
      required:
        - characters_unconverted
        - characters_converted
        - paragraphs_converted
        - paragraphs_unconverted
      title: ChapterStatisticsResponse
    type_:ChapterResponse:
      type: object
      properties:
        chapter_id:
          type: string
          description: The ID of the chapter.
        name:
          type: string
          description: The name of the chapter.
        last_conversion_date_unix:
          type: integer
          description: The last conversion date of the chapter.
        conversion_progress:
          type: number
          format: double
          description: The conversion progress of the chapter.
        can_be_downloaded:
          type: boolean
          description: Whether the chapter can be downloaded.
        state:
          $ref: '#/components/schemas/type_:ChapterState'
          description: The state of the chapter.
        has_video:
          type: boolean
          description: Whether the chapter has a video.
        has_visual_content:
          type: boolean
          description: >-
            Whether the chapter has any visual content (video, image, or text
            clips).
        voice_ids:
          type: array
          items:
            type: string
          description: List of voice ids used by the chapter
        statistics:
          $ref: '#/components/schemas/type_:ChapterStatisticsResponse'
          description: The statistics of the chapter.
        last_conversion_error:
          type: string
          description: The last conversion error of the chapter.
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
      title: ChapterResponse
    type_:GetChaptersResponse:
      type: object
      properties:
        chapters:
          type: array
          items:
            $ref: '#/components/schemas/type_:ChapterResponse'
      required:
        - chapters
      title: GetChaptersResponse
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

### TypeScript

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.chapters.list("21m00Tcm4TlvDq8ikWAM");
}
main();
```

### Python

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.list(
    project_id="21m00Tcm4TlvDq8ikWAM",
)
```

### Go

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

### Java

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters")
  .asString();
```

### PHP

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters');

echo $response->getBody();
```

### C#

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

### Swift

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters")! as URL,
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

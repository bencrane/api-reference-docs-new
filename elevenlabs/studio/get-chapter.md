# Get Chapter

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}

The endpoint "Returns information about a specific chapter."

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}:
    get:
      operationId: get
      summary: Get Chapter
      description: Returns information about a specific chapter.
      tags:
        - >-
          subpackage_studio.subpackage_studio/projects.subpackage_studio/projects/chapters
      parameters:
        - name: project_id
          in: path
          description: >-
            The ID of the project to be used. You can use the [List
            projects](/docs/api-reference/studio/get-projects) endpoint to list
            all the available projects.
          required: true
          schema:
            type: string
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/type_:ChapterWithContentResponseModel'
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
    type_:ChapterWithContentResponseModelState:
      type: string
      enum:
        - default
        - converting
      description: The state of the chapter.
      title: ChapterWithContentResponseModelState
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
    type_:ChapterContentBlockResponseModelNodesItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - tts_node
              description: 'Discriminator value: tts_node'
            voice_id:
              type: string
            text:
              type: string
          required:
            - type
            - voice_id
            - text
        - type: object
          properties:
            type:
              type: string
              enum:
                - _other
              description: 'Discriminator value: _other'
          required:
            - type
      discriminator:
        propertyName: type
      title: ChapterContentBlockResponseModelNodesItem
    type_:ChapterContentBlockResponseModel:
      type: object
      properties:
        block_id:
          type: string
        nodes:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ChapterContentBlockResponseModelNodesItem
      required:
        - block_id
        - nodes
      title: ChapterContentBlockResponseModel
    type_:ChapterContentResponseModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/type_:ChapterContentBlockResponseModel'
      required:
        - blocks
      title: ChapterContentResponseModel
    type_:ChapterWithContentResponseModel:
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
          $ref: '#/components/schemas/type_:ChapterWithContentResponseModelState'
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
        content:
          $ref: '#/components/schemas/type_:ChapterContentResponseModel'
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
        - content
      title: ChapterWithContentResponseModel
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
    await client.studio.projects.chapters.get("21m00Tcm4TlvDq8ikWAM", "21m00Tcm4TlvDq8ikWAM");
}
main();
```

### Python

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.get(
    project_id="21m00Tcm4TlvDq8ikWAM",
    chapter_id="21m00Tcm4TlvDq8ikWAM",
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

	url := "https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters/21m00Tcm4TlvDq8ikWAM"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters/21m00Tcm4TlvDq8ikWAM")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters/21m00Tcm4TlvDq8ikWAM")
  .asString();
```

### PHP

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters/21m00Tcm4TlvDq8ikWAM');

echo $response->getBody();
```

### C#

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters/21m00Tcm4TlvDq8ikWAM");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

### Swift

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/chapters/21m00Tcm4TlvDq8ikWAM")! as URL,
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

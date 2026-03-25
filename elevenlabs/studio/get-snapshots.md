# List Studio Project Snapshots

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots

Retrieves a list of snapshots for a Studio project.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-snapshots

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/snapshots:
    get:
      operationId: list
      summary: List Studio Project Snapshots
      description: Retrieves a list of snapshots for a Studio project.
      tags:
        - >-
          subpackage_studio.subpackage_studio/projects.subpackage_studio/projects/snapshots
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
                $ref: '#/components/schemas/type_:ProjectSnapshotsResponse'
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
    type_:ProjectSnapshotResponse:
      type: object
      properties:
        project_snapshot_id:
          type: string
          description: The ID of the project snapshot.
        project_id:
          type: string
          description: The ID of the project.
        created_at_unix:
          type: integer
          description: The creation date of the project snapshot.
        name:
          type: string
          description: The name of the project snapshot.
        audio_upload:
          type: object
          additionalProperties:
            description: Any type
          description: (Deprecated)
        zip_upload:
          type: object
          additionalProperties:
            description: Any type
          description: (Deprecated)
      required:
        - project_snapshot_id
        - project_id
        - created_at_unix
        - name
      title: ProjectSnapshotResponse
    type_:ProjectSnapshotsResponse:
      type: object
      properties:
        snapshots:
          type: array
          items:
            $ref: '#/components/schemas/type_:ProjectSnapshotResponse'
          description: List of project snapshots.
      required:
        - snapshots
      title: ProjectSnapshotsResponse
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
    await client.studio.projects.snapshots.list("21m00Tcm4TlvDq8ikWAM");
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.snapshots.list(
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

	url := "https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/snapshots"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/snapshots")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/snapshots")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/snapshots');

echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/snapshots");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/21m00Tcm4TlvDq8ikWAM/snapshots")! as URL,
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

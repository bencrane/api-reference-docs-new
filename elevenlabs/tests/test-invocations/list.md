# List Test Invocations

GET https://api.elevenlabs.io/v1/convai/test-invocations

Lists all test invocations with pagination support and optional search filtering.

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/test-invocations:
    get:
      operationId: list
      summary: List Test Invocations
      description: >-
        Lists all test invocations with pagination support and optional search
        filtering.
      tags:
        - >-
          subpackage_conversationalAi.subpackage_conversationalAi/tests.subpackage_conversationalAi/tests/invocations
      parameters:
        - name: agent_id
          in: query
          description: Filter by agent ID
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            How many Tests to return at maximum. Can not exceed 100, defaults to
            30.
          required: false
          schema:
            type: integer
            default: 30
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
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
                $ref: '#/components/schemas/type_:GetTestInvocationsPageResponseModel'
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
    type_:ListResponseMeta:
      type: object
      properties:
        total:
          type: integer
        page:
          type: integer
        page_size:
          type: integer
      title: ListResponseMeta
    type_:ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    type_:ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
          description: Whether the user making the request is the creator of the agent
        creator_name:
          type: string
          description: Name of the agent's creator
        creator_email:
          type: string
          description: Email of the agent's creator
        role:
          $ref: '#/components/schemas/type_:ResourceAccessInfoRole'
          description: The role of the user making the request
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
      title: ResourceAccessInfo
    type_:TestInvocationSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the test invocation
        agent_id:
          type: string
          description: The ID of the agent this test invocation belongs to
        branch_id:
          type: string
          description: The ID of the branch this test invocation was run on
        created_at_unix_secs:
          type: integer
          description: Creation time of the test invocation in unix seconds
        test_run_count:
          type: integer
          description: Number of test runs in this invocation
        passed_count:
          type: integer
          description: Number of test runs that passed
        failed_count:
          type: integer
          description: Number of test runs that failed
        pending_count:
          type: integer
          description: Number of test runs that are pending
        title:
          type: string
          description: >-
            Title of the test invocation - either the single test name or count
            of tests
        access_info:
          $ref: '#/components/schemas/type_:ResourceAccessInfo'
          description: The access information of the test invocation
      required:
        - id
        - created_at_unix_secs
        - test_run_count
        - passed_count
        - failed_count
        - pending_count
        - title
      title: TestInvocationSummaryResponseModel
    type_:GetTestInvocationsPageResponseModel:
      type: object
      properties:
        meta:
          $ref: '#/components/schemas/type_:ListResponseMeta'
        results:
          type: array
          items:
            $ref: '#/components/schemas/type_:TestInvocationSummaryResponseModel'
        next_cursor:
          type: string
          description: Cursor for the next page of results
        has_more:
          type: boolean
          description: Whether there are more results available
      required:
        - results
        - has_more
      title: GetTestInvocationsPageResponseModel
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
    await client.conversationalAi.tests.invocations.list({
        agentId: "agent_id",
        pageSize: 1,
        cursor: "cursor",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.invocations.list(
    agent_id="agent_id",
    page_size=1,
    cursor="cursor",
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

	url := "https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id&page_size=1&cursor=cursor"

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

url = URI("https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id&page_size=1&cursor=cursor")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id&page_size=1&cursor=cursor")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id&page_size=1&cursor=cursor');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id&page_size=1&cursor=cursor");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/test-invocations?agent_id=agent_id&page_size=1&cursor=cursor")! as URL,
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

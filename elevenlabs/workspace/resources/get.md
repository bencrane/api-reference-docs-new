# Get Resource

GET https://api.elevenlabs.io/v1/workspace/resources/{resource_id}

Gets the metadata of a resource by ID.

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/resources/{resource_id}:
    get:
      operationId: get
      summary: Get Resource
      description: Gets the metadata of a resource by ID.
      tags:
        - subpackage_workspace.subpackage_workspace/resources
      parameters:
        - name: resource_id
          in: path
          description: The ID of the target resource.
          required: true
          schema:
            type: string
        - name: resource_type
          in: query
          description: Resource type of the target resource.
          required: true
          schema:
            $ref: '#/components/schemas/type_:WorkspaceResourceType'
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
                $ref: '#/components/schemas/type_:ResourceMetadataResponseModel'
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
    type_:WorkspaceResourceType:
      type: string
      enum:
        - voice
        - voice_collection
        - pronunciation_dictionary
        - dubbing
        - project
        - convai_agents
        - convai_knowledge_base_documents
        - convai_tools
        - convai_settings
        - convai_secrets
        - workspace_auth_connections
        - convai_phone_numbers
        - convai_mcp_servers
        - convai_api_integration_connections
        - convai_api_integration_trigger_connections
        - convai_batch_calls
        - convai_agent_response_tests
        - convai_test_suite_invocations
        - convai_crawl_jobs
        - convai_crawl_tasks
        - convai_whatsapp_accounts
        - convai_agent_versions
        - convai_agent_branches
        - convai_agent_versions_deployments
        - convai_memory_entries
        - convai_coaching_proposals
        - dashboard
        - dashboard_configuration
        - convai_agent_drafts
        - resource_locators
        - assets
        - content_generations
        - content_templates
        - songs
      description: >-
        Resource types that can be shared in the workspace. The name always need
        to match the collection names
      title: WorkspaceResourceType
    type_:ResourceMetadataResponseModelAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: ResourceMetadataResponseModelAnonymousAccessLevelOverride
    type_:ShareOptionResponseModelType:
      type: string
      enum:
        - user
        - group
        - key
      description: >-
        The type of the principal: user, group, or service account (under
        'key').
      title: ShareOptionResponseModelType
    type_:ShareOptionResponseModel:
      type: object
      properties:
        name:
          type: string
          description: The name of the principal.
        id:
          type: string
          description: The ID of the principal.
        type:
          $ref: '#/components/schemas/type_:ShareOptionResponseModelType'
          description: >-
            The type of the principal: user, group, or service account (under
            'key').
      required:
        - name
        - id
        - type
      title: ShareOptionResponseModel
    type_:ResourceMetadataResponseModel:
      type: object
      properties:
        resource_id:
          type: string
          description: The ID of the resource.
        resource_name:
          type: string
          description: The name of the resource, if available.
        resource_type:
          $ref: '#/components/schemas/type_:WorkspaceResourceType'
          description: The type of the resource.
        creator_user_id:
          type: string
          description: The ID of the user who created the resource.
        anonymous_access_level_override:
          $ref: >-
            #/components/schemas/type_:ResourceMetadataResponseModelAnonymousAccessLevelOverride
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        role_to_group_ids:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          description: >-
            A mapping of roles to group IDs. When the resource is shared with a
            user, the group id is the user's id.
        share_options:
          type: array
          items:
            $ref: '#/components/schemas/type_:ShareOptionResponseModel'
          description: >-
            List of options for sharing the resource further in the workspace.
            These are users who don't have access to the resource yet.
      required:
        - resource_id
        - resource_type
        - role_to_group_ids
        - share_options
      title: ResourceMetadataResponseModel
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
    await client.workspace.resources.get("resource_id", {
        resourceType: "voice",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.resources.get(
    resource_id="resource_id",
    resource_type="voice",
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

	url := "https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice"

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

url = URI("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")! as URL,
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

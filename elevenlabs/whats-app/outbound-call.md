# Outbound call via WhatsApp

POST https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call
Content-Type: application/json

Make an outbound call via WhatsApp

Reference: https://elevenlabs.io/docs/api-reference/whats-app/outbound-call

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/whatsapp/outbound-call:
    post:
      operationId: outbound-call
      summary: Make An Outbound Call Via Whatsapp
      description: Make an outbound call via WhatsApp
      tags:
        - subpackage_conversationalAi.subpackage_conversationalAi/whatsapp
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
                $ref: '#/components/schemas/type_:WhatsAppOutboundCallResponse'
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
                whatsapp_phone_number_id:
                  type: string
                whatsapp_user_id:
                  type: string
                whatsapp_call_permission_request_template_name:
                  type: string
                whatsapp_call_permission_request_template_language_code:
                  type: string
                agent_id:
                  type: string
                conversation_initiation_client_data:
                  $ref: >-
                    #/components/schemas/type_:ConversationInitiationClientDataRequestInput
              required:
                - whatsapp_phone_number_id
                - whatsapp_user_id
                - whatsapp_call_permission_request_template_name
                - whatsapp_call_permission_request_template_language_code
                - agent_id
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_:WhatsAppOutboundCallResponse:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
        conversation_id:
          type: string
      required:
        - success
        - message
      title: WhatsAppOutboundCallResponse
```

## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsapp.outboundCall({
        whatsappPhoneNumberId: "whatsapp_phone_number_id",
        whatsappUserId: "whatsapp_user_id",
        whatsappCallPermissionRequestTemplateName: "whatsapp_call_permission_request_template_name",
        whatsappCallPermissionRequestTemplateLanguageCode: "whatsapp_call_permission_request_template_language_code",
        agentId: "agent_id",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp.outbound_call(
    whatsapp_phone_number_id="whatsapp_phone_number_id",
    whatsapp_user_id="whatsapp_user_id",
    whatsapp_call_permission_request_template_name="whatsapp_call_permission_request_template_name",
    whatsapp_call_permission_request_template_language_code="whatsapp_call_permission_request_template_language_code",
    agent_id="agent_id",
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
	url := "https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call"
	payload := strings.NewReader("{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}")
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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}"
response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call")
  .header("Content-Type", "application/json")
  .body("{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();
$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call', [
  'body' => '{
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
  "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
  "agent_id": "agent_id"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);
echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
  "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
  "agent_id": "agent_id"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])
let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call")! as URL,
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

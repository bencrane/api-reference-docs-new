# Outbound message via WhatsApp

POST https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message
Content-Type: application/json

Send an outbound message via WhatsApp

Reference: https://elevenlabs.io/docs/api-reference/whats-app/outbound-message

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/whatsapp/outbound-message:
    post:
      operationId: outbound-message
      summary: Send An Outbound Message Via Whatsapp
      description: Send an outbound message via WhatsApp
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
                $ref: '#/components/schemas/type_:WhatsAppOutboundMessageResponse'
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
                template_name:
                  type: string
                template_language_code:
                  type: string
                template_params:
                  type: array
                  items:
                    $ref: '#/components/schemas/TemplateParamsItem'
                agent_id:
                  type: string
                conversation_initiation_client_data:
                  $ref: '#/components/schemas/type_:ConversationInitiationClientDataRequestInput'
              required:
                - whatsapp_phone_number_id
                - whatsapp_user_id
                - template_name
                - template_language_code
                - template_params
                - agent_id
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_:WhatsAppOutboundMessageResponse:
      type: object
      properties:
        conversation_id:
          type: string
      required:
        - conversation_id
      title: WhatsAppOutboundMessageResponse
    type_:WhatsAppTemplateTextParam:
      type: object
      properties:
        parameter_name:
          type: string
        type:
          type: string
          enum:
            - text
        text:
          type: string
      required:
        - text
      title: WhatsAppTemplateTextParam
    TemplateParamsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - body
            parameters:
              type: array
              items:
                $ref: '#/components/schemas/type_:WhatsAppTemplateTextParam'
          required:
            - type
            - parameters
        - type: object
          properties:
            type:
              type: string
              enum:
                - button
            parameters:
              type: array
              items:
                $ref: '#/components/schemas/type_:WhatsAppTemplateTextParam'
            index:
              type: integer
            sub_type:
              type: string
          required:
            - type
            - parameters
            - index
            - sub_type
        - type: object
          properties:
            type:
              type: string
              enum:
                - header
            parameters:
              type: array
              items:
                $ref: '#/components/schemas/WhatsAppTemplateHeaderComponentParamsParametersItem'
          required:
            - type
            - parameters
      discriminator:
        propertyName: type
```

## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsapp.outboundMessage({
        whatsappPhoneNumberId: "whatsapp_phone_number_id",
        whatsappUserId: "whatsapp_user_id",
        templateName: "template_name",
        templateLanguageCode: "template_language_code",
        templateParams: [
            {
                type: "body",
                parameters: [
                    {
                        text: "text",
                    },
                ],
            },
        ],
        agentId: "agent_id",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs, WhatsAppTemplateTextParam

client = ElevenLabs()

client.conversational_ai.whatsapp.outbound_message(
    whatsapp_phone_number_id="whatsapp_phone_number_id",
    whatsapp_user_id="whatsapp_user_id",
    template_name="template_name",
    template_language_code="template_language_code",
    template_params=[
        {
            "type": "body",
            "parameters": [
                WhatsAppTemplateTextParam(
                    text="text",
                )
            ]
        }
    ],
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
	url := "https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message"
	payload := strings.NewReader("{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"template_name\": \"template_name\",\n  \"template_language_code\": \"template_language_code\",\n  \"template_params\": [\n    {\n      \"type\": \"body\",\n      \"parameters\": [\n        {\n          \"text\": \"text\"\n        }\n      ]\n    }\n  ],\n  \"agent_id\": \"agent_id\"\n}")
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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"template_name\": \"template_name\",\n  \"template_language_code\": \"template_language_code\",\n  \"template_params\": [\n    {\n      \"type\": \"body\",\n      \"parameters\": [\n        {\n          \"text\": \"text\"\n        }\n      ]\n    }\n  ],\n  \"agent_id\": \"agent_id\"\n}"
response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message")
  .header("Content-Type", "application/json")
  .body("{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"template_name\": \"template_name\",\n  \"template_language_code\": \"template_language_code\",\n  \"template_params\": [\n    {\n      \"type\": \"body\",\n      \"parameters\": [\n        {\n          \"text\": \"text\"\n        }\n      ]\n    }\n  ],\n  \"agent_id\": \"agent_id\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();
$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message', [
  'body' => '{
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "template_name": "template_name",
  "template_language_code": "template_language_code",
  "template_params": [
    {
      "type": "body",
      "parameters": [
        {
          "text": "text"
        }
      ]
    }
  ],
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"template_name\": \"template_name\",\n  \"template_language_code\": \"template_language_code\",\n  \"template_params\": [\n    {\n      \"type\": \"body\",\n      \"parameters\": [\n        {\n          \"text\": \"text\"\n        }\n      ]\n    }\n  ],\n  \"agent_id\": \"agent_id\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "template_name": "template_name",
  "template_language_code": "template_language_code",
  "template_params": [
    [
      "type": "body",
      "parameters": [["text": "text"]]
    ]
  ],
  "agent_id": "agent_id"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])
let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message")! as URL,
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

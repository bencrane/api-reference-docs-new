# Get environment variable

GET https://api.elevenlabs.io/v1/convai/environment-variables/{env_var_id}

"Get a specific environment variable by ID"

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/environment-variables/{env_var_id}:
    get:
      operationId: get
      summary: Get Environment Variable
      description: Get a specific environment variable by ID
      tags:
        - subpackage_environmentVariables
      parameters:
        - name: env_var_id
          in: path
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
                $ref: '#/components/schemas/type_:EnvironmentVariableResponse'
        '404':
          description: Environment variable not found
          content:
            application/json:
              schema:
                description: Any type
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
    type_:EnvironmentVariableResponseType:
      type: string
      enum:
        - string
        - secret
        - auth_connection
      title: EnvironmentVariableResponseType
    type_:EnvironmentVariableSecretValue:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      title: EnvironmentVariableSecretValue
    type_:EnvironmentVariableAuthConnectionValue:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
      title: EnvironmentVariableAuthConnectionValue
    type_:EnvironmentVariableResponseValues:
      oneOf:
        - type: object
          additionalProperties:
            type: string
        - type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:EnvironmentVariableSecretValue'
        - type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:EnvironmentVariableAuthConnectionValue'
      title: EnvironmentVariableResponseValues
    type_:EnvironmentVariableResponse:
      type: object
      properties:
        label:
          type: string
        created_at_unix_secs:
          type: integer
        updated_at_unix_secs:
          type: integer
        created_by_user_id:
          type: string
        type:
          $ref: '#/components/schemas/type_:EnvironmentVariableResponseType'
        id:
          type: string
        workspace_id:
          type: string
        values:
          $ref: '#/components/schemas/type_:EnvironmentVariableResponseValues'
      required:
        - label
        - created_at_unix_secs
        - updated_at_unix_secs
        - type
        - id
        - workspace_id
        - values
      title: EnvironmentVariableResponse
```

## SDK Code Examples

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.get("env_var_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.environment_variables.get(
    env_var_id="env_var_id",
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
	url := "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id"
	payload := strings.NewReader("{}")
	req, _ := http.NewRequest("GET", url, payload)
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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"
response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);
echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]
let postData = JSONSerialization.data(withJSONObject: parameters, options: [])
let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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

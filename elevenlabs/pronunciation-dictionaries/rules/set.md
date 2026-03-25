# Set pronunciation dictionary rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/set-rules
Content-Type: application/json

Replaces all existing rules on the pronunciation dictionary with the provided ones.

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/set

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/set-rules:
    post:
      operationId: set
      summary: Set pronunciation dictionary rules
      description: >-
        Replaces all existing rules on the pronunciation dictionary with the
        provided ones.
      tags:
        - >-
          subpackage_pronunciationDictionaries.subpackage_pronunciationDictionaries/rules
      parameters:
        - name: pronunciation_dictionary_id
          in: path
          description: The id of the pronunciation dictionary
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
          description: Successfully set rules on the pronunciation dictionary
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_:PronunciationDictionaryRulesResponseModel
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
                rules:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/type_pronunciationDictionaries/rules:BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem
                  description: |-
                    List of pronunciation rules. Rule can be either:
                        an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                        or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }
              required:
                - rules
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_pronunciationDictionaries/rules:BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - alias
              description: 'Discriminator value: alias'
            string_to_replace:
              type: string
              description: The string to replace. Must be a non-empty string.
            case_sensitive:
              type: boolean
              default: true
              description: Whether the rule should match case-sensitively.
            word_boundaries:
              type: boolean
              default: true
              description: Whether the rule should only match at word boundaries.
            alias:
              type: string
              description: The alias for the string to be replaced.
          required:
            - type
            - string_to_replace
            - alias
        - type: object
          properties:
            type:
              type: string
              enum:
                - phoneme
              description: 'Discriminator value: phoneme'
            string_to_replace:
              type: string
              description: The string to replace. Must be a non-empty string.
            case_sensitive:
              type: boolean
              default: true
              description: Whether the rule should match case-sensitively.
            word_boundaries:
              type: boolean
              default: true
              description: Whether the rule should only match at word boundaries.
            phoneme:
              type: string
              description: The phoneme rule.
            alphabet:
              type: string
              description: The alphabet to use with the phoneme rule.
          required:
            - type
            - string_to_replace
            - phoneme
            - alphabet
      discriminator:
        propertyName: type
      title: >-
        BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem
    type_:PronunciationDictionaryRulesResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the pronunciation dictionary.
        version_id:
          type: string
          description: The version ID of the pronunciation dictionary.
        version_rules_num:
          type: integer
          description: The number of rules in the version of the pronunciation dictionary.
      required:
        - id
        - version_id
        - version_rules_num
      title: PronunciationDictionaryRulesResponseModel
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
    await client.pronunciationDictionaries.rules.set("21m00Tcm4TlvDq8ikWAM", {
        rules: [
            {
                type: "alias",
                alias: "tie-land",
                stringToReplace: "Thailand",
                caseSensitive: true,
                wordBoundaries: true,
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.rules.set(
    pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
    rules=[
        {
            "type": "alias",
            "alias": "tie-land",
            "string_to_replace": "Thailand",
            "case_sensitive": True,
            "word_boundaries": True
        }
    ],
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/21m00Tcm4TlvDq8ikWAM/set-rules"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"type\": \"alias\",\n      \"alias\": \"tie-land\",\n      \"string_to_replace\": \"Thailand\",\n      \"case_sensitive\": true,\n      \"word_boundaries\": true\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/21m00Tcm4TlvDq8ikWAM/set-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"type\": \"alias\",\n      \"alias\": \"tie-land\",\n      \"string_to_replace\": \"Thailand\",\n      \"case_sensitive\": true,\n      \"word_boundaries\": true\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/21m00Tcm4TlvDq8ikWAM/set-rules")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"type\": \"alias\",\n      \"alias\": \"tie-land\",\n      \"string_to_replace\": \"Thailand\",\n      \"case_sensitive\": true,\n      \"word_boundaries\": true\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/21m00Tcm4TlvDq8ikWAM/set-rules', [
  'body' => '{
  "rules": [
    {
      "type": "alias",
      "alias": "tie-land",
      "string_to_replace": "Thailand",
      "case_sensitive": true,
      "word_boundaries": true
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/21m00Tcm4TlvDq8ikWAM/set-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"type\": \"alias\",\n      \"alias\": \"tie-land\",\n      \"string_to_replace\": \"Thailand\",\n      \"case_sensitive\": true,\n      \"word_boundaries\": true\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["rules": [
    [
      "type": "alias",
      "alias": "tie-land",
      "string_to_replace": "Thailand",
      "case_sensitive": true,
      "word_boundaries": true
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/21m00Tcm4TlvDq8ikWAM/set-rules")! as URL,
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

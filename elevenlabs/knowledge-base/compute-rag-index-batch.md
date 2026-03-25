# Compute RAG Index in Batch

POST https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index
Content-Type: application/json

Retrieves and/or creates RAG indexes for multiple knowledge base documents in a single request. Maximum 100 items per request.

## Parameters

- **xi-api-key** (header, optional): API authentication key

## Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| items | array | Yes | List of requested RAG indexes. Minimum 1, maximum 100 items. |

Each item in the array contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| document_id | string | Yes | ID of the knowledgebase document for which to retrieve the index |
| create_if_missing | boolean | Yes | Whether to create the RAG index if it does not exist |
| model | EmbeddingModelEnum | Yes | Embedding model to use (e5_mistral_7b_instruct, multilingual_e5_large_instruct, qwen3_embedding_4b) |

## Response

### 200 - Successful Response

Returns an object with document IDs as keys, each containing either:

**Success:**
- `status`: "success"
- `data`: RagDocumentIndexResponseModel (id, model, status, progress_percentage, document_model_index_usage)

**Failure:**
- `status`: "failure"
- `error_code`: integer
- `error_status`: string
- `error_message`: string

### 422 - Validation Error

Returns detailed error information.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Code Examples

### TypeScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.getOrCreateRagIndexes({
        items: [
            {
                documentId: "document_id",
                createIfMissing: true,
                model: "e5_mistral_7b_instruct",
            },
        ],
    });
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs, GetOrCreateRagIndexRequestModel

client = ElevenLabs()

client.conversational_ai.knowledge_base.get_or_create_rag_indexes(
    items=[
        GetOrCreateRagIndexRequestModel(
            document_id="document_id",
            create_if_missing=True,
            model="e5_mistral_7b_instruct",
        )
    ],
)
```

### Go
```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {
	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index"
	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}")
	req, _ := http.NewRequest("POST", url, payload)
	req.Header.Add("Content-Type", "application/json")
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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

### Java
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index', [
  'body' => '{
  "items": [
    {
      "document_id": "document_id",
      "create_if_missing": true,
      "model": "e5_mistral_7b_instruct"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["items": [
    [
      "document_id": "document_id",
      "create_if_missing": true,
      "model": "e5_mistral_7b_instruct"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")! as URL,
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

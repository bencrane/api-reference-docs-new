# Get RAG Index

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index

Provides information about all RAG indexes of the specified knowledgebase document.

## Parameters

- **documentation_id** (path, required): The id of a document from the knowledge base. This is returned on document addition.
- **xi-api-key** (header, optional): API authentication key

## Response

### 200 - Successful Response

Returns a `RagDocumentIndexesResponseModel` containing:

- **indexes** (array, required): Array of `RagDocumentIndexResponseModel` objects

Each index object contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Index identifier |
| model | EmbeddingModelEnum | Yes | Embedding model used (e5_mistral_7b_instruct, multilingual_e5_large_instruct, qwen3_embedding_4b) |
| status | RagIndexStatus | Yes | Index status (new, created, processing, failed, succeeded, rag_limit_exceeded, document_too_small, cannot_index_folder) |
| progress_percentage | number (double) | Yes | Processing progress |
| document_model_index_usage | RagDocumentIndexUsage | Yes | Usage metrics with used_bytes |

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
    await client.conversationalAi.getDocumentRagIndexes("21m00Tcm4TlvDq8ikWAM");
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.get_document_rag_indexes(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
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
	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index"
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

### Ruby
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

### Java
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index")! as URL,
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

# Get Document Chunk

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/chunk/{chunk_id}

Get details about a specific documentation part used by RAG.

## Parameters

- **documentation_id** (path, required): The id of a document from the knowledge base. This is returned on document addition.
- **chunk_id** (path, required): The id of a document RAG chunk from the knowledge base.
- **embedding_model** (query, optional): The embedding model used to retrieve the chunk. Enum values: `e5_mistral_7b_instruct` (default), `multilingual_e5_large_instruct`, `qwen3_embedding_4b`
- **xi-api-key** (header, optional): API authentication key

## Response

### 200 - Successful Response

Returns a `KnowledgeBaseDocumentChunkResponseModel`:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Chunk identifier |
| name | string | Yes | Chunk name |
| content | string | Yes | Chunk content |

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
    await client.conversationalAi.knowledgeBase.documents.chunk.get("21m00Tcm4TlvDq8ikWAM", "chunk_id", {
        embeddingModel: "e5_mistral_7b_instruct",
    });
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.chunk.get(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
    chunk_id="chunk_id",
    embedding_model="e5_mistral_7b_instruct",
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
	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct"
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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct');

echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct")! as URL,
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

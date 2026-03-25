# Get user subscription

GET https://api.elevenlabs.io/v1/user/subscription

## Overview

This endpoint retrieves detailed subscription information for the authenticated user. The API returns extended data about the user's current plan, usage metrics, and billing details.

## Request Details

**HTTP Method:** GET

**Authentication:** Optional `xi-api-key` header (string)

**Available Servers:**
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Response Schema

The successful response (HTTP 200) returns a `Subscription` object containing:

**Core Subscription Data:**
- `tier` - Current subscription tier
- `status` - Subscription status (trialing, active, incomplete, past_due, free, free_disabled)
- `billing_period` - Billing cycle (monthly, 3-month, 6-month, annual)
- `character_refresh_period` - Character limit reset frequency
- `currency` - Billing currency (USD, EUR, INR)

**Usage Metrics:**
- `character_count` - Characters consumed in current period
- `character_limit` - Maximum allowed characters
- `voice_slots_used` - Number of voice slots in use
- `voice_limit` - Maximum voice slots permitted
- `professional_voice_slots_used` - Professional voice usage
- `voice_add_edit_counter` - Voice modification count

**Capability Flags:**
- `can_extend_character_limit` - Ability to increase character allowance
- `can_use_instant_voice_cloning` - Instant cloning access
- `can_use_professional_voice_cloning` - Professional cloning access

**Financial Information:**
- `next_invoice` - Upcoming invoice details
- `open_invoices` - Array of unpaid invoices
- `pending_change` - Scheduled subscription modifications

## Code Examples

**TypeScript/JavaScript:**
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.user.subscription.get();
}
main();
```

**Python:**
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()
client.user.subscription.get()
```

**Go:**
```go
package main

import (
	"fmt"
	"io"
	"net/http"
	"strings"
)

func main() {
	url := "https://api.elevenlabs.io/v1/user/subscription"
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

**Ruby:**
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/user/subscription")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"
response = http.request(request)
puts response.read_body
```

**Java:**
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user/subscription")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

**PHP:**
```php
<?php
require_once('vendor/autoload.php');
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user/subscription', [
  'body' => '{}',
  'headers' => ['Content-Type' => 'application/json'],
]);
echo $response->getBody();
```

**C#:**
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/user/subscription");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

**Swift:**
```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]
let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user/subscription")! as URL,
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

## Error Handling

HTTP 422 responses indicate validation errors, returning detailed error information in the response body.

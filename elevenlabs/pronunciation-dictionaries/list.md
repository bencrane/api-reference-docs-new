# List pronunciation dictionaries

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries

Get a list of the pronunciation dictionaries you have access to and their metadata

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries:
    get:
      operationId: list
      summary: List pronunciation dictionaries
      description: >-
        Get a list of the pronunciation dictionaries you have access to and
        their metadata
      tags:
        - subpackage_pronunciationDictionaries
      parameters:
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            How many pronunciation dictionaries to return at maximum. Can not
            exceed 100, defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: sort
          in: query
          description: Which field to sort by, one of 'created_at_unix' or 'name'.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_pronunciationDictionaries:PronunciationDictionariesListRequestSort
        - name: sort_direction
          in: query
          description: Which direction to sort the voices in. 'ascending' or 'descending'.
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
                $ref: >-
                  #/components/schemas/type_:GetPronunciationDictionariesMetadataResponseModel
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
    type_pronunciationDictionaries:PronunciationDictionariesListRequestSort:
      type: string
      enum:
        - creation_time_unix
        - name
      title: PronunciationDictionariesListRequestSort
    type_:GetPronunciationDictionaryMetadataResponseModelPermissionOnResource:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
    type_:GetPronunciationDictionaryMetadataResponse:
      type: object
      properties:
        id:
          type: string
          description: The ID of the pronunciation dictionary.
        latest_version_id:
          type: string
          description: The ID of the latest version of the pronunciation dictionary.
        latest_version_rules_num:
          type: integer
          description: >-
            The number of rules in the latest version of the pronunciation
            dictionary.
        name:
          type: string
          description: The name of the pronunciation dictionary.
        permission_on_resource:
          $ref: >-
            #/components/schemas/type_:GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
          description: The permission on the resource of the pronunciation dictionary.
        created_by:
          type: string
          description: The user ID of the creator of the pronunciation dictionary.
        creation_time_unix:
          type: integer
          description: The creation time of the pronunciation dictionary in Unix timestamp.
        archived_time_unix:
          type: integer
          description: The archive time of the pronunciation dictionary in Unix timestamp.
        description:
          type: string
          description: The description of the pronunciation dictionary.
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - created_by
        - creation_time_unix
      title: GetPronunciationDictionaryMetadataResponse
    type_:GetPronunciationDictionariesMetadataResponseModel:
      type: object
      properties:
        pronunciation_dictionaries:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:GetPronunciationDictionaryMetadataResponse
          description: A list of pronunciation dictionaries and their metadata.
        next_cursor:
          type: string
          description: The next cursor to use for pagination.
        has_more:
          type: boolean
          description: Whether there are more pronunciation dictionaries to fetch.
      required:
        - pronunciation_dictionaries
        - has_more
      title: GetPronunciationDictionariesMetadataResponseModel
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
    await client.pronunciationDictionaries.list({
        cursor: "cursor",
        pageSize: 1,
        sort: "creation_time_unix",
        sortDirection: "sort_direction",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.list(
    cursor="cursor",
    page_size=1,
    sort="creation_time_unix",
    sort_direction="sort_direction",
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries?cursor=cursor&page_size=1&sort=creation_time_unix&sort_direction=sort_direction"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries?cursor=cursor&page_size=1&sort=creation_time_unix&sort_direction=sort_direction")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries?cursor=cursor&page_size=1&sort=creation_time_unix&sort_direction=sort_direction")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries?cursor=cursor&page_size=1&sort=creation_time_unix&sort_direction=sort_direction');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries?cursor=cursor&page_size=1&sort=creation_time_unix&sort_direction=sort_direction");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries?cursor=cursor&page_size=1&sort=creation_time_unix&sort_direction=sort_direction")! as URL,
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

# Get user

GET https://api.elevenlabs.io/v1/user

Gets information about the user

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/user:
    get:
      operationId: get
      summary: Get user
      description: Gets information about the user
      tags:
        - subpackage_user
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
                $ref: '#/components/schemas/type_:User'
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
    type_:SubscriptionResponseModelCurrency:
      type: string
      enum:
        - usd
        - eur
        - inr
      title: SubscriptionResponseModelCurrency
    type_:SubscriptionStatusType:
      type: string
      enum:
        - trialing
        - active
        - incomplete
        - past_due
        - free
        - free_disabled
      title: SubscriptionStatusType
    type_:BillingPeriod:
      type: string
      enum:
        - monthly_period
        - 3_month_period
        - 6_month_period
        - annual_period
      title: BillingPeriod
    type_:CharacterRefreshPeriod:
      type: string
      enum:
        - monthly_period
        - 3_month_period
        - 6_month_period
        - annual_period
      title: CharacterRefreshPeriod
    type_:SubscriptionResponse:
      type: object
      properties:
        tier:
          type: string
          description: The tier of the user's subscription.
        character_count:
          type: integer
          description: The number of characters used by the user.
        character_limit:
          type: integer
          description: >-
            The maximum number of characters allowed in the current billing
            period.
        max_character_limit_extension:
          type: integer
          description: >-
            Maximum number of characters that the character limit can be
            exceeded by. Managed by the workspace admin.
        can_extend_character_limit:
          type: boolean
          description: Whether the user can extend their character limit.
        allowed_to_extend_character_limit:
          type: boolean
          description: Whether the user is allowed to extend their character limit.
        next_character_count_reset_unix:
          type: integer
          description: The Unix timestamp of the next character count reset.
        voice_slots_used:
          type: integer
          description: The number of voice slots used by the user.
        professional_voice_slots_used:
          type: integer
          description: >-
            The number of professional voice slots used by the workspace/user if
            single seat.
        voice_limit:
          type: integer
          description: The maximum number of voice slots allowed for the user.
        max_voice_add_edits:
          type: integer
          description: The maximum number of voice add/edits allowed for the user.
        voice_add_edit_counter:
          type: integer
          description: The number of voice add/edits used by the user.
        professional_voice_limit:
          type: integer
          description: The maximum number of professional voices allowed for the user.
        can_extend_voice_limit:
          type: boolean
          description: Whether the user can extend their voice limit.
        can_use_instant_voice_cloning:
          type: boolean
          description: Whether the user can use instant voice cloning.
        can_use_professional_voice_cloning:
          type: boolean
          description: Whether the user can use professional voice cloning.
        currency:
          $ref: '#/components/schemas/type_:SubscriptionResponseModelCurrency'
          description: The currency of the user's subscription.
        status:
          $ref: '#/components/schemas/type_:SubscriptionStatusType'
          description: The status of the user's subscription.
        billing_period:
          $ref: '#/components/schemas/type_:BillingPeriod'
          description: The billing period of the user's subscription.
        character_refresh_period:
          $ref: '#/components/schemas/type_:CharacterRefreshPeriod'
          description: The character refresh period of the user's subscription.
      required:
        - tier
        - character_count
        - character_limit
        - can_extend_character_limit
        - allowed_to_extend_character_limit
        - voice_slots_used
        - professional_voice_slots_used
        - voice_limit
        - voice_add_edit_counter
        - professional_voice_limit
        - can_extend_voice_limit
        - can_use_instant_voice_cloning
        - can_use_professional_voice_cloning
        - status
      title: SubscriptionResponse
    type_:SeatType:
      type: string
      enum:
        - workspace_admin
        - workspace_member
        - workspace_lite_member
      description: |-
        Seat types for workspace members.
        Lite Member is equivalent to Basic Seat in the web application.
        Member is equivalent to Full Seat in the web application.
      title: SeatType
    type_:User:
      type: object
      properties:
        user_id:
          type: string
          description: The unique identifier of the user.
        subscription:
          $ref: '#/components/schemas/type_:SubscriptionResponse'
          description: Details of the user's subscription.
        is_new_user:
          type: boolean
          description: >-
            Whether the user is new. This field is deprecated and will be
            removed in the future. Use 'created_at' instead.
        xi_api_key:
          type: string
          description: The API key of the user.
        can_use_delayed_payment_methods:
          type: boolean
          description: >-
            This field is deprecated and will be removed in a future major
            version. Instead use subscription.trust_on_invoice_creation.
        is_onboarding_completed:
          type: boolean
          description: Whether the user's onboarding is completed.
        is_onboarding_checklist_completed:
          type: boolean
          description: Whether the user's onboarding checklist is completed.
        show_compliance_terms:
          type: boolean
          default: false
          description: >-
            Whether to show compliance terms (ToS, Privacy Policy, biometric
            consent) during onboarding. Set for users signing up from the
            marketing site.
        first_name:
          type: string
          description: First name of the user.
        is_api_key_hashed:
          type: boolean
          default: false
          description: Whether the user's API key is hashed.
        xi_api_key_preview:
          type: string
          description: The preview of the user's API key.
        referral_link_code:
          type: string
          description: The referral link code of the user.
        partnerstack_partner_default_link:
          type: string
          description: The Partnerstack partner default link of the user.
        created_at:
          type: integer
          description: >-
            The unix timestamp of the user's creation. 0 if the user was created
            before the unix timestamp was added.
        seat_type:
          $ref: '#/components/schemas/type_:SeatType'
          description: The seat type of the user.
      required:
        - user_id
        - subscription
        - is_new_user
        - can_use_delayed_payment_methods
        - is_onboarding_completed
        - is_onboarding_checklist_completed
        - created_at
        - seat_type
      title: User
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
    await client.user.get();
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.user.get()
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user"

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

url = URI("https://api.elevenlabs.io/v1/user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/user");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user")! as URL,
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

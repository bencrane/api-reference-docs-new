# Create a voice

POST https://api.elevenlabs.io/v1/text-to-voice
Content-Type: application/json

Create a voice from previously generated voice preview. This endpoint should be called after you fetched a generated_voice_id using POST /v1/text-to-voice/design or POST /v1/text-to-voice/:voice_id/remix.

Reference: https://elevenlabs.io/docs/api-reference/text-to-voice/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/text-to-voice:
    post:
      operationId: create
      summary: Create A New Voice From Voice Preview
      description: >-
        Create a voice from previously generated voice preview. This endpoint
        should be called after you fetched a generated_voice_id using POST
        /v1/text-to-voice/design or POST /v1/text-to-voice/:voice_id/remix.
      tags:
        - subpackage_textToVoice
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
                $ref: '#/components/schemas/type_:Voice'
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
                voice_name:
                  type: string
                  description: Name to use for the created voice.
                voice_description:
                  type: string
                  description: Description to use for the created voice.
                generated_voice_id:
                  type: string
                  description: >-
                    The generated_voice_id to create, call POST
                    /v1/text-to-voice/create-previews and fetch the
                    generated_voice_id from the response header if don't have
                    one yet.
                labels:
                  type: object
                  additionalProperties:
                    type: string
                  description: >-
                    Optional, metadata to add to the created voice. Defaults to
                    None.
                played_not_selected_voice_ids:
                  type: array
                  items:
                    type: string
                  description: >-
                    List of voice ids that the user has played but not selected.
                    Used for RLHF.
              required:
                - voice_name
                - voice_description
                - generated_voice_id
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_:SpeakerSeparationResponseModelStatus:
      type: string
      enum:
        - not_started
        - pending
        - completed
        - failed
      description: The status of the speaker separation.
      title: SpeakerSeparationResponseModelStatus
    type_:UtteranceResponseModel:
      type: object
      properties:
        start:
          type: number
          format: double
          description: The start time of the utterance in seconds.
        end:
          type: number
          format: double
          description: The end time of the utterance in seconds.
      required:
        - start
        - end
      title: UtteranceResponseModel
    type_:SpeakerResponseModel:
      type: object
      properties:
        speaker_id:
          type: string
          description: The ID of the speaker.
        duration_secs:
          type: number
          format: double
          description: The duration of the speaker segment in seconds.
        utterances:
          type: array
          items:
            $ref: '#/components/schemas/type_:UtteranceResponseModel'
          description: The utterances of the speaker.
      required:
        - speaker_id
        - duration_secs
      title: SpeakerResponseModel
    type_:SpeakerSeparationResponseModel:
      type: object
      properties:
        voice_id:
          type: string
          description: The ID of the voice.
        sample_id:
          type: string
          description: The ID of the sample.
        status:
          $ref: '#/components/schemas/type_:SpeakerSeparationResponseModelStatus'
          description: The status of the speaker separation.
        speakers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:SpeakerResponseModel'
          description: The speakers of the sample.
        selected_speaker_ids:
          type: array
          items:
            type: string
          description: The IDs of the selected speakers.
      required:
        - voice_id
        - sample_id
        - status
      title: SpeakerSeparationResponseModel
    type_:VoiceSample:
      type: object
      properties:
        sample_id:
          type: string
          description: The ID of the sample.
        file_name:
          type: string
          description: The name of the sample file.
        mime_type:
          type: string
          description: The MIME type of the sample file.
        size_bytes:
          type: integer
          description: The size of the sample file in bytes.
        hash:
          type: string
          description: The hash of the sample file.
        duration_secs:
          type: number
          format: double
        remove_background_noise:
          type: boolean
        has_isolated_audio:
          type: boolean
        has_isolated_audio_preview:
          type: boolean
        speaker_separation:
          $ref: '#/components/schemas/type_:SpeakerSeparationResponseModel'
        trim_start:
          type: integer
        trim_end:
          type: integer
      title: VoiceSample
    type_:VoiceResponseModelCategory:
      type: string
      enum:
        - generated
        - cloned
        - premade
        - professional
        - famous
        - high_quality
      description: The category of the voice.
      title: VoiceResponseModelCategory
    type_:FineTuningResponseModelStateValue:
      type: string
      enum:
        - not_started
        - queued
        - fine_tuning
        - fine_tuned
        - failed
        - delayed
      title: FineTuningResponseModelStateValue
    type_:RecordingResponse:
      type: object
      properties:
        recording_id:
          type: string
          description: The ID of the recording.
        mime_type:
          type: string
          description: The MIME type of the recording.
        size_bytes:
          type: integer
          description: The size of the recording in bytes.
        upload_date_unix:
          type: integer
          description: The date of the recording in Unix time.
        transcription:
          type: string
          description: The transcription of the recording.
      required:
        - recording_id
        - mime_type
        - size_bytes
        - upload_date_unix
        - transcription
      title: RecordingResponse
    type_:VerificationAttemptResponse:
      type: object
      properties:
        text:
          type: string
          description: The text of the verification attempt.
        date_unix:
          type: integer
          description: The date of the verification attempt in Unix time.
        accepted:
          type: boolean
          description: Whether the verification attempt was accepted.
        similarity:
          type: number
          format: double
          description: The similarity of the verification attempt.
        levenshtein_distance:
          type: number
          format: double
          description: The Levenshtein distance of the verification attempt.
        recording:
          $ref: '#/components/schemas/type_:RecordingResponse'
          description: The recording of the verification attempt.
      required:
        - text
        - date_unix
        - accepted
        - similarity
        - levenshtein_distance
      title: VerificationAttemptResponse
    type_:ManualVerificationFileResponse:
      type: object
      properties:
        file_id:
          type: string
          description: The ID of the file.
        file_name:
          type: string
          description: The name of the file.
        mime_type:
          type: string
          description: The MIME type of the file.
        size_bytes:
          type: integer
          description: The size of the file in bytes.
        upload_date_unix:
          type: integer
          description: The date of the file in Unix time.
      required:
        - file_id
        - file_name
        - mime_type
        - size_bytes
        - upload_date_unix
      title: ManualVerificationFileResponse
    type_:ManualVerificationResponse:
      type: object
      properties:
        extra_text:
          type: string
          description: The extra text of the manual verification.
        request_time_unix:
          type: integer
          description: The date of the manual verification in Unix time.
        files:
          type: array
          items:
            $ref: '#/components/schemas/type_:ManualVerificationFileResponse'
          description: The files of the manual verification.
      required:
        - extra_text
        - request_time_unix
        - files
      title: ManualVerificationResponse
    type_:FineTuningResponse:
      type: object
      properties:
        is_allowed_to_fine_tune:
          type: boolean
          description: Whether the user is allowed to fine-tune the voice.
        state:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:FineTuningResponseModelStateValue'
          description: The state of the fine-tuning process for each model.
        verification_failures:
          type: array
          items:
            type: string
          description: List of verification failures in the fine-tuning process.
        verification_attempts_count:
          type: integer
          description: The number of verification attempts in the fine-tuning process.
        manual_verification_requested:
          type: boolean
          description: >-
            Whether a manual verification was requested for the fine-tuning
            process.
        language:
          type: string
          description: The language of the fine-tuning process.
        progress:
          type: object
          additionalProperties:
            type: number
            format: double
          description: The progress of the fine-tuning process.
        message:
          type: object
          additionalProperties:
            type: string
          description: The message of the fine-tuning process.
        dataset_duration_seconds:
          type: number
          format: double
          description: The duration of the dataset in seconds.
        verification_attempts:
          type: array
          items:
            $ref: '#/components/schemas/type_:VerificationAttemptResponse'
          description: The number of verification attempts.
        slice_ids:
          type: array
          items:
            type: string
          description: List of slice IDs.
        manual_verification:
          $ref: '#/components/schemas/type_:ManualVerificationResponse'
          description: The manual verification of the fine-tuning process.
        max_verification_attempts:
          type: integer
          description: The maximum number of verification attempts.
        next_max_verification_attempts_reset_unix_ms:
          type: integer
          description: >-
            The next maximum verification attempts reset time in Unix
            milliseconds.
        finetuning_state:
          description: Any type
      title: FineTuningResponse
    type_:VoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
          description: >-
            Determines how stable the voice is and the randomness between each
            generation. Lower values introduce broader emotional range for the
            voice. Higher values can result in a monotonous voice with limited
            emotion.
        use_speaker_boost:
          type: boolean
          description: >-
            This setting boosts the similarity to the original speaker. Using
            this setting requires a slightly higher computational load, which in
            turn increases latency.
        similarity_boost:
          type: number
          format: double
          description: >-
            Determines how closely the AI should adhere to the original voice
            when attempting to replicate it.
        style:
          type: number
          format: double
          description: >-
            Determines the style exaggeration of the voice. This setting
            attempts to amplify the style of the original speaker. It does
            consume additional computational resources and might increase
            latency if set to anything other than 0.
        speed:
          type: number
          format: double
          description: >-
            Adjusts the speed of the voice. A value of 1.0 is the default speed,
            while values less than 1.0 slow down the speech, and values greater
            than 1.0 speed it up.
      title: VoiceSettings
    type_:voice_sharing_state:
      type: string
      enum:
        - enabled
        - disabled
        - copied
        - copied_disabled
      description: The status of the voice sharing.
      title: voice_sharing_state
    type_:VoiceSharingResponseModelCategory:
      type: string
      enum:
        - generated
        - cloned
        - premade
        - professional
        - famous
        - high_quality
      description: The category of the voice.
      title: VoiceSharingResponseModelCategory
    type_:review_status:
      type: string
      enum:
        - not_requested
        - pending
        - declined
        - allowed
        - allowed_with_changes
      description: The review status of the voice.
      title: review_status
    type_:VoiceSharingModerationCheckResponseModel:
      type: object
      properties:
        date_checked_unix:
          type: integer
          description: The date the moderation check was made in Unix time.
        name_value:
          type: string
          description: The name value of the voice.
        name_check:
          type: boolean
          description: Whether the name check was successful.
        description_value:
          type: string
          description: The description value of the voice.
        description_check:
          type: boolean
          description: Whether the description check was successful.
        sample_ids:
          type: array
          items:
            type: string
          description: A list of sample IDs.
        sample_checks:
          type: array
          items:
            type: number
            format: double
          description: A list of sample checks.
        captcha_ids:
          type: array
          items:
            type: string
          description: A list of captcha IDs.
        captcha_checks:
          type: array
          items:
            type: number
            format: double
          description: A list of CAPTCHA check values.
      title: VoiceSharingModerationCheckResponseModel
    type_:ReaderResourceResponseModelResourceType:
      type: string
      enum:
        - read
        - collection
      description: The type of resource.
      title: ReaderResourceResponseModelResourceType
    type_:ReaderResourceResponseModel:
      type: object
      properties:
        resource_type:
          $ref: '#/components/schemas/type_:ReaderResourceResponseModelResourceType'
          description: The type of resource.
        resource_id:
          type: string
          description: The ID of the resource.
      required:
        - resource_type
        - resource_id
      title: ReaderResourceResponseModel
    type_:VoiceSharingResponse:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/type_:voice_sharing_state'
        history_item_sample_id:
          type: string
        date_unix:
          type: integer
        whitelisted_emails:
          type: array
          items:
            type: string
        public_owner_id:
          type: string
        original_voice_id:
          type: string
        financial_rewards_enabled:
          type: boolean
        free_users_allowed:
          type: boolean
        live_moderation_enabled:
          type: boolean
        rate:
          type: number
          format: double
        fiat_rate:
          type: number
          format: double
        notice_period:
          type: integer
        disable_at_unix:
          type: integer
        voice_mixing_allowed:
          type: boolean
        featured:
          type: boolean
        category:
          $ref: '#/components/schemas/type_:VoiceSharingResponseModelCategory'
        reader_app_enabled:
          type: boolean
        image_url:
          type: string
        ban_reason:
          type: string
        liked_by_count:
          type: integer
        cloned_by_count:
          type: integer
        name:
          type: string
        description:
          type: string
        labels:
          type: object
          additionalProperties:
            type: string
        review_status:
          $ref: '#/components/schemas/type_:review_status'
        review_message:
          type: string
        enabled_in_library:
          type: boolean
        instagram_username:
          type: string
        twitter_username:
          type: string
        youtube_username:
          type: string
        tiktok_username:
          type: string
        moderation_check:
          $ref: '#/components/schemas/type_:VoiceSharingModerationCheckResponseModel'
        reader_restricted_on:
          type: array
          items:
            $ref: '#/components/schemas/type_:ReaderResourceResponseModel'
      title: VoiceSharingResponse
    type_:VerifiedVoiceLanguageResponseModel:
      type: object
      properties:
        language:
          type: string
        model_id:
          type: string
        accent:
          type: string
        locale:
          type: string
        preview_url:
          type: string
      required:
        - language
        - model_id
      title: VerifiedVoiceLanguageResponseModel
    type_:VoiceResponseModelSafetyControl:
      type: string
      enum:
        - NONE
        - BAN
        - CAPTCHA
        - ENTERPRISE_BAN
        - ENTERPRISE_CAPTCHA
      title: VoiceResponseModelSafetyControl
    type_:VoiceVerificationResponse:
      type: object
      properties:
        requires_verification:
          type: boolean
        is_verified:
          type: boolean
        verification_failures:
          type: array
          items:
            type: string
        verification_attempts_count:
          type: integer
        language:
          type: string
        verification_attempts:
          type: array
          items:
            $ref: '#/components/schemas/type_:VerificationAttemptResponse'
      required:
        - requires_verification
        - is_verified
        - verification_failures
        - verification_attempts_count
      title: VoiceVerificationResponse
    type_:Voice:
      type: object
      properties:
        voice_id:
          type: string
        name:
          type: string
        samples:
          type: array
          items:
            $ref: '#/components/schemas/type_:VoiceSample'
        category:
          $ref: '#/components/schemas/type_:VoiceResponseModelCategory'
        fine_tuning:
          $ref: '#/components/schemas/type_:FineTuningResponse'
        labels:
          type: object
          additionalProperties:
            type: string
        description:
          type: string
        preview_url:
          type: string
        available_for_tiers:
          type: array
          items:
            type: string
        settings:
          $ref: '#/components/schemas/type_:VoiceSettings'
        sharing:
          $ref: '#/components/schemas/type_:VoiceSharingResponse'
        high_quality_base_model_ids:
          type: array
          items:
            type: string
        verified_languages:
          type: array
          items:
            $ref: '#/components/schemas/type_:VerifiedVoiceLanguageResponseModel'
        collection_ids:
          type: array
          items:
            type: string
        safety_control:
          $ref: '#/components/schemas/type_:VoiceResponseModelSafetyControl'
        voice_verification:
          $ref: '#/components/schemas/type_:VoiceVerificationResponse'
        permission_on_resource:
          type: string
        is_owner:
          type: boolean
        is_legacy:
          type: boolean
          default: false
        is_mixed:
          type: boolean
          default: false
        favorited_at_unix:
          type: integer
        created_at_unix:
          type: integer
        is_bookmarked:
          type: boolean
      required:
        - voice_id
      title: Voice
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
    await client.textToVoice.create({
        voiceName: "Sassy squeaky mouse",
        voiceDescription: "A sassy squeaky mouse",
        generatedVoiceId: "37HceQefKmEi3bGovXjL",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.text_to_voice.create(
    voice_name="Sassy squeaky mouse",
    voice_description="A sassy squeaky mouse",
    generated_voice_id="37HceQefKmEi3bGovXjL",
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

	url := "https://api.elevenlabs.io/v1/text-to-voice"

	payload := strings.NewReader("{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice', [
  'body' => '{
  "voice_name": "Sassy squeaky mouse",
  "voice_description": "A sassy squeaky mouse",
  "generated_voice_id": "37HceQefKmEi3bGovXjL"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_name\": \"Sassy squeaky mouse\",\n  \"voice_description\": \"A sassy squeaky mouse\",\n  \"generated_voice_id\": \"37HceQefKmEi3bGovXjL\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "voice_name": "Sassy squeaky mouse",
  "voice_description": "A sassy squeaky mouse",
  "generated_voice_id": "37HceQefKmEi3bGovXjL"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice")! as URL,
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

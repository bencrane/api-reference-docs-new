# Stem Separation

POST https://api.elevenlabs.io/v1/music/stem-separation
Content-Type: multipart/form-data

Separate an audio file into individual stems. This endpoint might have high latency, depending on the length of the audio file.

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/stem-separation:
    post:
      operationId: separate-stems
      summary: Stem Separation
      description: >-
        Separate an audio file into individual stems. This endpoint might have
        high latency, depending on the length of the audio file.
      tags:
        - subpackage_music
      parameters:
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at
            32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate
            requires you to be subscribed to Creator tier or above. PCM with
            44.1kHz sample rate requires you to be subscribed to Pro tier or
            above. Note that the μ-law format (sometimes written mu-law, often
            approximated as u-law) is commonly used for Twilio audio inputs.
          required: false
          schema:
            $ref: '#/components/schemas/type_:AllowedOutputFormats'
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: >-
            ZIP archive containing separated audio stems. Each stem is provided
            as a separate audio file in the requested output format.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: The audio file to separate into stems.
                stem_variation_id:
                  $ref: >-
                    #/components/schemas/type_music:MusicSeparateStemsRequestStemVariationId
                  description: The id of the stem variation to use.
                sign_with_c2pa:
                  type: boolean
                  default: false
                  description: >-
                    Whether to sign the generated song with C2PA. Applicable
                    only for mp3 files.
              required:
                - file
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_:AllowedOutputFormats:
      type: string
      enum:
        - mp3_22050_32
        - mp3_24000_48
        - mp3_44100_32
        - mp3_44100_64
        - mp3_44100_96
        - mp3_44100_128
        - mp3_44100_192
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_32000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
        - alaw_8000
        - opus_48000_32
        - opus_48000_64
        - opus_48000_96
        - opus_48000_128
        - opus_48000_192
      title: AllowedOutputFormats
    type_music:MusicSeparateStemsRequestStemVariationId:
      type: string
      enum:
        - two_stems_v1
        - six_stems_v1
      default: six_stems_v1
      description: The id of the stem variation to use.
      title: MusicSeparateStemsRequestStemVariationId
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
    const client = new ElevenLabsClient({
        apiKey: "string",
    });
    await client.music.separateStems({
        outputFormat: "mp3_22050_32",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="string",
)

client.music.separate_stems(
    output_format="mp3_22050_32",
    file="example_file",
)
```

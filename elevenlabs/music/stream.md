# Stream Music

POST https://api.elevenlabs.io/v1/music/stream
Content-Type: application/json

Stream a composed song from a prompt or a composition plan.

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/stream:
    post:
      operationId: stream
      summary: Stream Composed Music
      description: Stream a composed song from a prompt or a composition plan.
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
          description: Streaming audio data in the format specified
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
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: >-
                    A simple text prompt to generate a song from. Cannot be used
                    in conjunction with `composition_plan`.
                composition_plan:
                  $ref: '#/components/schemas/type_:MusicPrompt'
                  description: >-
                    A detailed composition plan to guide music generation.
                    Cannot be used in conjunction with `prompt`.
                music_length_ms:
                  type: integer
                  description: >-
                    The length of the song to generate in milliseconds. Used
                    only in conjunction with `prompt`. Must be between 3000ms
                    and 600000ms. Optional - if not provided, the model will
                    choose a length based on the prompt.
                model_id:
                  type: string
                  enum:
                    - music_v1
                  description: The model to use for the generation.
                seed:
                  type: integer
                  description: >-
                    Random seed to initialize the music generation process.
                    Providing the same seed with the same parameters can help
                    achieve more consistent results, but exact reproducibility
                    is not guaranteed and outputs may change across system
                    updates. Cannot be used in conjunction with prompt.
                force_instrumental:
                  type: boolean
                  default: false
                  description: >-
                    If true, guarantees that the generated song will be
                    instrumental. If false, the song may or may not be
                    instrumental depending on the `prompt`. Can only be used
                    with `prompt`.
                store_for_inpainting:
                  type: boolean
                  default: false
                  description: >-
                    Whether to store the generated song for inpainting. Only
                    available to enterprise clients with access to the
                    inpainting feature.
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
    type_:TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
      title: TimeRange
    type_:SectionSource:
      type: object
      properties:
        song_id:
          type: string
          description: >-
            The ID of the song to source the section from. You can find the song
            ID in the response headers when you generate a song.
        range:
          $ref: '#/components/schemas/type_:TimeRange'
          description: The range to extract from the source song.
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/type_:TimeRange'
          description: The ranges to exclude from the 'range'.
      required:
        - song_id
        - range
      title: SectionSource
    type_:SongSection:
      type: object
      properties:
        section_name:
          type: string
          description: The name of the section. Must be between 1 and 100 characters.
        positive_local_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in this
            section. Use English language for best result.
        negative_local_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in this
            section. Use English language for best result.
        duration_ms:
          type: integer
          description: >-
            The duration of the section in milliseconds. Must be between 3000ms
            and 120000ms.
        lines:
          type: array
          items:
            type: string
          description: The lyrics of the section. Max 200 characters per line.
        source_from:
          $ref: '#/components/schemas/type_:SectionSource'
          description: >-
            Optional source to extract the section from. Used for inpainting.
            Only available to enterprise clients with access to the inpainting
            feature.
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
      title: SongSection
    type_:MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in the
            entire song. Use English language for best result.
        negative_global_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in the
            entire song. Use English language for best result.
        sections:
          type: array
          items:
            $ref: '#/components/schemas/type_:SongSection'
          description: The sections of the song.
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
      title: MusicPrompt
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
    await client.music.stream({});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.stream()
```

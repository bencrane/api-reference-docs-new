# Create transcript

POST https://api.elevenlabs.io/v1/speech-to-text
Content-Type: multipart/form-data

Transcribe an audio or video file. If webhook is set to true, the request will be processed asynchronously and results sent to configured webhooks. When use_multi_channel is true and the provided audio has multiple channels, a 'transcripts' object with separate transcripts for each channel is returned. Otherwise, returns a single transcript. The optional webhook_metadata parameter allows you to attach custom data that will be included in webhook responses for request correlation and tracking.

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/speech-to-text:
    post:
      operationId: convert
      summary: Create transcript
      description: >-
        Transcribe an audio or video file. If webhook is set to true, the
        request will be processed asynchronously and results sent to configured
        webhooks. When use_multi_channel is true and the provided audio has
        multiple channels, a 'transcripts' object with separate transcripts for
        each channel is returned. Otherwise, returns a single transcript. The
        optional webhook_metadata parameter allows you to attach custom data
        that will be included in webhook responses for request correlation and
        tracking.
      tags:
        - subpackage_speechToText
      parameters:
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean log and transcript storage features
            are unavailable for this request. Zero retention mode may only be
            used by enterprise customers.
          required: false
          schema:
            type: boolean
            default: true
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Synchronous transcription result
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_speechToText:SpeechToTextConvertResponse
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
                model_id:
                  $ref: >-
                    #/components/schemas/type_speechToText:SpeechToTextConvertRequestModelId
                  description: The ID of the model to use for transcription.
                file:
                  type: string
                  format: binary
                  description: >-
                    The file to transcribe. All major audio and video formats
                    are supported. Exactly one of the file or cloud_storage_url
                    parameters must be provided. The file size must be less than
                    3.0GB.
                language_code:
                  type: string
                  description: >-
                    An ISO-639-1 or ISO-639-3 language_code corresponding to the
                    language of the audio file. Can sometimes improve
                    transcription performance if known beforehand. Defaults to
                    null, in this case the language is predicted automatically.
                tag_audio_events:
                  type: boolean
                  default: true
                  description: >-
                    Whether to tag audio events like (laughter), (footsteps),
                    etc. in the transcription.
                num_speakers:
                  type: integer
                  description: >-
                    The maximum amount of speakers talking in the uploaded file.
                    Can help with predicting who speaks when. The maximum amount
                    of speakers that can be predicted is 32. Defaults to null,
                    in this case the amount of speakers is set to the maximum
                    value the model supports.
                timestamps_granularity:
                  $ref: >-
                    #/components/schemas/type_speechToText:SpeechToTextConvertRequestTimestampsGranularity
                  description: >-
                    The granularity of the timestamps in the transcription.
                    'word' provides word-level timestamps and 'character'
                    provides character-level timestamps per word.
                diarize:
                  type: boolean
                  default: false
                  description: >-
                    Whether to annotate which speaker is currently talking in
                    the uploaded file.
                diarization_threshold:
                  type: number
                  format: double
                  description: >-
                    Diarization threshold to apply during speaker diarization. A
                    higher value means there will be a lower chance of one
                    speaker being diarized as two different speakers but also a
                    higher chance of two different speakers being diarized as
                    one speaker (less total speakers predicted). A low value
                    means there will be a higher chance of one speaker being
                    diarized as two different speakers but also a lower chance
                    of two different speakers being diarized as one speaker
                    (more total speakers predicted). Can only be set when
                    diarize=True and num_speakers=None. Defaults to None, in
                    which case we will choose a threshold based on the model_id
                    (0.22 usually).
                additional_formats:
                  $ref: '#/components/schemas/type_:AdditionalFormats'
                  description: A list of additional formats to export the transcript to.
                file_format:
                  $ref: >-
                    #/components/schemas/type_speechToText:SpeechToTextConvertRequestFileFormat
                  description: >-
                    The format of input audio. Options are 'pcm_s16le_16' or
                    'other' For `pcm_s16le_16`, the input audio must be 16-bit
                    PCM at a 16kHz sample rate, single channel (mono), and
                    little-endian byte order. Latency will be lower than with
                    passing an encoded waveform.
                cloud_storage_url:
                  type: string
                  description: >-
                    The HTTPS URL of the file to transcribe. Exactly one of the
                    file or cloud_storage_url parameters must be provided. The
                    file must be accessible via HTTPS and the file size must be
                    less than 2GB. Any valid HTTPS URL is accepted, including
                    URLs from cloud storage providers (AWS S3, Google Cloud
                    Storage, Cloudflare R2, etc.), CDNs, or any other HTTPS
                    source. URLs can be pre-signed or include authentication
                    tokens in query parameters.
                webhook:
                  type: boolean
                  default: false
                  description: >-
                    Whether to send the transcription result to configured
                    speech-to-text webhooks.  If set the request will return
                    early without the transcription, which will be delivered
                    later via webhook.
                webhook_id:
                  type: string
                  description: >-
                    Optional specific webhook ID to send the transcription
                    result to. Only valid when webhook is set to true. If not
                    provided, transcription will be sent to all configured
                    speech-to-text webhooks.
                temperature:
                  type: number
                  format: double
                  description: >-
                    Controls the randomness of the transcription output. Accepts
                    values between 0.0 and 2.0, where higher values result in
                    more diverse and less deterministic results. If omitted, we
                    will use a temperature based on the model you selected which
                    is usually 0.
                seed:
                  type: integer
                  description: >-
                    If specified, our system will make a best effort to sample
                    deterministically, such that repeated requests with the same
                    seed and parameters should return the same result.
                    Determinism is not guaranteed. Must be an integer between 0
                    and 2147483647.
                use_multi_channel:
                  type: boolean
                  default: false
                  description: >-
                    Whether the audio file contains multiple channels where each
                    channel contains a single speaker. When enabled, each
                    channel will be transcribed independently and the results
                    will be combined. Each word in the response will include a
                    'channel_index' field indicating which channel it was spoken
                    on. A maximum of 5 channels is supported.
                webhook_metadata:
                  $ref: >-
                    #/components/schemas/type_speechToText:SpeechToTextConvertRequestWebhookMetadata
                  description: >-
                    Optional metadata to be included in the webhook response.
                    This should be a JSON string representing an object with a
                    maximum depth of 2 levels and maximum size of 16KB. Useful
                    for tracking internal IDs, job references, or other
                    contextual information.
                entity_detection:
                  $ref: >-
                    #/components/schemas/type_speechToText:SpeechToTextConvertRequestEntityDetection
                  description: >-
                    Detect entities in the transcript. Can be 'all' to detect
                    all entities, a single entity type or category string, or a
                    list of entity types/categories. Categories include 'pii',
                    'phi', 'pci', 'other', 'offensive_language'. When enabled,
                    detected entities will be returned in the 'entities' field
                    with their text, type, and character positions. Usage of
                    this parameter will incur additional costs.
                no_verbatim:
                  type: boolean
                  default: false
                  description: >-
                    If true, the transcription will not have any filler words,
                    false starts and non-speech sounds. Only supported with
                    scribe_v2 model.
                entity_redaction:
                  $ref: >-
                    #/components/schemas/type_speechToText:SpeechToTextConvertRequestEntityRedaction
                  description: >-
                    Redact entities from the transcript text. Accepts the same
                    format as entity_detection: 'all', a category ('pii',
                    'phi'), or specific entity types. Must be a subset of
                    entity_detection. When redaction is enabled, the entities
                    field will not be returned.
                entity_redaction_mode:
                  type: string
                  default: enumerated_entity_type
                  description: >-
                    How to format redacted entities. 'redacted' replaces with
                    {REDACTED}, 'entity_type' replaces with {ENTITY_TYPE},
                    'enumerated_entity_type' replaces with {ENTITY_TYPE_N} where
                    N enumerates each occurrence. Only used when
                    entity_redaction is set.
                keyterms:
                  type: array
                  items:
                    type: string
                  description: >-
                    A list of keyterms to bias the transcription
                    towards.           The keyterms are words or phrases you
                    want the model to recognise more accurately.           The
                    number of keyterms cannot exceed 1000.           The length
                    of each keyterm must be less than 50 characters.
                    Keyterms can contain at most 5 words (after
                    normalisation).           For example ["hello", "world",
                    "technical term"].           Usage of this parameter will
                    incur additional costs.           When more than 100
                    keyterms are provided, a minimum billable duration of 20
                    seconds applies per request.
              required:
                - model_id
servers:
  - url: https://api.elevenlabs.io
  - url: https://api.us.elevenlabs.io
  - url: https://api.eu.residency.elevenlabs.io
  - url: https://api.in.residency.elevenlabs.io
components:
  schemas:
    type_speechToText:SpeechToTextConvertRequestModelId:
      type: string
      enum:
        - scribe_v2
        - scribe_v1
      description: The ID of the model to use for transcription.
      title: SpeechToTextConvertRequestModelId
    type_speechToText:SpeechToTextConvertRequestTimestampsGranularity:
      type: string
      enum:
        - none
        - word
        - character
      default: word
      description: >-
        The granularity of the timestamps in the transcription. 'word' provides
        word-level timestamps and 'character' provides character-level
        timestamps per word.
      title: SpeechToTextConvertRequestTimestampsGranularity
    type_:ExportOptions:
      oneOf:
        - type: object
          properties:
            format:
              type: string
              enum:
                - docx
              description: 'Discriminator value: docx'
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type: number
              format: double
            max_segment_duration_s:
              type: number
              format: double
            max_segment_chars:
              type: integer
          required:
            - format
        - type: object
          properties:
            format:
              type: string
              enum:
                - html
              description: 'Discriminator value: html'
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type: number
              format: double
            max_segment_duration_s:
              type: number
              format: double
            max_segment_chars:
              type: integer
          required:
            - format
        - type: object
          properties:
            format:
              type: string
              enum:
                - pdf
              description: 'Discriminator value: pdf'
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type: number
              format: double
            max_segment_duration_s:
              type: number
              format: double
            max_segment_chars:
              type: integer
          required:
            - format
        - type: object
          properties:
            format:
              type: string
              enum:
                - segmented_json
              description: 'Discriminator value: segmented_json'
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type: number
              format: double
            max_segment_duration_s:
              type: number
              format: double
            max_segment_chars:
              type: integer
          required:
            - format
        - type: object
          properties:
            format:
              type: string
              enum:
                - srt
              description: 'Discriminator value: srt'
            max_characters_per_line:
              type: integer
            include_speakers:
              type: boolean
              default: false
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type: number
              format: double
            max_segment_duration_s:
              type: number
              format: double
            max_segment_chars:
              type: integer
          required:
            - format
        - type: object
          properties:
            format:
              type: string
              enum:
                - txt
              description: 'Discriminator value: txt'
            max_characters_per_line:
              type: integer
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type: number
              format: double
            max_segment_duration_s:
              type: number
              format: double
            max_segment_chars:
              type: integer
          required:
            - format
      discriminator:
        propertyName: format
      title: ExportOptions
    type_:AdditionalFormats:
      type: array
      items:
        $ref: '#/components/schemas/type_:ExportOptions'
      title: AdditionalFormats
    type_speechToText:SpeechToTextConvertRequestFileFormat:
      type: string
      enum:
        - pcm_s16le_16
        - other
      default: other
      description: >-
        The format of input audio. Options are 'pcm_s16le_16' or 'other' For
        `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample
        rate, single channel (mono), and little-endian byte order. Latency will
        be lower than with passing an encoded waveform.
      title: SpeechToTextConvertRequestFileFormat
    type_speechToText:SpeechToTextConvertRequestWebhookMetadata:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      description: >-
        Optional metadata to be included in the webhook response. This should be
        a JSON string representing an object with a maximum depth of 2 levels
        and maximum size of 16KB. Useful for tracking internal IDs, job
        references, or other contextual information.
      title: SpeechToTextConvertRequestWebhookMetadata
    type_speechToText:SpeechToTextConvertRequestEntityDetection:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: >-
        Detect entities in the transcript. Can be 'all' to detect all entities,
        a single entity type or category string, or a list of entity
        types/categories. Categories include 'pii', 'phi', 'pci', 'other',
        'offensive_language'. When enabled, detected entities will be returned
        in the 'entities' field with their text, type, and character positions.
        Usage of this parameter will incur additional costs.
      title: SpeechToTextConvertRequestEntityDetection
    type_speechToText:SpeechToTextConvertRequestEntityRedaction:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: >-
        Redact entities from the transcript text. Accepts the same format as
        entity_detection: 'all', a category ('pii', 'phi'), or specific entity
        types. Must be a subset of entity_detection. When redaction is enabled,
        the entities field will not be returned.
      title: SpeechToTextConvertRequestEntityRedaction
    type_:SpeechToTextWordResponseModelType:
      type: string
      enum:
        - word
        - spacing
        - audio_event
      description: >-
        The type of the word or sound. 'audio_event' is used for non-word sounds
        like laughter or footsteps.
      title: SpeechToTextWordResponseModelType
    type_:SpeechToTextCharacterResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The character that was transcribed.
        start:
          type: number
          format: double
          description: The start time of the character in seconds.
        end:
          type: number
          format: double
          description: The end time of the character in seconds.
      required:
        - text
      title: SpeechToTextCharacterResponseModel
    type_:SpeechToTextWordResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The word or sound that was transcribed.
        start:
          type: number
          format: double
          description: The start time of the word or sound in seconds.
        end:
          type: number
          format: double
          description: The end time of the word or sound in seconds.
        type:
          $ref: '#/components/schemas/type_:SpeechToTextWordResponseModelType'
          description: >-
            The type of the word or sound. 'audio_event' is used for non-word
            sounds like laughter or footsteps.
        speaker_id:
          type: string
          description: Unique identifier for the speaker of this word.
        logprob:
          type: number
          format: double
          description: >-
            The log of the probability with which this word was predicted.
            Logprobs are in range [-infinity, 0], higher logprobs indicate a
            higher confidence the model has in its predictions.
        characters:
          type: array
          items:
            $ref: '#/components/schemas/type_:SpeechToTextCharacterResponseModel'
          description: The characters that make up the word and their timing information.
      required:
        - text
        - type
        - logprob
      description: Word-level detail of the transcription with timing information.
      title: SpeechToTextWordResponseModel
    type_:AdditionalFormatResponseModel:
      type: object
      properties:
        requested_format:
          type: string
          description: The requested format.
        file_extension:
          type: string
          description: The file extension of the additional format.
        content_type:
          type: string
          description: The content type of the additional format.
        is_base64_encoded:
          type: boolean
          description: Whether the content is base64 encoded.
        content:
          type: string
          description: The content of the additional format.
      required:
        - requested_format
        - file_extension
        - content_type
        - is_base64_encoded
        - content
      title: AdditionalFormatResponseModel
    type_:DetectedEntity:
      type: object
      properties:
        text:
          type: string
          description: The text that was identified as an entity.
        entity_type:
          type: string
          description: >-
            The type of entity detected (e.g., 'credit_card', 'email_address',
            'person_name').
        start_char:
          type: integer
          description: Start character position in the transcript text.
        end_char:
          type: integer
          description: End character position in the transcript text.
      required:
        - text
        - entity_type
        - start_char
        - end_char
      title: DetectedEntity
    type_:SpeechToTextChunkResponseModel:
      type: object
      properties:
        language_code:
          type: string
          description: The detected language code (e.g. 'eng' for English).
        language_probability:
          type: number
          format: double
          description: The confidence score of the language detection (0 to 1).
        text:
          type: string
          description: The raw text of the transcription.
        words:
          type: array
          items:
            $ref: '#/components/schemas/type_:SpeechToTextWordResponseModel'
          description: List of words with their timing information.
        channel_index:
          type: integer
          description: >-
            The channel index this transcript belongs to (for multichannel
            audio).
        additional_formats:
          type: array
          items:
            $ref: '#/components/schemas/type_:AdditionalFormatResponseModel'
          description: Requested additional formats of the transcript.
        transcription_id:
          type: string
          description: The transcription ID of the response.
        entities:
          type: array
          items:
            $ref: '#/components/schemas/type_:DetectedEntity'
          description: >-
            List of detected entities with their text, type, and character
            positions in the transcript.
      required:
        - language_code
        - language_probability
        - text
        - words
      description: Chunk-level detail of the transcription with timing information.
      title: SpeechToTextChunkResponseModel
    type_:MultichannelSpeechToTextResponseModel:
      type: object
      properties:
        transcripts:
          type: array
          items:
            $ref: '#/components/schemas/type_:SpeechToTextChunkResponseModel'
          description: >-
            List of transcripts, one for each audio channel. Each transcript
            contains the text and word-level details for its respective channel.
        transcription_id:
          type: string
          description: The transcription ID of the response.
      required:
        - transcripts
      description: Response model for multichannel speech-to-text transcription.
      title: MultichannelSpeechToTextResponseModel
    type_:SpeechToTextWebhookResponseModel:
      type: object
      properties:
        message:
          type: string
          description: The message of the webhook response.
        request_id:
          type: string
          description: The request ID of the webhook response.
        transcription_id:
          type: string
          description: The transcription ID of the webhook response.
      required:
        - message
        - request_id
      title: SpeechToTextWebhookResponseModel
    type_speechToText:SpeechToTextConvertResponse:
      oneOf:
        - $ref: '#/components/schemas/type_:SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/type_:MultichannelSpeechToTextResponseModel'
        - $ref: '#/components/schemas/type_:SpeechToTextWebhookResponseModel'
      title: SpeechToTextConvertResponse
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
    await client.speechToText.convert({
        enableLogging: true,
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_to_text.convert(
    enable_logging=True,
    file="example_file",
)
```

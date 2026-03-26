# Execute @cf/deepgram/nova-3 model.

`POST /accounts/{account_id}/ai/run/@cf/deepgram/nova-3`

Runs inference on the @cf/deepgram/nova-3 model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **audio** (object, required): 
- **channels** (number, optional): The number of channels in the submitted audio
- **custom_intent** (string, optional): Custom intents you want the model to detect within your input audio if present
- **custom_intent_mode** (string, optional): Sets how the model will interpret intents submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in addition those submitted using the custom_intents param Values: `extended`, `strict`
- **custom_topic** (string, optional): Custom topics you want the model to detect within your input audio or text if present Submit up to 100
- **custom_topic_mode** (string, optional): Sets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param. Values: `extended`, `strict`
- **detect_entities** (boolean, optional): Identifies and extracts key entities from content in submitted audio
- **detect_language** (boolean, optional): Identifies the dominant language spoken in submitted audio
- **diarize** (boolean, optional): Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0
- **dictation** (boolean, optional): Identify and extract key entities from content in submitted audio
- **encoding** (string, optional): Specify the expected encoding of your submitted audio Values: `linear16`, `flac`, `mulaw`, `amr-nb`, `amr-wb`, `opus`, `speex`, `g729`
- **endpointing** (string, optional): Indicates how long model will wait to detect whether a speaker has finished speaking or pauses for a significant period of time. When set to a value, the streaming endpoint immediately finalizes the transcription for the processed time range and returns the transcript with a speech_final parameter set to true. Can also be set to false to disable endpointing
- **extra** (string, optional): Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
- **filler_words** (boolean, optional): Filler Words can help transcribe interruptions in your audio, like 'uh' and 'um'
- **interim_results** (boolean, optional): Specifies whether the streaming endpoint should provide ongoing transcription updates as more audio is received. When set to true, the endpoint sends continuous updates, meaning transcription results may evolve over time. Note: Supported only for webosockets.
- **keyterm** (string, optional): Key term prompting can boost or suppress specialized terminology and brands.
- **keywords** (string, optional): Keywords can boost or suppress specialized terminology and brands.
- **language** (string, optional): The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available.
- **measurements** (boolean, optional): Spoken measurements will be converted to their corresponding abbreviations.
- **mip_opt_out** (boolean, optional): Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip.
- **mode** (string, optional): Mode of operation for the model representing broad area of topic that will be talked about in the supplied audio Values: `general`, `medical`, `finance`
- **multichannel** (boolean, optional): Transcribe each audio channel independently.
- **numerals** (boolean, optional): Numerals converts numbers from written format to numerical format.
- **paragraphs** (boolean, optional): Splits audio into paragraphs to improve transcript readability.
- **profanity_filter** (boolean, optional): Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely.
- **punctuate** (boolean, optional): Add punctuation and capitalization to the transcript.
- **redact** (string, optional): Redaction removes sensitive information from your transcripts.
- **replace** (string, optional): Search for terms or phrases in submitted audio and replaces them.
- **search** (string, optional): Search for terms or phrases in submitted audio.
- **sentiment** (boolean, optional): Recognizes the sentiment throughout a transcript or text.
- **smart_format** (boolean, optional): Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability.
- **topics** (boolean, optional): Detect topics throughout a transcript or text.
- **utt_split** (number, optional): Seconds to wait before detecting a pause between words in submitted audio.
- **utterance_end_ms** (boolean, optional): Indicates how long model will wait to send an UtteranceEnd message after a word has been transcribed. Use with interim_results. Note: Supported only for webosockets.
- **utterances** (boolean, optional): Segments speech into meaningful semantic units.
- **vad_events** (boolean, optional): Indicates that speech has started. You'll begin receiving Speech Started messages upon speech starting. Note: Supported only for webosockets.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

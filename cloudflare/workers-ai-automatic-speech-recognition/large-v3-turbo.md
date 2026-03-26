# Execute @cf/openai/whisper-large-v3-turbo model.

`POST /accounts/{account_id}/ai/run/@cf/openai/whisper-large-v3-turbo`

Runs inference on the @cf/openai/whisper-large-v3-turbo model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **audio** (object, required): 
- **beam_size** (integer, optional): The number of beams to use in beam search decoding. Higher values may improve accuracy at the cost of speed.
- **compression_ratio_threshold** (number, optional): Threshold for filtering out segments with high compression ratio, which often indicate repetitive or hallucinated text.
- **condition_on_previous_text** (boolean, optional): Whether to condition on previous text during transcription. Setting to false may help prevent hallucination loops.
- **hallucination_silence_threshold** (number, optional): Optional threshold (in seconds) to skip silent periods that may cause hallucinations.
- **initial_prompt** (string, optional): A text prompt to help provide context to the model on the contents of the audio.
- **language** (string, optional): The language of the audio being transcribed or translated.
- **log_prob_threshold** (number, optional): Threshold for filtering out segments with low average log probability, indicating low confidence.
- **no_speech_threshold** (number, optional): Threshold for detecting no-speech segments. Segments with no-speech probability above this value are skipped.
- **prefix** (string, optional): The prefix appended to the beginning of the output of the transcription and can guide the transcription result.
- **task** (string, optional): Supported tasks are 'translate' or 'transcribe'.
- **vad_filter** (boolean, optional): Preprocess the audio with a voice activity detection model.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

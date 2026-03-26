# Execute @cf/deepgram/aura-1 model.

`POST /accounts/{account_id}/ai/run/@cf/deepgram/aura-1`

Runs inference on the @cf/deepgram/aura-1 model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **bit_rate** (number, optional): The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.
- **container** (string, optional): Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.. Values: `none`, `wav`, `ogg`
- **encoding** (string, optional): Encoding of the output audio. Values: `linear16`, `flac`, `mulaw`, `alaw`, `mp3`, `opus`, `aac`
- **sample_rate** (number, optional): Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable
- **speaker** (string, optional): Speaker used to produce the audio. Values: `angus`, `asteria`, `arcas`, `orion`, `orpheus`, `athena`, `luna`, `zeus`, `perseus`, `helios`, `hera`, `stella`
- **text** (string, required): The text content to be converted to speech

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

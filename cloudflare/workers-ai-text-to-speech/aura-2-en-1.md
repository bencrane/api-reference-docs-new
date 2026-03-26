# Execute @cf/deepgram/aura-2-en model.

`POST /accounts/{account_id}/ai/run/@cf/deepgram/aura-2-en`

Runs inference on the @cf/deepgram/aura-2-en model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **bit_rate** (number, optional): The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.
- **container** (string, optional): Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.. Values: `none`, `wav`, `ogg`
- **encoding** (string, optional): Encoding of the output audio. Values: `linear16`, `flac`, `mulaw`, `alaw`, `mp3`, `opus`, `aac`
- **sample_rate** (number, optional): Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable
- **speaker** (string, optional): Speaker used to produce the audio. Values: `amalthea`, `andromeda`, `apollo`, `arcas`, `aries`, `asteria`, `athena`, `atlas`, `aurora`, `callista`, `cora`, `cordelia`, `delia`, `draco`, `electra`, `harmonia`, `helena`, `hera`, `hermes`, `hyperion`, `iris`, `janus`, `juno`, `jupiter`, `luna`, `mars`, `minerva`, `neptune`, `odysseus`, `ophelia`, `orion`, `orpheus`, `pandora`, `phoebe`, `pluto`, `saturn`, `thalia`, `theia`, `vesta`, `zeus`
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

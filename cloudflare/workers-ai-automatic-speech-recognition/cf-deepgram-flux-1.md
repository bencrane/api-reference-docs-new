# Execute @cf/deepgram/flux model.

`POST /accounts/{account_id}/ai/run/@cf/deepgram/flux`

Runs inference on the @cf/deepgram/flux model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **eager_eot_threshold** (string, optional): End-of-turn confidence required to fire an eager end-of-turn event. When set, enables EagerEndOfTurn and TurnResumed events. Valid Values 0.3 - 0.9.
- **encoding** (string, required): Encoding of the audio stream. Currently only supports raw signed little-endian 16-bit PCM. Values: `linear16`
- **eot_threshold** (string, optional): End-of-turn confidence required to finish a turn. Valid Values 0.5 - 0.9.
- **eot_timeout_ms** (string, optional): A turn will be finished when this much time has passed after speech, regardless of EOT confidence.
- **keyterm** (string, optional): Keyterm prompting can improve recognition of specialized terminology. Pass multiple keyterm query parameters to boost multiple keyterms.
- **mip_opt_out** (string, optional): Opts out requests from the Deepgram Model Improvement Program. Refer to Deepgram Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip Values: `true`, `false`
- **sample_rate** (string, required): Sample rate of the audio stream in Hz.
- **tag** (string, optional): Label your requests for the purpose of identification during usage reporting

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

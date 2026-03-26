# Create signed URL tokens for videos

`POST /accounts/{account_id}/stream/{identifier}/token`

Creates a signed URL token for a video. If a body is not provided in the request, a token is created with default values.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **accessRules** (array, optional): The optional list of access rule constraints on the token. Access can be blocked or allowed based on an IP, IP range, or by country. Access rules are evaluated from first to last. If a rule matches, the associated action is applied and no further rules are evaluated.
- **downloadable** (boolean, optional): The optional boolean value that enables using signed tokens to access MP4 download links for a video.
- **exp** (integer, optional): The optional unix epoch timestamp that specficies the time after a token is not accepted. The maximum time specification is 24 hours from issuing time. If this field is not set, the default is one hour after issuing.
- **id** (string, optional): The optional ID of a Stream signing key. If present, the `pem` field is also required.
- **nbf** (integer, optional): The optional unix epoch timestamp that specifies the time before a the token is not accepted. If this field is not set, the default is one hour before issuing.
- **pem** (string, optional): The optional base64 encoded private key in PEM format associated with a Stream signing key. If present, the `id` field is also required.

## Response

### 200

Create signed URL tokens for videos response.

- **result** (object, optional): 

### 4XX

Create signed URL tokens for videos response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

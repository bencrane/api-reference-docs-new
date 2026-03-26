# Get all converted formats supported

`GET /accounts/{account_id}/ai/tomarkdown/supported`

Lists all file formats supported for conversion to Markdown.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Successful response

- **result** (array): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):

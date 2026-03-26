# Create new saved logo queries from image files

`POST /accounts/{account_id}/brand-protection/logos`

Return new saved logo queries created from image files

## Parameters

- **tag** (string, optional) [query]: 
- **match_type** (string, optional) [query]: 
- **threshold** (number, optional) [query]: 


## Response

### 201

Created

- **id** (integer): 
- **tag** (string): 
- **upload_path** (string): 

### 422

Unprocessable Content

- **code** (integer): Error code
- **errors** (object): Errors
- **message** (string): Error message
- **status** (string): Error name

### default

Default error response

- **code** (integer): Error code
- **errors** (object): Errors
- **message** (string): Error message
- **status** (string): Error name

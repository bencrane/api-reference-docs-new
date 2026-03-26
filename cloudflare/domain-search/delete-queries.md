# Delete saved string queries by ID

`DELETE /accounts/{account_id}/brand-protection/queries`

Return a success message after deleting saved string queries by ID

## Parameters

- **id** (string, optional) [query]: 
- **tag** (string, optional) [query]: 
- **scan** (boolean, optional) [query]: 

## Response

### 204

No Content

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

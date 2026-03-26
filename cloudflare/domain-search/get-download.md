# Download matches for string queries by ID

`GET /accounts/{account_id}/brand-protection/matches/download`

Return matches as CSV for string queries based on ID

## Parameters

- **id** (string, optional) [query]: 
- **offset** (integer, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **include_domain_id** (boolean, optional) [query]: 

## Response

### 200

OK

- **matches** (array): 
- **total** (integer): 

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

# Read matches for logo queries by ID

`GET /accounts/{account_id}/brand-protection/logo-matches`

Return matches for logo queries based on ID

## Parameters

- **logo_id** (array, optional) [query]: 
- **offset** (string, optional) [query]: 
- **limit** (string, optional) [query]: 

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

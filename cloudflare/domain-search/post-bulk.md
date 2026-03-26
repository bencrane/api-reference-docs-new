# Create new saved string queries in bulk

`POST /accounts/{account_id}/brand-protection/queries/bulk`

Return a success message after creating new saved string queries in bulk

## Request Body

- **queries** (array, optional): 

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

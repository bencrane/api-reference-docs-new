# Create new saved string queries

`POST /accounts/{account_id}/brand-protection/queries`

Return a success message after creating new saved string queries

## Parameters

- **id** (string, optional) [query]: 
- **tag** (string, optional) [query]: 
- **scan** (boolean, optional) [query]: 

## Request Body

- **max_time** (string, optional): 
- **min_time** (string, optional): 
- **scan** (boolean, optional): 
- **string_matches** (object, optional): 
- **tag** (string, optional): 

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

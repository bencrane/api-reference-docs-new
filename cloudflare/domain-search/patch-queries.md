# Update saved string queries by ID

`PATCH /accounts/{account_id}/brand-protection/queries`

Update a saved query's tag, scan setting, or string_matches (pattern). When string_matches is provided, the query parameters and hash are updated. At least one of tag, scan, or string_matches is required.

## Request Body

- **id** (integer, optional): The query ID to update (required when updating tag or scan)
- **scan** (boolean, optional): Whether to scan matches
- **string_matches** (array, optional): Updated pattern match constraints. When provided, replaces the existing string_matches.
- **tag** (string, optional): Query tag. Required as identifier when updating string_matches.

## Response

### default

Default error response

- **code** (integer): Error code
- **errors** (object): Errors
- **message** (string): Error message
- **status** (string): Error name

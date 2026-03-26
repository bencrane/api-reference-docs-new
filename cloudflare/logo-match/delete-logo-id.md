# Delete saved logo queries by ID

`DELETE /accounts/{account_id}/brand-protection/logos/{logo_id}`

Return a success message after deleting saved logo queries by ID

## Response

### 204

No Content

### default

Default error response

- **code** (integer): Error code
- **errors** (object): Errors
- **message** (string): Error message
- **status** (string): Error name

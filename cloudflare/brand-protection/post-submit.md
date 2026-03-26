# Create new URL submissions

`POST /accounts/{account_id}/brand-protection/submit`

Return new URL submissions

## Response

### 201

Created

- **skipped_urls** (array): 
- **submitted_urls** (array): 

### default

Default error response

- **code** (integer): Error code
- **errors** (object): Errors
- **message** (string): Error message
- **status** (string): Error name

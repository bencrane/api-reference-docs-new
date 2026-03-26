# Validate a DLP regex pattern

`POST /accounts/{account_id}/dlp/patterns/validate`

Validates whether this pattern is a valid regular expression. Rejects it if
the regular expression is too complex or can match an unbounded-length
string. The regex will be rejected if it uses `*` or `+`. Bound the maximum
number of characters that can be matched using a range, e.g. `{1,100}`.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **max_match_bytes** (integer, optional): Maximum number of bytes that the regular expression can match.

If this is `null` then there is no limit on the length. Patterns can use
`*` and `+`. Otherwise repeats should use a range `{m,n}` to restrict
patterns to the length. If this field is missing, then a default length
limit is used.

Note that the length is specified in bytes. Since regular expressions
use UTF-8 the pattern `.` can match up to 4 bytes. Hence `.{1,256}`
has a maximum length of 1024 bytes.
- **regex** (string, required): 

## Response

### 200

Validation response.

- **result** (object, optional): 

### 4XX

Failed to validate.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

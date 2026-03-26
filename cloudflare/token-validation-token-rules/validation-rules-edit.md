# Edit a zone token validation rule

`PATCH /zones/{zone_id}/token_validation/rules/{rule_id}`

Edit a zone token validation rule.

## Request Body

- **action** (string, optional): Action to take on requests that match operations included in `selector` and fail `expression`. Values: `log`, `block`
- **description** (string, optional): A human-readable description that gives more details than `title`.
- **enabled** (boolean, optional): Toggle rule on or off.
- **expression** (string, optional): Rule expression. Requests that fail to match this expression will be subject to `action`.

For details on expressions, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

- **selector** (object, optional): Select operations covered by this rule.

For details on selectors, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

- **title** (string, optional): A human-readable name for the rule.
- **position** (object, optional): Update rule order among zone rules.

## Response

### 200

OK

- **result** (object, optional): A Token Validation rule that can enforce security policies using JWT Tokens.

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

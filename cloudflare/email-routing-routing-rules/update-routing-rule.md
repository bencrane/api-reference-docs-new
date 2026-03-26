# Update routing rule

`PUT /zones/{zone_id}/email/routing/rules/{rule_identifier}`

Update actions and matches, or enable/disable specific routing rules.

## Parameters

- **rule_identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **actions** (array, required): List actions patterns.
- **enabled** (boolean, optional): Routing rule status. Values: `true`, `false`
- **matchers** (array, required): Matching patterns to forward to your actions.
- **name** (string, optional): Routing rule name.
- **priority** (number, optional): Priority of the routing rule.

## Response

### 200

Update routing rule response

- **result** (object, optional):

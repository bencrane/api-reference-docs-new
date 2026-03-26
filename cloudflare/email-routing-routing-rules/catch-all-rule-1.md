# Update catch-all rule

`PUT /zones/{zone_id}/email/routing/rules/catch_all`

Enable or disable catch-all routing rule, or change action to forward to specific destination address.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **actions** (array, required): List actions for the catch-all routing rule.
- **enabled** (boolean, optional): Routing rule status. Values: `true`, `false`
- **matchers** (array, required): List of matchers for the catch-all routing rule.
- **name** (string, optional): Routing rule name.

## Response

### 200

Update catch-all rule response

- **result** (object, optional):

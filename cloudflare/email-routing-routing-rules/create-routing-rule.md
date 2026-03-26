# Create routing rule

`POST /zones/{zone_id}/email/routing/rules`

Rules consist of a set of criteria for matching emails (such as an email being sent to a specific custom email address) plus a set of actions to take on the email (like forwarding it to a specific destination address).

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **actions** (array, required): List actions patterns.
- **enabled** (boolean, optional): Routing rule status. Values: `true`, `false`
- **matchers** (array, required): Matching patterns to forward to your actions.
- **name** (string, optional): Routing rule name.
- **priority** (number, optional): Priority of the routing rule.

## Response

### 200

Create routing rule response

- **result** (object, optional):

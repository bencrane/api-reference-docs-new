# Create a Zero Trust Gateway rule

`POST /accounts/{account_id}/gateway/rules`

Create a new Zero Trust Gateway rule.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **action** (string, required): Specify the action to perform when the associated traffic, identity, and device posture expressions either absent or evaluate to `true`. Values: `on`, `off`, `allow`, `block`, `scan`, `noscan`, `safesearch`, `ytrestricted`, `isolate`, `noisolate`, `override`, `l4_override`, `egress`, `resolve`, `quarantine`, `redirect`
- **description** (string, optional): Specify the rule description.
- **device_posture** (string, optional): Specify the wirefilter expression used for device posture check. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response.
- **enabled** (boolean, optional): Specify whether the rule is enabled.
- **expiration** (object, optional): Defines the expiration time stamp and default duration of a DNS policy. Takes precedence over the policy's `schedule` configuration, if any. This  does not apply to HTTP or network policies. Settable only for `dns` rules.
- **filters** (array, optional): Specify the protocol or layer to evaluate the traffic, identity, and device posture expressions. Can only contain a single value.
- **identity** (string, optional): Specify the wirefilter expression used for identity matching. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response.
- **name** (string, required): Specify the rule name.
- **precedence** (integer, optional): Set the order of your rules. Lower values indicate higher precedence. At each processing phase, evaluate applicable rules in ascending order of this value. Refer to [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform) to manage precedence via Terraform.
- **rule_settings** (object, optional): Defines settings for this rule. Settings apply only to specific rule types and must use compatible selectors. If Terraform detects drift, confirm the setting supports your rule type and check whether the API modifies the value. Use API-returned values in your configuration to prevent drift.
- **schedule** (object, optional): Defines the schedule for activating DNS policies. Settable only for `dns` and `dns_resolver` rules.
- **traffic** (string, optional): Specify the wirefilter expression used for traffic matching. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response.

## Response

### 200

Create a Zero Trust Gateway rule response.

_Empty object_

### 4XX

Create a Zero Trust Gateway rule response failure.

_Empty object_

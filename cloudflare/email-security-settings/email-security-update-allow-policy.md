# Update an email allow policy

`PATCH /accounts/{account_id}/email-security/settings/allow_policies/{policy_id}`

Updates an existing email allow policy, modifying its matching criteria or scope.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Request Body

- **comments** (string, optional): 
- **is_acceptable_sender** (boolean, optional): Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions.
Note: This will not exempt messages with Malicious or Suspicious dispositions.
- **is_exempt_recipient** (boolean, optional): Messages to this recipient will bypass all detections.
- **is_regex** (boolean, optional): 
- **is_trusted_sender** (boolean, optional): Messages from this sender will bypass all detections and link following.
- **pattern** (string, optional): 
- **pattern_type** (object, optional): 
- **verify_sender** (boolean, optional): Enforce DMARC, SPF or DKIM authentication.
When on, Email Security only honors policies that pass authentication.

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):

# Create an email allow policy

`POST /accounts/{account_id}/email-security/settings/allow_policies`

Creates a new email allow policy that permits specific senders, domains, or patterns
to bypass security scanning.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **comments** (string, optional): 
- **is_acceptable_sender** (boolean, required): Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions.
Note: This will not exempt messages with Malicious or Suspicious dispositions.
- **is_exempt_recipient** (boolean, required): Messages to this recipient will bypass all detections.
- **is_recipient** (boolean, optional): 
- **is_regex** (boolean, required): 
- **is_sender** (boolean, optional): 
- **is_spoof** (boolean, optional): 
- **is_trusted_sender** (boolean, required): Messages from this sender will bypass all detections and link following.
- **pattern** (string, required): 
- **pattern_type** (string, required):  Values: `EMAIL`, `DOMAIN`, `IP`, `UNKNOWN`
- **verify_sender** (boolean, required): Enforce DMARC, SPF or DKIM authentication.
When on, Email Security only honors policies that pass authentication.

## Response

### 201

Contains the newly created policy.

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

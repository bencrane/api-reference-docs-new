# Update a trusted email domain

`PATCH /accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}`

Modifies a trusted domain entry's configuration.

## Parameters

- **account_id** (string, required) [path]: 
- **trusted_domain_id** (string, required) [path]: 

## Request Body

- **comments** (string, optional): 
- **is_recent** (boolean, optional): Select to prevent recently registered domains from triggering a
Suspicious or Malicious disposition.
- **is_regex** (boolean, optional): 
- **is_similarity** (boolean, optional): Select for partner or other approved domains that have similar
spelling to your connected domains. Prevents listed domains from
triggering a Spoof disposition.
- **pattern** (string, optional): 

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

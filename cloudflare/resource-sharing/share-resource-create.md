# Create a new share resource

`POST /accounts/{account_id}/shares/{share_id}/resources`

Adds a resource to an existing share, making it available to share recipients.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 

## Request Body

- **meta** (object, required): Resource Metadata.
- **resource_account_id** (string, required): Account identifier.
- **resource_id** (string, required): Share Resource identifier.
- **resource_type** (string, required): Resource Type. Values: `custom-ruleset`, `gateway-policy`, `gateway-destination-ip`, `gateway-block-page-settings`, `gateway-extended-email-matching`

## Response

### 201

Share resource created.

_Empty object_

### 4XX

Create share resource failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Create share resource failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

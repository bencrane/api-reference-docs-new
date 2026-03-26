# List Access SCIM update logs

`GET /accounts/{account_id}/access/logs/scim/updates`

Lists Access SCIM update logs that maintain a record of updates made to User and Group resources synced to Cloudflare via the System for Cross-domain Identity Management (SCIM).

## Parameters

- **account_id** (string, required) [path]: 
- **limit** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **until** (string, optional) [query]: 
- **idp_id** (string, required) [query]: 
- **status** (string, optional) [query]: 
- **resource_type** (string, optional) [query]: 
- **request_method** (string, optional) [query]: 
- **resource_user_email** (string, optional) [query]: 
- **resource_group_name** (string, optional) [query]: 
- **cf_resource_id** (string, optional) [query]: 
- **idp_resource_id** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Get Access SCIM update logs response

- **result** (array, optional): 

### 4XX

Get Access SCIM update logs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

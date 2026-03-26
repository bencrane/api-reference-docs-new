# List SCIM User resources

`GET /accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/users`

Lists SCIM User resources synced to Cloudflare via the System for Cross-domain Identity Management (SCIM).

## Parameters

- **identity_provider_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cf_resource_id** (string, optional) [query]: 
- **idp_resource_id** (string, optional) [query]: 
- **username** (string, optional) [query]: 
- **email** (string, optional) [query]: 
- **name** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List SCIM User resources response

- **result** (array, optional): 

### 4XX

List SCIM User resources response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Update a risk score integration.

`PUT /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}`

Overwrite the reference_id, tenant_url, and active values with the ones provided.

## Parameters

- **account_id** (string, required) [path]: 
- **integration_id** (string, required) [path]: 

## Request Body

- **active** (boolean, required): Whether this integration is enabled. If disabled, no risk changes will be exported to the third-party.
- **reference_id** (string, optional): A reference id that can be supplied by the client. Currently this should be set to the Access-Okta IDP ID (a UUIDv4).
https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider
- **tenant_url** (string, required): The base url of the tenant, e.g. "https://tenant.okta.com".

## Response

### 200

Update response.

- **result** (object, optional): 

### 4XX

Update failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

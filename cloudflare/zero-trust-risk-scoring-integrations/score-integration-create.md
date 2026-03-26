# Create new risk score integration.

`POST /accounts/{account_id}/zt_risk_scoring/integrations`

Creates a new Zero Trust risk score integration, connecting external risk signals to Cloudflare's risk scoring system.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **integration_type** (string, required):  Values: `Okta`
- **reference_id** (string, optional): A reference id that can be supplied by the client. Currently this should be set to the Access-Okta IDP ID (a UUIDv4).
https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider
- **tenant_url** (string, required): The base url of the tenant, e.g. "https://tenant.okta.com".

## Response

### 200

Create response.

- **result** (object, optional): 

### 4XX

Create failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Get SCIM Service Provider Config

`GET /accounts/{account_id}/scim/v2/ServiceProviderConfig`

Returns the SCIM 2.0 Service Provider configuration (RFC 7643 Section 5). IdPs use this endpoint to auto-configure their SCIM integration with Cloudflare, discovering which optional features (patch, bulk, filter, etc.) are supported.


## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get SCIM Service Provider Config response

### 4XX

Get SCIM Service Provider Config response failure

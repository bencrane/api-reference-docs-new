# Update an Access identity provider

`PUT /zones/{zone_id}/access/identity_providers/{identity_provider_id}`

Updates a configured identity provider.

## Parameters

- **identity_provider_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

One of: Azure AD, Centrify, Facebook, GitHub, Google, Google Workspace, LinkedIn, Generic OAuth, Okta, OneLogin, PingOne, Generic SAML, Yandex

## Response

### 200

Update an Access identity provider response

_Empty object_

### 4XX

Update an Access identity provider response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

# Add an Access identity provider

`POST /zones/{zone_id}/access/identity_providers`

Adds a new identity provider to Access.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

One of: Azure AD, Centrify, Facebook, GitHub, Google, Google Workspace, LinkedIn, Generic OAuth, Okta, OneLogin, PingOne, Generic SAML, Yandex

## Response

### 201

Add an Access identity provider response

_Empty object_

### 4XX

Add an Access identity provider response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

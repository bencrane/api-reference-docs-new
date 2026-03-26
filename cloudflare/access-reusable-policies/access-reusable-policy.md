# Create an Access reusable policy

`POST /accounts/{account_id}/access/policies`

Creates a new Access reusable policy.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **approval_groups** (array, optional): Administrators who can approve a temporary authentication request.
- **approval_required** (boolean, optional): Requires the user to request access from an administrator at the start of each session.
- **connection_rules** (object, optional): The rules that define how users may connect to targets secured by your application.
- **isolation_required** (boolean, optional): Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.
- **mfa_config** (object, optional): Configures multi-factor authentication (MFA) settings.
- **purpose_justification_prompt** (string, optional): A custom message that will appear on the purpose justification screen.
- **purpose_justification_required** (boolean, optional): Require users to enter a justification when they log in to the application.
- **session_duration** (string, optional): The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

## Response

### 201

Create an Access reusable policy response.

_Empty object_

### 4XX

Create an Access reusable policy response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

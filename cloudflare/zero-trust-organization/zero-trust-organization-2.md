# Update your Zero Trust organization

`PUT /accounts/{account_id}/access/organizations`

Updates the configuration for your Zero Trust organization.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **allow_authenticate_via_warp** (boolean, optional): When set to true, users can authenticate via WARP for any application in your organization. Application settings will take precedence over this value.
- **auth_domain** (string, optional): The unique subdomain assigned to your Zero Trust organization.
- **auto_redirect_to_identity** (boolean, optional): When set to `true`, users skip the identity provider selection step during login.
- **custom_pages** (object, optional): 
- **deny_unmatched_requests** (boolean, optional): Determines whether to deny all requests to Cloudflare-protected resources that lack an associated Access application. If enabled, you must explicitly configure an Access application and policy to allow traffic to your Cloudflare-protected resources. For domains you want to be public across all subdomains, add the domain to the `deny_unmatched_requests_exempted_zone_names` array.
- **deny_unmatched_requests_exempted_zone_names** (array, optional): Contains zone names to exempt from the `deny_unmatched_requests` feature. Requests to a subdomain in an exempted zone will block unauthenticated traffic by default if there is a configured Access application and policy that matches the request.
- **is_ui_read_only** (boolean, optional): Lock all settings as Read-Only in the Dashboard, regardless of user permission. Updates may only be made via the API or Terraform for this account when enabled.
- **login_design** (object, optional): 
- **mfa_config** (object, optional): Configures multi-factor authentication (MFA) settings for an organization.
- **mfa_required_for_all_apps** (boolean, optional): Determines whether global MFA settings apply to applications by default. The organization must have MFA enabled with at least one authentication method and a session duration configured.
- **name** (string, optional): The name of your Zero Trust organization.
- **session_duration** (string, optional): The amount of time that tokens issued for applications will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.
- **ui_read_only_toggle_reason** (string, optional): A description of the reason why the UI read only field is being toggled.
- **user_seat_expiration_inactive_time** (string, optional): The amount of time a user seat is inactive before it expires. When the user seat exceeds the set time of inactivity, the user is removed as an active seat and no longer counts against your Teams seat count.  Minimum value for this setting is 1 month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.
- **warp_auth_session_duration** (string, optional): The amount of time that tokens issued for applications will be valid. Must be in the format `30m` or `2h45m`. Valid time units are: m, h.

## Response

### 200

Update your Zero Trust organization response

_Empty object_

### 4XX

Update your Zero Trust organization response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

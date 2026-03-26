# Create your Zero Trust organization

`POST /zones/{zone_id}/access/organizations`

Sets up a Zero Trust organization for your account.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **auth_domain** (string, required): The unique subdomain assigned to your Zero Trust organization.
- **is_ui_read_only** (boolean, optional): Lock all settings as Read-Only in the Dashboard, regardless of user permission. Updates may only be made via the API or Terraform for this account when enabled.
- **login_design** (object, optional): 
- **name** (string, required): The name of your Zero Trust organization.
- **ui_read_only_toggle_reason** (string, optional): A description of the reason why the UI read only field is being toggled.
- **user_seat_expiration_inactive_time** (string, optional): The amount of time a user seat is inactive before it expires. When the user seat exceeds the set time of inactivity, the user is removed as an active seat and no longer counts against your Teams seat count. Must be in the format `300ms` or `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

## Response

### 201

Create your Zero Trust organization response

_Empty object_

### 4XX

Create your Zero Trust organization response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

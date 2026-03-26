# Create a Turnstile Widget

`POST /accounts/{account_id}/challenges/widgets`

Lists challenge widgets.

## Request Body

- **bot_fight_mode** (boolean, optional): If bot_fight_mode is set to `true`, Cloudflare issues computationally
expensive challenges in response to malicious bots (ENT only).

- **clearance_level** (string, optional): If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance,
this setting can determine the clearance level to be set
 Values: `no_clearance`, `jschallenge`, `managed`, `interactive`
- **domains** (array, required): 
- **ephemeral_id** (boolean, optional): Return the Ephemeral ID in /siteverify (ENT only).

- **mode** (string, required): Widget Mode Values: `non-interactive`, `invisible`, `managed`
- **name** (string, required): Human readable widget name. Not unique. Cloudflare suggests that you
set this to a meaningful string to make it easier to identify your
widget, and where it is used.

- **offlabel** (boolean, optional): Do not show any Cloudflare branding on the widget (ENT only).

- **region** (string, optional): Region where this widget can be used. This cannot be changed after creation.
 Values: `world`, `china`

## Response

### 200

Create Turnstile Widget Response

_Empty object_

### 4XX

Create Turnstile Widget Response Error

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful

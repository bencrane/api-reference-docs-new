# Create Campaign

Creates a new campaign with the provided properties. See how to launch your first campaign.

## Authorization

`basicAuth`

## Header Parameters

| Parameter | Type | Description |
|---|---|---|
| `x-lang-output` | string | Enum: `"native"` `"match"`. `native` - Translate response to the native language of the country in the request. `match` - match the response to the language in the request. Default response is in English. |

## Request Body Schema: `application/json`

### Required Fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Name of the campaign. |
| `schedule_type` | string (cmp_schedule_type) | How the campaign should be scheduled. Only value available today is `immediate`. |
| `use_type` | string or null (cmp_use_type) | Enum: `"marketing"` `"operational"` `null`. The use type for each mailpiece. Can be one of marketing, operational, or null. Null use_type is only allowed if an account default use_type is selected in Account Settings. |

### Optional Fields

| Field | Type | Description |
|---|---|---|
| `billing_group_id` | string or null `^bg_[a-zA-Z0-9]+$` | Unique identifier prefixed with `bg_`. |
| `description` | string or null <= 255 characters | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `target_delivery_date` | string or null \<date-time\> | If schedule_type is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign. |
| `send_date` | string or null \<date-time\> | If schedule_type is `scheduled_send_date`, provide a date to send this campaign. |
| `cancel_window_campaign_minutes` | integer or null | A window, in minutes, within which the campaign can be canceled. |
| `metadata` | object <= 500 characters `[^"\\]{0,500}` | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. Nested objects are not supported. |
| `auto_cancel_if_ncoa` | boolean | Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA. |
| `print_speed` | string or null (default: `"core"`) | A string designating the mail speed type: `core` - 2 production business days. |

## Responses

### 200 — Campaign created successfully

#### Response Schema: `application/json`

##### Required Fields

| Field | Type | Description |
|---|---|---|
| `date_created` | string \<date-time\> | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string \<date-time\> | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string (default: `"campaign"`) | Value is resource type. |
| `name` | string | Name of the campaign. |
| `schedule_type` | string (cmp_schedule_type) | How the campaign should be scheduled. Only value available today is `immediate`. |
| `use_type` | string or null | Enum: `"marketing"` `"operational"` `null`. The use type for each mailpiece. |
| `id` | string `^cmp_[a-zA-Z0-9]+$` | Unique identifier prefixed with `cmp_`. |
| `description` | string or null <= 255 characters | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `is_draft` | boolean (default: `true`) | Whether or not the campaign is still a draft. |
| `creatives` | Array of objects (creative) >= 0 items | An array of creatives that have been associated with this campaign. |
| `uploads` | Array of objects (upload) [0..1] items | A single-element array containing the upload object that is associated with this campaign. |
| `auto_cancel_if_ncoa` | boolean | Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA. |

##### Optional Fields

| Field | Type | Description |
|---|---|---|
| `deleted` | boolean | Only returned if the resource has been successfully deleted. |
| `billing_group_id` | string or null `^bg_[a-zA-Z0-9]+$` | Unique identifier prefixed with `bg_`. |
| `target_delivery_date` | string or null \<date-time\> | If schedule_type is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign. |
| `send_date` | string or null \<date-time\> | If schedule_type is `scheduled_send_date`, provide a date to send this campaign. |
| `cancel_window_campaign_minutes` | integer or null | A window, in minutes, within which the campaign can be canceled. |
| `metadata` | object <= 500 characters `[^"\\]{0,500}` | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. Nested objects are not supported. |
| `print_speed` | string or null (default: `"core"`) | A string designating the mail speed type: `core` - 2 production business days. |

## Request Samples

### Payload

```json
{
  "name": "My Demo Campaign",
  "description": "My Campaign's description",
  "schedule_type": "immediate",
  "print_speed": "core"
}
```

### CURL

```bash
POST /campaigns
```

## Response Samples

### 200

```json
{
  "id": "cmp_e05ee61ff80764b",
  "billing_group_id": "bg_fe3079dcdd80e5ae",
  "name": "My Campaign",
  "description": "My Campaign's description",
  "schedule_type": "immediate",
  "cancel_window_campaign_minutes": 60,
  "metadata": {},
  "use_type": "marketing",
  "is_draft": true,
  "deleted": false,
  "creatives": [],
  "uploads": [],
  "auto_cancel_if_ncoa": false,
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "campaign"
}
```
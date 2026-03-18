# Hypertide - Schemas

## Error

| Field | Type | Example |
|---|---|---|
| `success` | boolean | `false` |
| `error` | string | `"VALIDATION_FAILED"` |
| `message` | string | `"Order validation failed"` |
| `details` | array | `[{...}]` |
| `requestId` | string | `"req_1234567890_abc123"` |

## User

| Field | Type | Required | Example |
|---|---|---|---|
| `first_name` | string | Yes | `"John"` |
| `last_name` | string | Yes | `"Doe"` |

## ToolCredentials

| Field | Type | Description |
|---|---|---|
| `api_key` | string | API key for the tool |
| `oauth_link` | string | OAuth link (Smartlead only, must start with `https://login.microsoftonline.com`) |
| `username` | string | Username/email for the tool |
| `password` | string | Password for the tool |
| `bison_url` | string | Bison URL (Bison only) |

## CreateOrderRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `plan` | string | Yes | Plan type. `entra` = 52 users per domain, `google` = 3 users per domain. Enum: `entra`, `google` |
| `domains` | string[] | Yes | Exactly 2 domains are required per order. Min: 2, Max: 2. Example: `["domain1.com", "domain2.com"]` |
| `domain_option` | string | Yes | Domain option. Enum: see API spec |
| `forwarding_domain` | string | Yes | Example: `"forward.example.com"` |
| `client_name` | string | Yes | Example: `"Client Inc."` |
| `selected_tool` | string | Yes | Sending tool selection. Enum: see API spec |
| `tool_credentials` | ToolCredentials | No | See [ToolCredentials](#toolcredentials) |
| `users` | User[] | Yes | User names. Google plan: exactly 1 user (applied to all 3 accounts). Entra plan: any number (split across 52 accounts). See [User](#user) |
| `profile_picture_link` | string | No | Optional, only for Google plan |
| `warmup_setup` | WarmupSetup | No | Warmup configuration for email accounts. See [WarmupSetup](#warmupsetup) |
| ~~`enable_warmup`~~ | boolean | No | **DEPRECATED.** Simple on/off toggle. Default: `true`. Use `warmup_setup` for full control. |

## WarmupSetup

Warmup configuration for email accounts.

| Field | Type | Default | Description |
|---|---|---|---|
| `enabled` | boolean | `true` | Enable warmup for inboxes |
| `settings` | SmartleadWarmupSettings \| InstantlyWarmupSettings | — | Tool-specific warmup settings. Fields vary by `selected_tool`. See below. |
| `tags` | string[] | — | Tags to apply to accounts. Example: `["hypertide", "client-name"]` |

### SmartleadWarmupSettings

Warmup settings for Smartlead.

| Field | Type | Default | Example | Description |
|---|---|---|---|---|
| `max_warmup_emails_per_day` | integer | `5` | `5` | Maximum warmup emails per day |
| `ramp_up_value` | integer | `1` | `1` | Daily increment for warmup volume |
| `warmup_reply_rate` | integer | `60` | `60` | Target reply rate percentage (0-100) |
| `warmup_tag_identifier` | string | `"tryit-hypertide"` | `"tryit-hypertide"` | Warmup tag identifier |

### InstantlyWarmupSettings

Warmup settings for Instantly.

| Field | Type | Default | Example | Description |
|---|---|---|---|---|
| `warmup_limit` | integer | `5` | `5` | Maximum warmup emails per day |
| `warmup_reply_rate` | integer | `100` | `100` | Target reply rate percentage (0-100) |
| `warmup_increment` | integer | `1` | `1` | Daily increment for warmup volume |

## UpdateForwardingRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `domains` | string[] | Yes | Example: `["domain1.com", "domain2.com"]` |
| `forwardingDomain` | string | No | New forwarding domain (use this OR `forwardingEmail`). Example: `"forward.example.com"` |
| `forwardingEmail` | string | No | New forwarding email (use this OR `forwardingDomain`). Example: `"contact@example.com"` |

## UpdateUsernameRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `domains` | string[] | Yes | List of domains to update. Example: `["domain1.com", "domain2.com"]` |
| `users` | object[] | Yes | List of users to assign. Inbox count is auto-calculated based on domain plan. |

**Users object:**

| Field | Type | Required | Description |
|---|---|---|---|
| `first_name` | string | Yes | User's first name |
| `last_name` | string | Yes | User's last name |
| `signature` | string | No | User's email signature |

## DnsRecord

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `type` | string | Yes | — | Record type. Enum: `A`, `AAAA`, `CNAME`, `MX`, `TXT`, `NS`, `SRV`. Example: `"A"` |
| `name` | string | No | — | Subdomain name, leave empty for root (`@`). Example: `"subdomain"` |
| `content` | string | Yes | — | Record content (IP, hostname, or text). Example: `"192.168.1.1"` |
| `ttl` | integer | No | `3600` | Time to live. Example: `3600` |

# Hypertide - Orders

## Orders

Order management

---

### `POST /orders`

**Create a new order**

Creates a new order with the provided configuration.

**Domain Availability Check:**

- When `domain_option` is `"purchase_domain_for_me"`, all domains are checked for availability
- If any domain is unavailable, the order is rejected with details

**Credential Verification:**

- **Smartlead:** OAuth link format, API key validity, login credentials
- **Instantly:** Login credentials, workspace fetch via API key

> **Note:** `tool_credentials` is not required when `selected_tool` is `"other"`

#### Parameters

No parameters.

#### Request Body

**Media type:** `application/json`

```json
{
  "plan": "entra",
  "domains": [
    "domain1.com",
    "domain2.com"
  ],
  "domain_option": "purchase_domain_for_me",
  "forwarding_domain": "forward.example.com",
  "client_name": "Client Inc.",
  "selected_tool": "smartlead",
  "tool_credentials": {
    "api_key": "string",
    "oauth_link": "string",
    "username": "string",
    "password": "string",
    "bison_url": "string"
  },
  "users": [
    {
      "first_name": "John",
      "last_name": "Doe"
    }
  ],
  "profile_picture_link": "string",
  "warmup_setup": {
    "enabled": true,
    "settings": {
      "max_warmup_emails_per_day": 5,
      "ramp_up_value": 1,
      "warmup_reply_rate": 60,
      "warmup_tag_identifier": "tryit-hypertide"
    },
    "tags": [
      "hypertide",
      "client-name"
    ]
  }
}
```

#### Responses

| Code | Description |
|---|---|
| `201` | Order created successfully |
| `400` | Validation failed |
| `401` | API key required |
| `403` | Permission denied |

**`201` - Order created successfully**

**Media type:** `application/json`

```json
{
  "success": true,
  "message": "Orders submitted successfully.",
  "data": {
    "orderCount": 2,
    "orders": [
      {
        "id": "recXXXXXXXXXXXX",
        "domain": "example.com"
      }
    ],
    "nameservers": {
      "message": "Please update your domain nameservers to the following",
      "ns": [
        "ns1.dnsimple.com",
        "ns2.dnsimple-edge.net",
        "ns3.dnsimple.com",
        "ns4.dnsimple-edge.org"
      ]
    }
  },
  "requestId": "string"
}
```

**`400` - Validation failed**

**Media type:** `application/json`

```json
{
  "success": false,
  "error": "VALIDATION_FAILED",
  "message": "Order validation failed",
  "details": [
    {
      "field": "string",
      "reason": "string"
    }
  ],
  "requestId": "req_1234567890_abc123"
}
```

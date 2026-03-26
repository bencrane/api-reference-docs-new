# Stripe Customers API Reference

**Canonical reference for the Stripe Customers API, optimized for B2B SaaS billing integrations.**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

## Table of Contents

1. [The Customer Object](#1-the-customer-object)
2. [Create a Customer](#2-create-a-customer)
3. [Update a Customer](#3-update-a-customer)
4. [Retrieve a Customer](#4-retrieve-a-customer)
5. [List All Customers](#5-list-all-customers)
6. [Delete a Customer](#6-delete-a-customer)
7. [Search Customers](#7-search-customers)
8. [B2B Billing Patterns for Customers](#8-b2b-billing-patterns-for-customers)

---

## 1. The Customer Object

The Customer object represents a buyer in your Stripe account. It stores billing details, payment methods, subscriptions, and metadata used throughout the billing lifecycle.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | — | Unique identifier for the customer (e.g., `cus_abc123`). |
| `address` | object, nullable | No | Customer address: `line1`, `line2`, `city`, `state`, `postal_code`, `country`. |
| `balance` | integer | No | Account balance in cents. Negative values represent credit that will be applied to the next invoice. |
| `business_name` | string, nullable | No | Business name associated with the customer. |
| `cash_balance` | object, nullable, expandable | No | Cash balance settings for the customer. |
| `created` | timestamp | — | Time at which the customer was created. Measured in seconds since the Unix epoch. |
| `currency` | string, nullable | No | Three-letter ISO currency code for the customer's default currency. |
| `customer_account` | string, nullable | No | ID of the Account object representing this customer. |
| `default_source` | string, nullable, expandable | No | Default payment source for the customer (legacy field). |
| `delinquent` | boolean, nullable | — | Whether the customer currently has at least one unpaid invoice. |
| `description` | string, nullable | No | Arbitrary string attached to the customer for your own reference. |
| `email` | string, nullable | No | Customer's email address. |
| `individual_name` | string, nullable | No | Individual name associated with the customer. |
| `invoice_credit_balance` | object, expandable | — | Credit balance per currency, applied automatically to future invoices. |
| `invoice_prefix` | string, nullable | No | Prefix used to generate invoice numbers for this customer. |
| `invoice_settings` | object | No | Default invoice settings: `custom_fields`, `default_payment_method`, `footer`, `rendering_options`. |
| `livemode` | boolean | — | Whether the object exists in live mode (`true`) or test mode (`false`). |
| `metadata` | object | No | Set of key-value pairs. You can store up to 50 keys, each with a string value up to 500 characters. |
| `name` | string, nullable | No | Full name or business name. Maximum 256 characters. |
| `next_invoice_sequence` | integer, nullable | No | Suffix of the next invoice number generated for this customer. |
| `phone` | string, nullable | No | Customer's phone number. Maximum 20 characters. |
| `preferred_locales` | array of strings, nullable | No | Ordered list of preferred languages for communication (e.g., `["en", "de"]`). |
| `shipping` | object, nullable | No | Shipping address. Appears on invoices for this customer. |
| `sources` | object, nullable, expandable | — | Legacy payment sources attached to the customer. |
| `subscriptions` | object, nullable, expandable | — | Active subscriptions for the customer. |
| `tax` | object, expandable | No | Tax details about the customer. |
| `tax_exempt` | enum, nullable | No | Tax exemption status: `none`, `exempt`, or `reverse`. |
| `tax_ids` | object, nullable, expandable | — | Tax IDs associated with the customer. |
| `test_clock` | string, nullable, expandable | No | ID of the test clock this customer belongs to. |

---

## 2. Create a Customer

```
POST /v1/customers
```

No parameters are strictly required to create a customer. However:

- `address` is **required** if you are calculating taxes via Stripe Tax.
- `tax` is **recommended** if you are calculating taxes.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `address` | object | Conditional | Customer address. Required if calculating taxes. |
| `description` | string | No | Arbitrary string for display or internal reference. |
| `email` | string | No | Customer's email address. Maximum 512 characters. |
| `metadata` | object | No | Key-value pairs for storing structured data. |
| `name` | string | No | Full name or business name. Maximum 256 characters. |
| `payment_method` | string | No | ID of a PaymentMethod to attach to the customer. |
| `phone` | string | No | Phone number. Maximum 20 characters. |
| `shipping` | object | No | Shipping information. Appears on invoices. |
| `tax` | object | No | Tax details. Recommended if calculating taxes. |
| `balance` | integer | No | Initial account balance in cents. |
| `business_name` | string | No | Business name. |
| `cash_balance` | object | No | Cash balance settings. |
| `individual_name` | string | No | Individual name. |
| `invoice_prefix` | string | No | Prefix for invoice numbers. |
| `invoice_settings` | object | No | Default invoice settings. |
| `next_invoice_sequence` | integer | No | Starting suffix for invoice numbers. |
| `preferred_locales` | array of strings | No | Preferred languages for communication. |
| `source` | string | No | Legacy payment source token or ID. |
| `tax_exempt` | enum | No | Tax exemption status: `none`, `exempt`, `reverse`. |
| `tax_id_data` | array of objects | No | Tax IDs to add during creation. |
| `test_clock` | string | No | ID of a test clock to assign. |

### Example: Create a B2B Customer with Metadata

```bash
curl https://api.stripe.com/v1/customers \
  -u sk_test_YOUR_KEY: \
  -d name="Acme Corp" \
  -d email="billing@acmecorp.com" \
  -d phone="+14155551234" \
  -d "address[line1]=100 Market St" \
  -d "address[city]=San Francisco" \
  -d "address[state]=CA" \
  -d "address[postal_code]=94105" \
  -d "address[country]=US" \
  -d business_name="Acme Corporation" \
  -d tax_exempt=none \
  -d "metadata[tenant_id]=tenant_abc123" \
  -d "metadata[client_id]=client_456" \
  -d "metadata[company_name]=Acme Corp" \
  -d "metadata[vertical]=fintech" \
  -d "metadata[plan]=enterprise" \
  -d "invoice_settings[default_payment_method]=pm_card_visa" \
  -d "preferred_locales[0]=en"
```

---

## 3. Update a Customer

```
POST /v1/customers/:id
```

Accepts the same parameters as the create endpoint, with the following differences:

- `payment_method` is **not accepted** on update. Use the PaymentMethods API to attach or detach.
- `tax_id_data` is **not accepted** on update. Use the Tax IDs API instead.
- `test_clock` is **not accepted** on update. It can only be set at creation.
- `default_source` is **accepted** on update to change the customer's default payment source.

### Auto-Retry Behavior on Source Update

When you update a customer to a new valid card via the `source` parameter, Stripe will automatically retry the latest open invoice for each of the customer's subscriptions that:

1. Bill automatically (`collection_method: charge_automatically`)
2. Are in a `past_due` status

This retry does **not** count against the subscription's automatic retry schedule configured in your billing settings.

---

## 4. Retrieve a Customer

```
GET /v1/customers/:id
```

Retrieves the details of an existing customer by its ID.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The customer's unique identifier. |

Deleted customers remain retrievable. The response will include `"deleted": true` along with the customer's `id`. Other fields may be omitted.

---

## 5. List All Customers

```
GET /v1/customers
```

Returns a paginated list of customers.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `email` | string | No | Case-sensitive exact match filter on the customer's email. Maximum 512 characters. |
| `created` | object | No | Date filter. Accepts `gt`, `gte`, `lt`, `lte` with Unix timestamps. |
| `ending_before` | string | No | Cursor for backward pagination. |
| `limit` | integer | No | Number of results per page (default 10, max 100). |
| `starting_after` | string | No | Cursor for forward pagination. |
| `test_clock` | string | No | Filter by test clock ID. |

> **Gap:** The `email` filter is case-sensitive and exact-match only. There is no built-in fuzzy or case-insensitive email lookup on the list endpoint. Use the Search endpoint for more flexible queries.

---

## 6. Delete a Customer

```
DELETE /v1/customers/:id
```

Permanently deletes a customer. This action **cannot be undone**.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The customer's unique identifier. |

### Side Effects

- **All active subscriptions** are immediately cancelled.
- **Credit card details** are removed.
- Deleted customers **can still be retrieved** via the Retrieve endpoint (returns `"deleted": true`) for historical reference.

> **Gap:** There is no soft-delete or archive mechanism in the Stripe API. If you need to retain the customer for audit purposes while preventing future charges, consider setting `metadata` flags or removing payment methods rather than deleting.

---

## 7. Search Customers

```
GET /v1/customers/search
```

Search across customer records using the Stripe Search Query Language.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query using Stripe Search Query Language. |
| `limit` | integer | No | Number of results per page. Default 10, range 1-100. |
| `page` | string | No | Cursor for pagination across search results. |

### Consistency and Availability

- Search results are **eventually consistent**. Newly created or updated customers may take up to 1 minute to appear in search results under normal conditions.
- During outages, propagation may take **up to 1 hour**.
- Search is **not available** to merchants in India.

### Example: Search by Metadata

```bash
curl https://api.stripe.com/v1/customers/search \
  -u sk_test_YOUR_KEY: \
  -d "query=metadata['tenant_id']:'tenant_abc123'"
```

### Example: Search by Email Domain

```bash
curl https://api.stripe.com/v1/customers/search \
  -u sk_test_YOUR_KEY: \
  -d "query=email~'acmecorp.com'"
```

> **Gap:** Search is eventually consistent, making it unsuitable for read-after-write flows. If you need immediate confirmation after creating a customer, use the Retrieve endpoint with the returned `id` instead.

---

## 8. B2B Billing Patterns for Customers

### Metadata for Tenant Mapping

Use `metadata` to link Stripe customers to your internal tenant model. This enables downstream automation, reporting, and webhook routing.

Recommended keys for B2B SaaS:

| Key | Purpose |
|-----|---------|
| `tenant_id` | Your internal tenant or organization identifier. |
| `client_id` | External-facing client identifier. |
| `company_name` | Human-readable company name for dashboards and reports. |
| `vertical` | Industry vertical (e.g., `fintech`, `healthcare`, `logistics`). |

### Tax Exemption for Enterprise Customers

Set `tax_exempt` to `exempt` for VAT-exempt enterprise customers, or `reverse` for customers subject to reverse-charge VAT (common in cross-border B2B within the EU). Combine with `tax_ids` to store their VAT registration number.

### Payment Method Hierarchy

The `invoice_settings.default_payment_method` takes precedence over the customer's `default_source`. For B2B billing:

1. **`invoice_settings.default_payment_method`** (highest priority) — Set this for modern PaymentMethod-based flows.
2. **`default_source`** (legacy) — Falls back to this if no `default_payment_method` is set.
3. **Subscription-level `default_payment_method`** — Overrides customer-level settings for individual subscriptions.

### Business Name for Company Identification

Use `business_name` to store the legal entity name separately from `name`. This is useful when the billing contact (`name`) differs from the company (`business_name`), which is common in B2B.

### Preferred Locales for International B2B

Set `preferred_locales` to control the language of Stripe-generated emails (e.g., payment receipts, invoice reminders). The first locale in the array that Stripe supports is used.

### Customer Balance for Account Credits

Use the `balance` field to manage account credits:

- A **negative balance** represents a credit that will be automatically applied to the customer's next invoice.
- A **positive balance** represents an amount owed that will be added to the next invoice.

This is useful for B2B scenarios like prepaid credits, negotiated discounts, or refund-to-credit workflows.

### Example: Well-Structured B2B Customer Object

```json
{
  "id": "cus_R4bK7mZvqL2nXp",
  "object": "customer",
  "name": "Jordan Chen",
  "business_name": "Meridian Analytics Inc.",
  "email": "billing@meridiananalytics.com",
  "phone": "+14155559876",
  "address": {
    "line1": "200 Mission St",
    "line2": "Suite 1400",
    "city": "San Francisco",
    "state": "CA",
    "postal_code": "94105",
    "country": "US"
  },
  "currency": "usd",
  "balance": -50000,
  "tax_exempt": "none",
  "tax_ids": {
    "data": [
      {
        "type": "us_ein",
        "value": "12-3456789"
      }
    ]
  },
  "invoice_settings": {
    "default_payment_method": "pm_1abc2DEF3ghi4JKL",
    "custom_fields": [
      {
        "name": "PO Number",
        "value": "PO-2026-0042"
      }
    ],
    "footer": "Net 30. Questions? billing@meridiananalytics.com"
  },
  "shipping": {
    "name": "Meridian Analytics Inc.",
    "address": {
      "line1": "200 Mission St",
      "line2": "Suite 1400",
      "city": "San Francisco",
      "state": "CA",
      "postal_code": "94105",
      "country": "US"
    }
  },
  "preferred_locales": ["en"],
  "metadata": {
    "tenant_id": "tenant_meridian_001",
    "client_id": "client_ma_2026",
    "company_name": "Meridian Analytics",
    "vertical": "data_analytics",
    "plan": "enterprise",
    "contract_start": "2026-01-15",
    "csm": "alex.rivera"
  },
  "livemode": true,
  "created": 1737000000
}
```

> **Gap:** Stripe does not natively enforce uniqueness on `metadata` keys like `tenant_id` across customers. If your application requires a one-to-one mapping between tenants and Stripe customers, enforce this constraint in your own application layer or use the Search endpoint to check for duplicates before creation.

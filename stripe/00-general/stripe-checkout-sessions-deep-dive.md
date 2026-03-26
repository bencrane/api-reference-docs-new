# Stripe Checkout Sessions API Reference

**Canonical deep-dive for B2B SaaS billing integrations**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

---

## Table of Contents

1. [The Session Object](#1-the-session-object)
2. [Create a Session](#2-create-a-session)
3. [Update a Session](#3-update-a-session)
4. [Retrieve a Session](#4-retrieve-a-session)
5. [List Sessions](#5-list-sessions)
6. [Expire a Session](#6-expire-a-session)
7. [B2B SaaS Patterns](#7-b2b-saas-patterns)

---

## 1. The Session Object

A Checkout Session represents a single payment or subscription flow initiated by your application. Sessions are ephemeral — they expire after 24 hours if not completed.

| Parameter | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the Session object. |
| `mode` | enum | The mode of the Checkout Session. One of `payment`, `setup`, or `subscription`. |
| `status` | enum | Status of the Session. One of `open`, `complete`, or `expired`. |
| `payment_status` | enum | Payment status of the Session. One of `no_payment_required`, `paid`, or `unpaid`. |
| `ui_mode` | enum | The UI mode of the Session. One of `hosted_page`, `embedded_page`, or `elements`. |
| `url` | string | The hosted URL for the Checkout page. Expires 24 hours after Session creation. |
| `success_url` | string | URL the customer is redirected to after successful payment (hosted mode). |
| `return_url` | string | URL the customer is returned to after completing checkout (embedded/elements mode). |
| `cancel_url` | string | URL the customer is redirected to if they cancel checkout (hosted mode). |
| `client_reference_id` | string | A unique string (max 200 chars) to reference this Session on your system. |
| `customer` | string, expandable | ID of the Customer this Session is for. |
| `customer_email` | string | Pre-filled email for the customer. |
| `currency` | enum | Three-letter ISO currency code. |
| `line_items` | object | The line items purchased by the customer. |
| `automatic_tax` | object | Settings for automatic tax computation. |
| `metadata` | object | Set of key-value pairs for storing additional information. |
| `payment_intent` | string, expandable | The PaymentIntent associated with this Session. Present when `mode=payment`. |
| `subscription` | string, expandable | The Subscription associated with this Session. Present when `mode=subscription`. |
| `setup_intent` | string, expandable | The SetupIntent associated with this Session. Present when `mode=setup`. |
| `allow_promotion_codes` | boolean | Whether to allow promotion codes in checkout. |
| `billing_address_collection` | enum | Whether to collect billing address. |
| `consent_collection` | object | Settings for consent collection (e.g., terms of service). |
| `custom_fields` | array | Custom fields displayed during checkout. |
| `custom_text` | object | Custom text displayed at various points during checkout. |
| `discounts` | array | Discounts applied to the Session. |
| `expires_at` | timestamp | The timestamp at which the Session expires. |
| `locale` | enum | The locale used for the Checkout page (e.g., `en`, `de`, `ja`). |
| `payment_method_collection` | enum | Whether to collect payment methods. |
| `payment_method_configuration` | string | The payment method configuration used for this Session. |
| `payment_method_options` | object | Payment-method-specific configuration. |
| `payment_method_types` | array | List of accepted payment method types. |
| `phone_number_collection` | object | Settings for phone number collection. |
| `shipping_address_collection` | object | Settings for shipping address collection. |
| `shipping_options` | array | Available shipping rates for the customer to choose from. |
| `shipping_cost` | object | The shipping cost charged to the customer. |
| `shipping_details` | object | Shipping information provided by the customer. |
| `submit_type` | enum | The label for the submit button (e.g., `pay`, `book`, `donate`). |
| `tax_id_collection` | object | Settings for tax ID collection. |

> **Gap:** The Session object does not expose a direct link to the Invoice created during subscription mode. Use the `subscription` expand to reach the latest invoice.

---

## 2. Create a Session

```
POST /v1/checkout/sessions
```

### Required Parameters

| Parameter | Condition | Description |
|---|---|---|
| `mode` | Always | One of `payment`, `setup`, or `subscription`. |
| `line_items` | When `mode=payment` or `mode=subscription` | Array of items the customer is purchasing. |
| `success_url` | When `ui_mode=hosted_page` | URL to redirect to on successful payment. |
| `return_url` | When `ui_mode=embedded_page` or `ui_mode=elements` | URL to return the customer to after checkout. |

### Key Optional Parameters

| Parameter | Type | Description |
|---|---|---|
| `automatic_tax` | object | Enable automatic tax calculation. |
| `client_reference_id` | string | Your internal reference ID (max 200 chars). |
| `customer` | string | Existing Stripe Customer ID. |
| `customer_email` | string | Pre-fill the email field. |
| `metadata` | object | Key-value pairs attached to the Session. |
| `ui_mode` | enum | One of `hosted_page`, `embedded_page`, or `elements`. |

### Additional Optional Parameters

`after_expiration`, `allow_promotion_codes`, `billing_address_collection`, `cancel_url`, `consent_collection`, `currency`, `custom_fields`, `custom_text`, `customer_creation`, `customer_update`, `discounts`, `expires_at`, `invoice_creation`, `locale`, `optional_items`, `payment_intent_data`, `payment_method_collection`, `payment_method_configuration`, `payment_method_data`, `payment_method_options`, `payment_method_types`, `phone_number_collection`, `redirect_on_completion`, `saved_payment_method_options`, `setup_intent_data`, `shipping_address_collection`, `shipping_options`, `submit_type`, `subscription_data`, `tax_id_collection`

### Example: Create a Subscription Checkout Session

```bash
curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_xxx: \
  -d mode=subscription \
  -d "line_items[0][price]"=price_abc123 \
  -d "line_items[0][quantity]"=1 \
  -d success_url="https://app.example.com/billing?session_id={CHECKOUT_SESSION_ID}" \
  -d cancel_url="https://app.example.com/pricing" \
  -d client_reference_id=tenant_456 \
  -d "metadata[workspace_id]"=ws_789 \
  -d "subscription_data[metadata][workspace_id]"=ws_789
```

> **Gap:** `client_reference_id` is not automatically propagated to the resulting Subscription or PaymentIntent. You must explicitly pass metadata via `subscription_data[metadata]` or `payment_intent_data[metadata]` to ensure downstream objects carry your identifiers.

---

## 3. Update a Session

```
POST /v1/checkout/sessions/:id
```

Only Sessions with status `open` can be updated. Updatable fields:

| Parameter | Type | Description |
|---|---|---|
| `line_items` | array | Replace the line items on the Session. |
| `metadata` | object | Update metadata key-value pairs. |
| `collected_information` | object | Update collected information fields. |
| `shipping_options` | array | Update available shipping options. |

> **Gap:** You cannot update `mode`, `customer`, or `currency` after Session creation. If these need to change, expire the Session and create a new one.

---

## 4. Retrieve a Session

```
GET /v1/checkout/sessions/:id
```

Retrieve an existing Session by its ID. Use the `expand` parameter to include related objects.

### Example: Retrieve with expanded line items and customer

```bash
curl https://api.stripe.com/v1/checkout/sessions/cs_test_xxx \
  -u sk_test_xxx: \
  -d "expand[]"=line_items \
  -d "expand[]"=customer
```

---

## 5. List Sessions

```
GET /v1/checkout/sessions
```

Returns a paginated list of Checkout Sessions. Supports the following filters:

| Filter | Type | Description |
|---|---|---|
| `payment_intent` | string | Filter by PaymentIntent ID. |
| `subscription` | string | Filter by Subscription ID. |
| `customer` | string | Filter by Customer ID. |
| `status` | enum | Filter by Session status: `open`, `complete`, or `expired`. |

### Example: List completed sessions for a customer

```bash
curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_xxx: \
  -d customer=cus_abc123 \
  -d status=complete \
  -d limit=10
```

---

## 6. Expire a Session

```
POST /v1/checkout/sessions/:id/expire
```

Immediately expires a Checkout Session that is in `open` status. Once expired, the customer can no longer complete the checkout flow.

### Example

```bash
curl -X POST https://api.stripe.com/v1/checkout/sessions/cs_test_xxx/expire \
  -u sk_test_xxx:
```

> **Gap:** There is no webhook event specifically for manual expiration vs. automatic expiration. Both trigger `checkout.session.expired`. Check `expires_at` vs. the event timestamp to distinguish.

---

## 7. B2B SaaS Patterns

### Subscription Onboarding with Tenant Tracking

Use `client_reference_id` to map the Checkout Session back to your internal tenant or workspace ID. Listen for the `checkout.session.completed` webhook and read `client_reference_id` to provision the account.

```bash
curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_xxx: \
  -d mode=subscription \
  -d "line_items[0][price]"=price_growth_monthly \
  -d "line_items[0][quantity]"=1 \
  -d client_reference_id=tenant_456 \
  -d "subscription_data[metadata][tenant_id]"=tenant_456 \
  -d success_url="https://app.example.com/onboarding/complete"
```

### Setup Mode for Saving Payment Methods Before Billing

Use `mode=setup` to collect and save a payment method without charging the customer. Useful for trial-first flows where billing starts later.

```bash
curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_xxx: \
  -d mode=setup \
  -d customer=cus_abc123 \
  -d success_url="https://app.example.com/trial-started"
```

### Hosted vs. Embedded Checkout

- **Hosted (`ui_mode=hosted_page`):** Stripe-hosted page. Best for quick integrations and full PCI compliance offloading. Requires `success_url`.
- **Embedded (`ui_mode=embedded_page`):** Embed checkout in an iframe on your domain. Requires `return_url`. Better for white-label platforms.
- **Elements (`ui_mode=elements`):** Use Stripe.js Elements for full UI control. Requires `return_url`. Maximum customization.

### Passing Metadata to Subscriptions

Metadata set on the Session does not flow through to the Subscription automatically. Use `subscription_data[metadata]` to ensure your identifiers are present on the resulting Subscription object.

### Collecting Billing Address and Tax IDs for B2B Compliance

```bash
curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_xxx: \
  -d mode=subscription \
  -d "line_items[0][price]"=price_enterprise_annual \
  -d "line_items[0][quantity]"=1 \
  -d billing_address_collection=required \
  -d "tax_id_collection[enabled]"=true \
  -d "automatic_tax[enabled]"=true \
  -d success_url="https://app.example.com/billing/success"
```

> **Gap:** Tax ID collection at checkout does not validate the tax ID in real time. Validation occurs asynchronously. Listen for `customer.tax_id.updated` to confirm validity before issuing compliant invoices.

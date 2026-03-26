# Stripe Payment Intents API Reference

**Canonical reference for the Stripe Payment Intents API — the core payment orchestration primitive for B2B billing, authorization holds, and recurring server-initiated charges.**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

## Table of Contents

1. [The PaymentIntent Object](#1-the-paymentintent-object)
2. [Status Lifecycle](#2-status-lifecycle)
3. [Create a PaymentIntent](#3-create-a-paymentintent)
4. [Confirm a PaymentIntent](#4-confirm-a-paymentintent)
5. [Capture a PaymentIntent](#5-capture-a-paymentintent)
6. [Cancel a PaymentIntent](#6-cancel-a-paymentintent)
7. [Update a PaymentIntent](#7-update-a-paymentintent)
8. [Retrieve a PaymentIntent](#8-retrieve-a-paymentintent)
9. [List PaymentIntents](#9-list-paymentintents)
10. [Search PaymentIntents](#10-search-paymentintents)
11. [B2B Billing Patterns](#11-b2b-billing-patterns)

---

## 1. The PaymentIntent Object

A PaymentIntent tracks the lifecycle of a payment from creation through confirmation, processing, and final settlement. It is the recommended way to accept payments in Stripe and supports dynamic payment method selection, 3D Secure, and server-side capture flows.

### Core Fields

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | — | Unique identifier for the PaymentIntent (e.g., `pi_abc123`). |
| `amount` | integer | — | Amount intended to be collected, in the smallest currency unit (e.g., cents for USD). |
| `currency` | enum | — | Three-letter ISO 4217 currency code, lowercase (e.g., `usd`, `eur`). |
| `status` | enum | — | Current status of the PaymentIntent. See [Status Lifecycle](#2-status-lifecycle). |
| `automatic_payment_methods` | object | No | When enabled, Stripe dynamically determines payment methods to display based on currency, payment method restrictions, and other parameters. Contains `allow_redirects` and `enabled`. |
| `client_secret` | string | — | Secret used on the client side to complete a payment. Pass this to Stripe.js or the mobile SDK. |
| `customer` | string, expandable | No | ID of the Customer this PaymentIntent belongs to. Expandable to the full Customer object. |
| `customer_account` | string | No | The customer account for cross-account payments. Used in Connect platforms. |
| `description` | string | No | Arbitrary string attached to the PaymentIntent for your own reference. Appears in the dashboard. |
| `last_payment_error` | object, nullable | — | The last payment error encountered. Contains `charge`, `code`, `decline_code`, `doc_url`, `message`, `param`, `payment_method`, `type`. |
| `latest_charge` | string, expandable | — | ID of the most recent Charge created by this PaymentIntent. Expandable. |
| `metadata` | object | No | Key-value pairs for storing structured data. Up to 50 keys, each value up to 500 characters. |
| `next_action` | object, nullable | — | If present, describes the action required to continue payment (e.g., redirect to 3D Secure, display a QR code). Populated when `status=requires_action`. |
| `payment_method` | string, expandable | No | ID of the PaymentMethod used in this PaymentIntent. Expandable. |
| `receipt_email` | string, nullable | No | Email address to send the receipt to. |
| `setup_future_usage` | enum, nullable | No | Indicates that you intend to make future payments with this PaymentMethod. Values: `off_session`, `on_session`. |
| `shipping` | object, nullable | No | Shipping information for this PaymentIntent. Contains `address`, `name`, `carrier`, `phone`, `tracking_number`. |
| `statement_descriptor` | string, nullable | No | For non-card charges, the statement descriptor that appears on the customer's statement. Maximum 22 characters. |
| `statement_descriptor_suffix` | string, nullable | No | Suffix appended to the statement descriptor on card charges. Maximum 22 characters. |

### Additional Fields

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `amount_capturable` | integer | — | Amount that can be captured from this PaymentIntent (relevant for `capture_method=manual`). |
| `amount_received` | integer | — | Amount that was collected by this PaymentIntent. |
| `application` | string, expandable | — | ID of the Connect application that created the PaymentIntent. |
| `application_fee_amount` | integer, nullable | No | Application fee amount to collect on behalf of the connected account (Connect only). |
| `canceled_at` | timestamp, nullable | — | Time at which the PaymentIntent was canceled. Null if not canceled. |
| `cancellation_reason` | enum, nullable | — | Reason for cancellation: `duplicate`, `fraudulent`, `requested_by_customer`, `abandoned`. |
| `capture_method` | enum | No | Controls when funds will be captured. Values: `automatic`, `automatic_async`, `manual`. Default `automatic`. |
| `confirmation_method` | enum | — | Describes whether the PaymentIntent can be confirmed via the API or requires client-side action. Values: `automatic`, `manual`. |
| `created` | timestamp | — | Time at which the PaymentIntent was created. Measured in seconds since the Unix epoch. |
| `invoice` | string, nullable, expandable | — | ID of the invoice that created this PaymentIntent, if applicable. |
| `on_behalf_of` | string, nullable | No | The account on whose behalf the payment is made (Connect only). |
| `payment_method_configuration_details` | object, nullable | — | Information about the payment method configuration used for this PaymentIntent. |
| `payment_method_options` | object, nullable | No | Payment-method-specific configuration for this PaymentIntent (e.g., card options, bank transfer settings). |
| `payment_method_types` | array of strings | No | List of payment method types that this PaymentIntent can accept (e.g., `["card", "us_bank_account"]`). |
| `processing` | object, nullable | — | Processing information for the PaymentIntent, if currently processing. |
| `review` | string, nullable, expandable | — | ID of the review associated with this PaymentIntent, if flagged by Radar. |
| `transfer_data` | object, nullable | No | Transfer details for Connect destinations. Contains `destination` and `amount`. |
| `transfer_group` | string, nullable | No | A string that identifies related payments for Connect transfers. |

---

## 2. Status Lifecycle

A PaymentIntent moves through a well-defined set of statuses during its lifecycle:

```
requires_payment_method → requires_confirmation → requires_action → processing → succeeded
                                                                    ↓
                                                             requires_capture → succeeded (capture)

Any non-terminal status → canceled
```

| Status | Description |
|--------|-------------|
| `requires_payment_method` | The PaymentIntent has been created but no payment method has been attached. The customer must select or provide a payment method. |
| `requires_confirmation` | A payment method has been attached but the PaymentIntent has not yet been confirmed. Call the Confirm endpoint or confirm client-side. |
| `requires_action` | The payment requires additional action from the customer, such as 3D Secure authentication, redirect-based payment completion, or other multi-step flows. Inspect `next_action` for details. |
| `processing` | The payment is being processed. This is common for asynchronous payment methods (e.g., bank debits). No further action is needed; wait for a webhook. |
| `requires_capture` | The payment was authorized but not yet captured. Applies when `capture_method=manual`. Call the Capture endpoint to collect funds. Uncaptured intents expire after 7 days. |
| `succeeded` | The payment completed successfully. Funds have been collected. |
| `canceled` | The PaymentIntent was canceled. No further charges will be made. Cancellation is terminal. |

> **Gap:** Stripe does not expose a built-in timeout or auto-cancel mechanism for PaymentIntents stuck in `requires_payment_method` or `requires_confirmation`. B2B integrations should implement their own cleanup logic to cancel stale intents.

---

## 3. Create a PaymentIntent

```
POST /v1/payment_intents
```

Creates a PaymentIntent with the given amount and currency. Optionally confirm it in the same call by setting `confirm=true`.

### Required Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `amount` | integer | Yes | Amount to collect in the smallest currency unit. |
| `currency` | string | Yes | Three-letter ISO 4217 currency code. |

### Key Optional Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `automatic_payment_methods` | object | No | Enable dynamic payment method selection. Set `enabled=true`. |
| `confirm` | boolean | No | If `true`, confirm the PaymentIntent immediately upon creation. Default `false`. |
| `customer` | string | No | ID of the Customer to attach this PaymentIntent to. |
| `description` | string | No | Arbitrary string for your reference. |
| `metadata` | object | No | Key-value pairs for storing structured data. |
| `off_session` | boolean | No | Set `true` to indicate the customer is not in your checkout flow. Only valid when `confirm=true`. |
| `payment_method` | string | No | ID of the PaymentMethod to attach. |
| `receipt_email` | string | No | Email address for the payment receipt. |
| `setup_future_usage` | enum | No | Indicates that you intend to make future payments: `off_session` or `on_session`. |
| `shipping` | object | No | Shipping information for this PaymentIntent. |
| `statement_descriptor` | string | No | Statement descriptor for the charge. |
| `statement_descriptor_suffix` | string | No | Suffix appended to the statement descriptor on card charges. |

### Additional Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `application_fee_amount` | integer | No | Application fee for Connect platforms. |
| `capture_method` | enum | No | `automatic`, `automatic_async`, or `manual`. Default `automatic`. |
| `confirmation_method` | enum | No | `automatic` or `manual`. Default `automatic`. |
| `error_on_requires_action` | boolean | No | If `true`, return an error if the PaymentIntent transitions to `requires_action`. Useful for server-side-only flows. |
| `mandate` | string | No | ID of the mandate to be used for this payment. |
| `mandate_data` | object | No | Details about the mandate for this payment. |
| `on_behalf_of` | string | No | Stripe account ID for Connect payments. |
| `payment_method_configuration` | string | No | ID of the payment method configuration to use. |
| `payment_method_data` | object | No | Inline payment method data (alternative to passing a PaymentMethod ID). |
| `payment_method_options` | object | No | Payment-method-specific configuration options. |
| `payment_method_types` | array | No | List of payment method types to accept. |
| `radar_options` | object | No | Options for Radar fraud detection. Contains `session`. |
| `return_url` | string | No | URL to redirect to after the customer completes authentication. |
| `transfer_data` | object | No | Connect transfer details: `destination`, `amount`. |
| `transfer_group` | string | No | A transfer group identifier for Connect. |
| `use_stripe_sdk` | boolean | No | Set `true` when using Stripe.js or mobile SDKs for client-side confirmation. |

### Example: Create a basic PaymentIntent

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=50000 \
  -d currency=usd \
  -d customer=cus_abc123 \
  -d "metadata[contract_id]=contract_456" \
  -d "metadata[invoice_number]=INV-2026-001"
```

---

## 4. Confirm a PaymentIntent

```
POST /v1/payment_intents/:id/confirm
```

Confirms a PaymentIntent, transitioning it from `requires_confirmation` to `processing`, `requires_action`, or `succeeded`.

### Key Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `payment_method` | string | No | ID of the PaymentMethod to use for this confirmation. |
| `receipt_email` | string | No | Email address for the payment receipt. |
| `setup_future_usage` | enum | No | Indicates intent for future payments: `off_session` or `on_session`. |
| `shipping` | object | No | Shipping information. |

### Additional Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `capture_method` | enum | No | Override capture method for this confirmation. |
| `confirmation_token` | string | No | ID of the ConfirmationToken used to confirm this PaymentIntent. |
| `error_on_requires_action` | boolean | No | Fail instead of transitioning to `requires_action`. |
| `mandate` | string | No | ID of the mandate for this payment. |
| `mandate_data` | object | No | Mandate details. |
| `off_session` | boolean | No | Indicate the customer is not present. |
| `payment_method_data` | object | No | Inline payment method data. |
| `payment_method_options` | object | No | Payment-method-specific options. |
| `payment_method_types` | array | No | Payment method types to accept. |
| `radar_options` | object | No | Radar fraud detection options. |
| `return_url` | string | No | URL for post-authentication redirect. |
| `use_stripe_sdk` | boolean | No | Set `true` for client-side SDK confirmation. |

### Example: Confirm with a saved payment method

```bash
curl https://api.stripe.com/v1/payment_intents/pi_abc123/confirm \
  -u sk_test_xxx: \
  -d payment_method=pm_card_visa
```

---

## 5. Capture a PaymentIntent

```
POST /v1/payment_intents/:id/capture
```

Captures funds for a PaymentIntent that has `status=requires_capture` (i.e., created with `capture_method=manual`). If you do not capture within 7 days, the authorization expires and the PaymentIntent reverts to `requires_payment_method`.

### Key Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `amount_to_capture` | integer | No | Amount to capture. Defaults to the full `amount_capturable`. Must be less than or equal to `amount_capturable`. |
| `metadata` | object | No | Key-value pairs to update on the PaymentIntent. |

### Additional Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `application_fee_amount` | integer | No | Application fee override for Connect. |
| `final_capture` | boolean | No | If `true`, indicates this is the final capture (allows releasing remaining uncaptured funds). |
| `statement_descriptor` | string | No | Override statement descriptor for the capture. |
| `statement_descriptor_suffix` | string | No | Override statement descriptor suffix. |
| `transfer_data` | object | No | Override Connect transfer data. |

### Example: Partial capture

```bash
curl https://api.stripe.com/v1/payment_intents/pi_abc123/capture \
  -u sk_test_xxx: \
  -d amount_to_capture=30000
```

> **Gap:** Stripe does not support incremental authorizations on all payment methods. For B2B use cases where the final charge amount may change (e.g., usage-based billing), verify that your payment method supports over-capture or plan to authorize the maximum expected amount.

---

## 6. Cancel a PaymentIntent

```
POST /v1/payment_intents/:id/cancel
```

Cancels a PaymentIntent. You can cancel a PaymentIntent in any non-terminal status. Once canceled, no further charges will be made.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cancellation_reason` | enum | No | Reason for cancellation. Values: `duplicate`, `fraudulent`, `requested_by_customer`, `abandoned`. |

### Example

```bash
curl https://api.stripe.com/v1/payment_intents/pi_abc123/cancel \
  -u sk_test_xxx: \
  -d cancellation_reason=duplicate
```

---

## 7. Update a PaymentIntent

```
POST /v1/payment_intents/:id
```

Updates a PaymentIntent. You can update most fields on a PaymentIntent as long as it has not yet been confirmed. After confirmation, only `description` and `metadata` can be updated.

### Example

```bash
curl https://api.stripe.com/v1/payment_intents/pi_abc123 \
  -u sk_test_xxx: \
  -d "metadata[po_number]=PO-2026-789" \
  -d description="Annual platform license renewal"
```

---

## 8. Retrieve a PaymentIntent

```
GET /v1/payment_intents/:id
```

Retrieves a PaymentIntent by its ID. Use the `expand` parameter to include related objects.

### Example

```bash
curl https://api.stripe.com/v1/payment_intents/pi_abc123 \
  -u sk_test_xxx: \
  -G \
  -d "expand[]=latest_charge" \
  -d "expand[]=customer"
```

---

## 9. List PaymentIntents

```
GET /v1/payment_intents
```

Returns a paginated list of PaymentIntents. Supports filtering by `customer`, `created` date range, and standard pagination parameters (`limit`, `starting_after`, `ending_before`).

### Example: List recent intents for a customer

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -G \
  -d customer=cus_abc123 \
  -d limit=10
```

---

## 10. Search PaymentIntents

```
GET /v1/payment_intents/search
```

Searches PaymentIntents using Stripe's query language. Supports searching by `status`, `amount`, `currency`, `customer`, `metadata`, and more.

### Example: Search by metadata

```bash
curl https://api.stripe.com/v1/payment_intents/search \
  -u sk_test_xxx: \
  -G \
  -d "query=metadata['contract_id']:'contract_456'"
```

> **Gap:** Search results may be delayed by up to 1 minute after a PaymentIntent is created or updated. Do not rely on search for real-time lookups — use Retrieve instead.

---

## 11. B2B Billing Patterns

### Off-Session Payments for Recurring Billing

Server-initiated charges for subscription renewals, usage-based invoices, or scheduled installments. The customer is not present at the time of payment.

```bash
# Step 1: Create a PaymentIntent and save the method for future use
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=120000 \
  -d currency=usd \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d setup_future_usage=off_session

# Step 2: Later, charge the saved method off-session
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=120000 \
  -d currency=usd \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d off_session=true
```

> **Gap:** If an off-session payment fails (e.g., card declined, 3D Secure required), the PaymentIntent transitions to `requires_payment_method` or `requires_action`. Your integration must handle this by notifying the customer and providing a way to complete the payment on-session.

### Authorization Holds for Large Contracts

Use `capture_method=manual` to place an authorization hold without immediately collecting funds. This is common for enterprise contracts where final amounts may be adjusted.

```bash
# Authorize $50,000
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=5000000 \
  -d currency=usd \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d capture_method=manual \
  -d "metadata[contract_id]=contract_789"

# Capture the final negotiated amount after contract finalization
curl https://api.stripe.com/v1/payment_intents/pi_abc123/capture \
  -u sk_test_xxx: \
  -d amount_to_capture=4500000
```

> **Gap:** Authorization holds expire after 7 days for most card networks. For B2B contracts with longer negotiation cycles, consider deferring the PaymentIntent creation until the amount is finalized, or use extended authorizations (available on select Visa and Mastercard transactions via Stripe).

### Saving Payment Methods for Recurring Charges

Set `setup_future_usage=off_session` on the initial PaymentIntent to indicate to Stripe that the payment method will be reused for future server-initiated charges. This optimizes for SCA exemptions in Europe.

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=25000 \
  -d currency=eur \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d setup_future_usage=off_session
```

### 3D Secure / SCA Handling for European B2B

Strong Customer Authentication (SCA) applies to European Economic Area transactions. When `status=requires_action`, redirect the customer to complete authentication.

```bash
# Create with error_on_requires_action for fully server-side flow
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=75000 \
  -d currency=eur \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d error_on_requires_action=true \
  -d off_session=true
```

If the above returns an error with `code=authentication_required`, the payment cannot be completed server-side. You must bring the customer back on-session to complete authentication.

> **Gap:** B2B transactions between two businesses may qualify for SCA exemptions (e.g., merchant-initiated transactions, recurring fixed-amount payments). Stripe handles exemption requests automatically when `setup_future_usage` or `off_session` is set correctly, but exemption approval is at the issuing bank's discretion.

### Collecting Setup Fees as One-Time PaymentIntents

For B2B onboarding flows, collect a one-time setup fee while simultaneously saving the payment method for future recurring charges.

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=50000 \
  -d currency=usd \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d setup_future_usage=off_session \
  -d "metadata[charge_type]=setup_fee" \
  -d "metadata[plan]=enterprise_annual"
```

### Server-Side-Only Flows with error_on_requires_action

For fully automated billing pipelines where no customer interaction is possible, set `error_on_requires_action=true`. This causes the PaymentIntent to fail immediately if 3D Secure or other interactive authentication is required, rather than entering the `requires_action` state.

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=99900 \
  -d currency=usd \
  -d customer=cus_abc123 \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d off_session=true \
  -d error_on_requires_action=true \
  -d "metadata[billing_cycle]=2026-03"
```

> **Gap:** When `error_on_requires_action` is used and the payment fails, the PaymentIntent remains in `requires_payment_method`. Your billing pipeline should have a fallback strategy: retry with a different payment method, queue the payment for manual review, or send the customer an email with a hosted payment link.

---

*This reference covers the Stripe Payment Intents API as of 2026-03-26. For the full Stripe API surface, see the [master-docs-overview.md](master-docs-overview.md).*

# Stripe Payment Methods API Reference

**Canonical API reference for Stripe Payment Methods — B2B SaaS billing focus**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

---

## Table of Contents

1. [Payment Method Object](#1-payment-method-object)
2. [Create Payment Method](#2-create-payment-method)
3. [Attach to Customer](#3-attach-to-customer)
4. [Detach from Customer](#4-detach-from-customer)
5. [Update Payment Method](#5-update-payment-method)
6. [Retrieve Payment Method](#6-retrieve-payment-method)
7. [List Payment Methods](#7-list-payment-methods)
8. [SetupIntents (Save for Future Use)](#8-setupintents-save-for-future-use)
9. [Payment Method Hierarchy](#9-payment-method-hierarchy)
10. [B2B Patterns](#10-b2b-patterns)

---

## 1. Payment Method Object

### Top-Level Fields

| Parameter | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the payment method |
| `type` | enum | Payment method type. 55+ types. B2B-relevant: `card`, `us_bank_account`, `sepa_debit`, `bacs_debit`, `customer_balance`, `link`, `pay_by_bank` |
| `billing_details` | object | Billing information: `address`, `email`, `name`, `phone` |
| `customer` | string, nullable, expandable | ID of the customer this payment method is attached to |
| `metadata` | object | Set of key-value pairs for storing additional information |
| `allow_redisplay` | enum | Controls whether the payment method can be shown again to the customer in a checkout flow |
| `created` | integer | Timestamp of when the payment method was created |
| `livemode` | boolean | Whether the object exists in live mode |

### Card Sub-Object (`payment_method.card`)

| Field | Type | Description |
|---|---|---|
| `brand` | string | Card brand: `visa`, `mastercard`, `amex`, `discover`, etc. |
| `checks` | object | Card verification checks: `address_line1_check`, `address_postal_code_check`, `cvc_check` |
| `country` | string | Two-letter ISO country code of the issuing country |
| `exp_month` | integer | Expiration month (1-12) |
| `exp_year` | integer | Four-digit expiration year |
| `fingerprint` | string | Uniquely identifies this card number; use for deduplication |
| `funding` | string | `credit`, `debit`, `prepaid`, or `unknown` |
| `last4` | string | Last four digits of the card number |
| `networks` | object | Available card networks and preferred network |
| `wallet` | object, nullable | If the card is stored in a digital wallet (Apple Pay, Google Pay, etc.) |

### US Bank Account Sub-Object (`payment_method.us_bank_account`)

| Field | Type | Description |
|---|---|---|
| `account_holder_type` | string | `individual` or `company` |
| `account_type` | string | `checking` or `savings` |
| `bank_name` | string | Name of the bank |
| `financial_connections_account` | string | ID of the Financial Connections account used to create this payment method |
| `fingerprint` | string | Uniquely identifies this bank account |
| `last4` | string | Last four digits of the account number |
| `routing_number` | string | Routing number of the bank account |

---

## 2. Create Payment Method

**`POST /v1/payment_methods`**

| Parameter | Required | Type | Description |
|---|---|---|---|
| `type` | **Yes** | string | The type of payment method to create |
| `billing_details` | No | object | Billing information (address, email, name, phone) |
| `metadata` | No | object | Key-value pairs |
| Type-specific params | No | object | e.g., `card` object with `number`, `exp_month`, `exp_year`, `cvc`; or `us_bank_account` with `account_holder_type`, `account_number`, `routing_number` |

```bash
curl https://api.stripe.com/v1/payment_methods \
  -u sk_test_key: \
  -d type=card \
  -d "card[number]"=4242424242424242 \
  -d "card[exp_month]"=12 \
  -d "card[exp_year]"=2027 \
  -d "card[cvc]"=314
```

**Note:** In most integrations, payment method creation is handled client-side via Stripe.js or Stripe Elements to avoid PCI compliance scope on your server.

---

## 3. Attach to Customer

**`POST /v1/payment_methods/:id/attach`**

| Parameter | Required | Type | Description |
|---|---|---|---|
| `customer` | **Yes** | string | The ID of the customer to attach the payment method to |

Attaches an unattached PaymentMethod to a Customer. Once attached, it can be used for future payments on behalf of that customer.

```bash
curl https://api.stripe.com/v1/payment_methods/pm_1234/attach \
  -u sk_test_key: \
  -d customer=cus_5678
```

---

## 4. Detach from Customer

**`POST /v1/payment_methods/:id/detach`**

Detaches the payment method from its customer. No parameters required.

After detaching, the payment method can no longer be used for payments. It cannot be re-attached to another customer.

```bash
curl -X POST https://api.stripe.com/v1/payment_methods/pm_1234/detach \
  -u sk_test_key:
```

---

## 5. Update Payment Method

**`POST /v1/payment_methods/:id`**

| Parameter | Required | Type | Description |
|---|---|---|---|
| `billing_details` | No | object | Update billing information |
| `metadata` | No | object | Update key-value pairs |
| `card` | No | object | For card payment methods: update `exp_month` and `exp_year` only |

---

## 6. Retrieve Payment Method

**`GET /v1/payment_methods/:id`**

Returns the payment method object.

---

## 7. List Payment Methods

**`GET /v1/payment_methods`**

| Parameter | Required | Type | Description |
|---|---|---|---|
| `customer` | **Yes** | string | Filter by customer ID |
| `type` | No | string | Filter by payment method type |

Standard list pagination: `ending_before`, `starting_after`, `limit`.

**Alternative endpoint:**

**`GET /v1/customers/:id/payment_methods`**

Same functionality, accessed via the customer resource path.

---

## 8. SetupIntents (Save for Future Use)

SetupIntents allow you to save a payment method for future use without making an immediate charge. This is essential for B2B SaaS where you collect payment details during onboarding and charge later.

### Create SetupIntent

**`POST /v1/setup_intents`**

| Parameter | Required | Type | Description |
|---|---|---|---|
| `customer` | No | string | Customer ID. Payment method auto-attaches to this customer on success |
| `payment_method` | No | string | ID of payment method to set up |
| `usage` | No | string | `off_session` (default) or `on_session`. `off_session` optimizes for future server-initiated charges |
| `confirm` | No | boolean | Set to `true` to confirm the SetupIntent immediately |
| `payment_method_types` | No | array | Allowed payment method types |
| `metadata` | No | object | Key-value pairs |

### SetupIntent Status Flow

```
requires_payment_method → requires_confirmation → requires_action → processing → succeeded
                                                                                ↘ canceled
```

| Status | Description |
|---|---|
| `requires_payment_method` | No payment method attached yet |
| `requires_confirmation` | Payment method attached, awaiting confirmation |
| `requires_action` | Customer action needed (e.g., 3D Secure authentication) |
| `processing` | Setup is being processed |
| `succeeded` | Payment method saved and ready for future use |
| `canceled` | SetupIntent was canceled |

### `off_session` Usage

Setting `usage: 'off_session'` tells Stripe to optimize for future server-initiated charges. This is critical for EU customers subject to Strong Customer Authentication (SCA) — it triggers the necessary authentication upfront so that future off-session charges can proceed without customer interaction.

---

## 9. Payment Method Hierarchy

When Stripe processes a payment on an invoice, the payment method is resolved in the following priority order:

| Priority | Source | Field |
|---|---|---|
| 1 (highest) | Invoice | `default_payment_method` |
| 2 | Subscription | `default_payment_method` |
| 3 | Customer | `invoice_settings.default_payment_method` |
| 4 (lowest, legacy) | Customer | `default_source` |

If none of these are set, the invoice cannot be automatically collected and will require manual payment.

**Recommendation:** For B2B SaaS, set the payment method at the **customer** level (`invoice_settings.default_payment_method`) unless you have customers with multiple subscriptions using different payment methods.

---

## 10. B2B Patterns

### ACH (`us_bank_account`) for Lower-Fee Enterprise Billing

ACH transfers have significantly lower fees than card payments (capped at $5 vs. 2.9% + 30c for cards). For enterprise customers with large invoices, ACH can save substantial processing costs.

- Use Financial Connections to verify bank accounts instantly (preferred over microdeposits)
- ACH payments are not instant — typically settle in 4-5 business days
- Handle `checkout.session.async_payment_succeeded` and `checkout.session.async_payment_failed` for ACH via Checkout

### SetupIntents with `off_session` for Recurring B2B Invoices

1. During onboarding, create a SetupIntent with `usage: 'off_session'` and `customer` set
2. Complete authentication on the client side (handles SCA for EU)
3. On success, the payment method is automatically attached to the customer
4. Set as default: `POST /v1/customers/:id` with `invoice_settings.default_payment_method`
5. Future subscription invoices will charge this method automatically

### Card on File for Automatic Collection

The most common B2B pattern:

1. Collect card via Stripe Elements or Checkout
2. Attach to customer and set as default payment method
3. Create subscription — Stripe handles automatic billing each cycle
4. Monitor `invoice.payment_failed` for failed charges

### SEPA Direct Debit for European B2B

- Lower fees than card payments for European transactions
- Requires a mandate (authorization from the customer)
- Settlement takes 5-7 business days
- Use SetupIntents to collect mandate and save the payment method

### Payment Method Self-Service via Billing Portal

Stripe's Billing Portal allows customers to manage their own payment methods:

- Update card on file
- Add a new payment method
- View payment history

Create a portal session with `POST /v1/billing_portal/sessions` and redirect the customer to the returned URL.

---

> **Gap:** Detailed card verification (CVC, AVS) checks behavior not in scraped docs. Bank account verification flow (microdeposits) referenced but not detailed.

# Stripe Connect API Reference

**Platform and marketplace billing infrastructure for accepting payments, managing connected accounts, and distributing funds to third parties.**

Generated: 2026-03-26
**Parent:** [master-docs-overview.md](master-docs-overview.md)

---

## Table of Contents

1. [Overview](#1-overview)
2. [Account Types Comparison](#2-account-types-comparison)
3. [The Account Object (Key Attributes)](#3-the-account-object-key-attributes)
4. [Create an Account](#4-create-an-account)
5. [Account Links](#5-account-links)
6. [Transfers](#6-transfers)
7. [Application Fees](#7-application-fees)
8. [Charge Types on Connect](#8-charge-types-on-connect)
9. [B2B Platform Patterns](#9-b2b-platform-patterns)

---

## 1. Overview

Stripe Connect enables platforms and marketplaces to accept payments on behalf of others, pay out to third parties, and manage connected business accounts. Connect provides the building blocks for multi-party payment flows, onboarding, identity verification, and compliance.

Three account types are available, each offering a different balance of control, onboarding complexity, and customization:

- **Standard** — Connected account owners use their own Stripe Dashboard and handle disputes directly.
- **Express** — Stripe provides a lightweight onboarding flow and a limited dashboard for the connected account.
- **Custom** — The platform controls the entire experience: onboarding UI, dashboard, and communication with the connected account.

---

## 2. Account Types Comparison

| Feature | Standard | Express | Custom |
|---|---|---|---|
| **Dashboard access** | Full Stripe Dashboard | Stripe Express Dashboard | None (platform-managed) |
| **Onboarding flow** | Stripe-hosted (OAuth) | Stripe-hosted (embedded) | Platform-built (API-driven) |
| **Branding** | Stripe-branded | Platform + Stripe co-branded | Fully platform-branded |
| **API complexity** | Low | Medium | High |
| **Best for** | Platforms where users already have or want Stripe accounts | Marketplaces needing quick onboarding with some Stripe UI | Platforms requiring full white-label control |

---

## 3. The Account Object (Key Attributes)

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the account (e.g., `acct_1A2B3C4D5E`). |
| `type` | enum | Account type: `standard`, `express`, or `custom`. |
| `business_type` | enum | One of `company`, `government_entity`, `individual`, or `non_profit`. |
| `business_profile` | object | Contains `mcc`, `name`, `product_description`, `support_address`, `support_email`, `support_phone`, `support_url`, and `url`. |
| `capabilities` | object | Hash of requested capabilities and their states (e.g., `card_payments: "active"`). |
| `charges_enabled` | boolean | Whether the account can create charges. |
| `payouts_enabled` | boolean | Whether the account can receive payouts. |
| `country` | string | Two-letter ISO country code (e.g., `US`). |
| `default_currency` | string | Three-letter ISO currency code for the account's default currency. |
| `email` | string, nullable | Email address associated with the account. |
| `external_accounts` | object | List of bank accounts and debit cards attached for payouts. |
| `requirements` | object | Contains `currently_due`, `eventually_due`, `past_due`, `pending_verification`, and `current_deadline` arrays describing what information is needed. |
| `settings` | object | Sub-objects for `branding`, `card_payments`, `dashboard`, `payments`, `payout_schedule`, and `payouts`. |
| `tos_acceptance` | object | Details of Terms of Service acceptance: `date`, `ip`, `user_agent`. |
| `metadata` | object | Arbitrary key-value pairs attached to the account. |

---

## 4. Create an Account

**Endpoint:** `POST /v1/accounts`

### Required / Primary Parameters

| Parameter | Type | Description |
|---|---|---|
| `type` | enum | `standard`, `express`, or `custom`. |
| `business_type` | enum | `company`, `government_entity`, `individual`, or `non_profit`. |
| `capabilities` | object | Required for Custom accounts. Hash of capabilities to request (e.g., `{card_payments: {requested: true}}`). |
| `company` | object | Information about the company or business entity. |
| `controller` | object | Properties of the platform-controlled account relationship. |
| `country` | string | Two-letter ISO code. Defaults to platform's country. |
| `email` | string | Email address for the account holder. |
| `individual` | object | Information about the person represented by the account (for `individual` business type). |
| `metadata` | object | Arbitrary key-value pairs. |
| `tos_acceptance` | object | Details of ToS acceptance. Required for Custom accounts. |

### Additional Parameters

| Parameter | Type | Description |
|---|---|---|
| `account_token` | string | An account token, used to securely pass account details from the frontend. |
| `business_profile` | object | Business information: MCC, name, support details, URL. |
| `default_currency` | string | Override the default currency for the account. |
| `documents` | object | Documents that may be submitted to satisfy verification requirements. |
| `external_account` | object | Bank account or debit card to attach for payouts. |
| `settings` | object | Account settings: branding, card_payments, payments, payouts. |

### Example: Create a Custom Account

```bash
curl https://api.stripe.com/v1/accounts \
  -u sk_test_xxx: \
  -d type=custom \
  -d country=US \
  -d email="platform-user@example.com" \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "business_type"=company \
  -d "tos_acceptance[date]"=1680000000 \
  -d "tos_acceptance[ip]"="8.8.8.8"
```

---

## 5. Account Links

**Endpoint:** `POST /v1/account_links`

Account Links generate temporary URLs that redirect Express or Custom connected accounts into Stripe-hosted onboarding or update flows. These links are single-use and expire after a short period.

| Parameter | Type | Description |
|---|---|---|
| `account` | string | **Required.** The ID of the connected account. |
| `refresh_url` | string | **Required.** URL to redirect the user if the link expires or is invalid. |
| `return_url` | string | **Required.** URL to redirect the user after they complete onboarding. |
| `type` | enum | **Required.** `account_onboarding` or `account_update`. |
| `collect` | enum | Specifies whether to collect `currently_due` or `eventually_due` requirements. |
| `collection_options` | object | Specifies options for fields and future requirements collection. |

### Example: Generate an Onboarding Link

```bash
curl https://api.stripe.com/v1/account_links \
  -u sk_test_xxx: \
  -d account=acct_1A2B3C4D5E \
  -d refresh_url="https://example.com/reauth" \
  -d return_url="https://example.com/onboarding-complete" \
  -d type=account_onboarding
```

---

## 6. Transfers

Transfers move funds from the platform's Stripe balance to a connected account's balance.

**Endpoint:** `POST /v1/transfers`

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `amount` | integer | **Required.** Amount in the smallest currency unit (e.g., cents). |
| `currency` | string | **Required.** Three-letter ISO currency code. |
| `destination` | string | **Required.** ID of the connected account to receive funds. |
| `description` | string | Arbitrary description attached to the transfer. |
| `metadata` | object | Key-value pairs for the transfer. |
| `source_transaction` | string | A charge ID to pull funds from, rather than the platform's available balance. |
| `transfer_group` | string | Identifier linking related charges and transfers. |

### Example: Transfer to a Connected Account

```bash
curl https://api.stripe.com/v1/transfers \
  -u sk_test_xxx: \
  -d amount=5000 \
  -d currency=usd \
  -d destination=acct_1A2B3C4D5E \
  -d transfer_group="ORDER_123"
```

> **Note:** The platform must have sufficient available balance. If funds are insufficient, Stripe returns an `Insufficient Funds` error. Use `source_transaction` to tie the transfer to a specific charge's funds.

---

## 7. Application Fees

Application fees are automatically collected when charges are made through a platform using `application_fee_amount` or the legacy `application_fee` parameter. They represent the platform's revenue from each transaction.

### Key Attributes

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the application fee. |
| `amount` | integer | Fee amount collected, in smallest currency unit. |
| `account` | string | ID of the connected account the charge was made on behalf of. |
| `charge` | string | ID of the charge that generated this fee. |
| `refunds` | list | List of fee refunds applied. |
| `amount_refunded` | integer | Total amount refunded back to the connected account. |

### Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/v1/application_fees/:id` | Retrieve a single application fee. |
| `GET` | `/v1/application_fees` | List application fees. Filter by `charge` to find fees for a specific charge. |

> **Note:** Application fees are read-only via the API. They are created automatically when a charge includes `application_fee_amount`. There are no create or update endpoints.

---

## 8. Charge Types on Connect

Stripe Connect supports three charge patterns, each suited to different platform architectures:

### Direct Charges

The charge is created directly on the connected account. The platform authenticates the request using the `Stripe-Account` header.

```bash
curl https://api.stripe.com/v1/charges \
  -u sk_test_xxx: \
  -H "Stripe-Account: acct_1A2B3C4D5E" \
  -d amount=2000 \
  -d currency=usd \
  -d source=tok_visa
```

- The connected account is the merchant of record.
- The connected account's statement descriptor appears on the customer's statement.
- Refunds and disputes are handled by the connected account.

### Destination Charges

The charge is created on the platform's account, and Stripe automatically transfers funds to the connected account specified in `transfer_data.destination`.

```bash
curl https://api.stripe.com/v1/charges \
  -u sk_test_xxx: \
  -d amount=2000 \
  -d currency=usd \
  -d source=tok_visa \
  -d "transfer_data[destination]"=acct_1A2B3C4D5E \
  -d application_fee_amount=200
```

- The platform is the merchant of record.
- The platform's statement descriptor appears on the customer's statement.
- The platform handles refunds and disputes.

### Separate Charges and Transfers

The platform creates a charge on its own account and later creates one or more transfers to connected accounts. This pattern supports splitting a single payment across multiple recipients.

```bash
# Step 1: Charge the customer
curl https://api.stripe.com/v1/charges \
  -u sk_test_xxx: \
  -d amount=10000 \
  -d currency=usd \
  -d source=tok_visa \
  -d transfer_group="ORDER_456"

# Step 2: Transfer to connected accounts
curl https://api.stripe.com/v1/transfers \
  -u sk_test_xxx: \
  -d amount=7000 \
  -d currency=usd \
  -d destination=acct_PROVIDER_A \
  -d transfer_group="ORDER_456"

curl https://api.stripe.com/v1/transfers \
  -u sk_test_xxx: \
  -d amount=2000 \
  -d currency=usd \
  -d destination=acct_PROVIDER_B \
  -d transfer_group="ORDER_456"
```

- Most flexible pattern; supports multi-party splits.
- Platform retains full control over timing and amounts.
- Use `transfer_group` to link related charges and transfers.

---

## 9. B2B Platform Patterns

### Agency Billing and Payouts

An agency bills its clients for services and pays out to service providers (freelancers, contractors, vendors). The agency acts as the platform, each service provider is a connected account.

- Use **destination charges** to bill clients, routing funds to the provider's connected account.
- Collect the agency's margin via `application_fee_amount`.
- Use **separate charges and transfers** when a single client invoice covers multiple providers.

### Marketplace with Platform Fees

A marketplace connects buyers and sellers, collecting a platform fee on each transaction.

```bash
# Destination charge with application fee
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=5000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d "transfer_data[destination]"=acct_SELLER_123 \
  -d application_fee_amount=750
```

In this example, the marketplace charges the buyer $50.00, transfers $42.50 to the seller, and retains $7.50 as the platform fee.

### White-Label Billing with Custom Accounts

Platforms that need full brand control use Custom accounts. The end customer never sees Stripe branding. The platform builds its own onboarding UI, collects identity verification via the API, and manages all communication with the connected account.

- Use `POST /v1/accounts` with `type=custom` and request the needed `capabilities`.
- Build onboarding with `POST /v1/account_links` or the embedded onboarding component.
- Handle `requirements` updates to keep accounts in good standing.

### Multi-Party Payments with Transfer Groups

When a single order involves multiple vendors or service providers, use transfer groups to link the charge with multiple transfers:

```bash
# Charge the customer
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_xxx: \
  -d amount=20000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d transfer_group="ORDER_789"

# Pay vendor A
curl https://api.stripe.com/v1/transfers \
  -u sk_test_xxx: \
  -d amount=12000 \
  -d currency=usd \
  -d destination=acct_VENDOR_A \
  -d transfer_group="ORDER_789"

# Pay vendor B
curl https://api.stripe.com/v1/transfers \
  -u sk_test_xxx: \
  -d amount=5000 \
  -d currency=usd \
  -d destination=acct_VENDOR_B \
  -d transfer_group="ORDER_789"

# Platform retains $30.00
```

---

> **Gap:** Account Links, Account Sessions, Login Links, and Capabilities source files were not read in detail. The onboarding flow documentation is summarized from context.

> **Gap:** Payout schedules, negative balance handling, and dispute responsibility across connected accounts are not covered in the source material.

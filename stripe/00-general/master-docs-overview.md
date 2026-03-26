# Stripe Billing API Reference for B2B SaaS Integration

**Canonical technical reference for Stripe's billing, payments, and subscription APIs — scoped to multi-tenant B2B service businesses**

Generated: 2026-03-26

This document covers the Stripe API surface relevant to engineers building billing for B2B service businesses: agencies, lead generation platforms, insurance GTM, and performance marketing firms. It covers setup fees, monthly retainers, per-lead/per-action pricing, usage-based billing, client self-service, and multi-tenant payment collection. Tier 1 sections (deep coverage) link to dedicated deep-dive files. Tier 2 and Tier 3 sections are documented inline.

---

## Table of Contents

**Tier 1 — Deep-Dive References**

1. [Authentication & API Conventions](#1-authentication--api-conventions)
2. [Core Billing Architecture](#2-core-billing-architecture)
3. [Customers](#3-customers)
4. [Products & Prices](#4-products--prices)
5. [Subscriptions](#5-subscriptions)
6. [Invoices](#6-invoices)
7. [Checkout Sessions](#7-checkout-sessions)
8. [Billing Portal](#8-billing-portal)
9. [Webhooks](#9-webhooks)
10. [Payment Methods](#10-payment-methods)
11. [Payment Intents](#11-payment-intents)

**Tier 2 — Moderate Coverage (Inline)**

12. [Charges & Refunds](#12-charges--refunds)
13. [Coupons, Promotion Codes & Discounts](#13-coupons-promotion-codes--discounts)
14. [Usage Records & Metered Billing](#14-usage-records--metered-billing)
15. [Tax Rates & Tax IDs](#15-tax-rates--tax-ids)
16. [Connect (Platforms & Marketplaces)](#16-connect-platforms--marketplaces)
17. [Disputes](#17-disputes)

**Tier 3 — Light Coverage (Inline)**

18. [Payment Links](#18-payment-links)
19. [Quotes](#19-quotes)
20. [Terminal, Issuing & Treasury](#20-terminal-issuing--treasury)
21. [Identity, Radar, Sigma & Reporting](#21-identity-radar-sigma--reporting)
22. [Climate & Financial Connections](#22-climate--financial-connections)

**Cross-Cutting**

23. [B2B Billing Integration Patterns](#23-b2b-billing-integration-patterns)
24. [Gaps & Missing Documentation](#24-gaps--missing-documentation)

---

## 1. Authentication & API Conventions

### Authentication

Stripe uses API keys for authentication. Every request must include a key via the `Authorization` header.

| Key Type | Prefix | Usage | Scope |
|---|---|---|---|
| Secret key | `sk_live_` / `sk_test_` | Server-side only. Full API access. | All operations |
| Publishable key | `pk_live_` / `pk_test_` | Client-side (Stripe.js, mobile SDKs). | Token creation, Checkout, Elements |
| Restricted key | `rk_live_` / `rk_test_` | Server-side with limited permissions. | Configurable per resource |

```bash
curl https://api.stripe.com/v1/customers \
  -u "sk_test_your_key:"
```

For Connect platforms, pass the `Stripe-Account` header to make requests on behalf of connected accounts:

```bash
curl https://api.stripe.com/v1/charges \
  -u "sk_test_your_key:" \
  -H "Stripe-Account: acct_connected_id"
```

### Common API Patterns

**Base URL:** `https://api.stripe.com/v1/`

**Pagination:** All list endpoints support cursor-based pagination.

| Parameter | Type | Description |
|---|---|---|
| `limit` | integer | Number of objects to return (1–100, default 10) |
| `starting_after` | string | Cursor for forward pagination (object ID) |
| `ending_before` | string | Cursor for backward pagination (object ID) |

**Idempotency:** Include an `Idempotency-Key` header to safely retry requests. Keys expire after 24 hours.

```bash
curl https://api.stripe.com/v1/customers \
  -u "sk_test_key:" \
  -H "Idempotency-Key: unique_request_id" \
  -d "email=client@agency.com"
```

**Metadata:** Most objects support a `metadata` hash (up to 50 keys, key max 40 chars, value max 500 chars). Essential for B2B multi-tenant tracking:

```bash
curl https://api.stripe.com/v1/customers \
  -u "sk_test_key:" \
  -d "metadata[tenant_id]=tenant_abc" \
  -d "metadata[client_id]=client_123" \
  -d "metadata[campaign_id]=camp_456"
```

**Expanding Objects:** Nested object IDs can be expanded inline using the `expand[]` parameter:

```bash
curl https://api.stripe.com/v1/invoices/in_xxx \
  -u "sk_test_key:" \
  -d "expand[]=customer" \
  -d "expand[]=subscription"
```

**Versioning:** Set `Stripe-Version` header or pin via Dashboard. Events are rendered in the API version of the webhook endpoint (or account default).

**Search:** Customers, Subscriptions, Invoices, Prices, Products, Charges, and PaymentIntents support `GET /v1/{resource}/search` with Stripe Query Language. Search is eventually consistent (typically <1 minute delay). Not available to merchants in India.

---

## 2. Core Billing Architecture

### How Stripe Billing Objects Relate

```
Product  ──→  Price  ──→  Subscription  ──→  Invoice  ──→  PaymentIntent  ──→  Charge
  │              │              │                │               │
  │              │              ├─ items[]        ├─ lines[]      ├─ payment_method
  │              │              ├─ schedule       ├─ customer     └─ outcome
  │              ├─ recurring   ├─ trial_end      ├─ discounts
  │              ├─ tiers[]     └─ discounts      └─ status
  │              └─ billing_scheme                    (draft→open→paid)
  └─ tax_code
```

**Core Object Relationships:**
- A **Product** represents what you sell (e.g., "Lead Generation Service")
- A **Price** defines how much and how often (e.g., "$500/month" or "$2.50/lead metered")
- A **Subscription** binds a Customer to one or more Prices, generating Invoices on a schedule
- An **Invoice** is the billing document; it triggers a **PaymentIntent** for collection
- A **PaymentIntent** orchestrates the actual payment flow, producing a **Charge**
- A **Customer** owns subscriptions, payment methods, invoices, and metadata

**Payment Method Hierarchy (which method gets charged):**
1. Invoice's `default_payment_method`
2. Subscription's `default_payment_method`
3. Customer's `invoice_settings.default_payment_method`
4. Customer's `default_source` (legacy)

---

## 3. Customers

Customers are the foundation of Stripe billing — every subscription, invoice, and payment method belongs to a Customer. In B2B, each Customer typically represents a client company.

**Key Attributes:** `id`, `email`, `name`, `metadata`, `invoice_settings`, `tax_exempt`, `balance`, `default_payment_method`

**Endpoints:** Create, Update, Retrieve, List, Delete, Search

**B2B Pattern:** Use `metadata` for tenant mapping (`tenant_id`, `client_id`), `business_name` for company name, `tax_exempt` for VAT-exempt enterprises, and `invoice_settings.default_payment_method` for the client's preferred payment method.

See: [stripe-customers-deep-dive.md](stripe-customers-deep-dive.md)

---

## 4. Products & Prices

Products define your service catalog; Prices define billing terms. Together they model setup fees, retainers, per-lead pricing, and tiered usage.

**Key Concepts:**
- `billing_scheme`: `per_unit` (fixed price × quantity) or `tiered` (volume/graduated tiers)
- `tiers_mode`: `volume` (all units at same tier) or `graduated` (each tier priced separately)
- `recurring.usage_type`: `licensed` (fixed quantity) or `metered` (usage-reported)
- `type`: `one_time` (setup fees) or `recurring` (subscriptions)

**Endpoints:** Product CRUD + Search, Price CRUD + Search

See: [stripe-products-prices-deep-dive.md](stripe-products-prices-deep-dive.md)

---

## 5. Subscriptions

Subscriptions automate recurring billing. They manage lifecycle (trial → active → canceled), proration on plan changes, pause/resume, and multi-item billing.

**Key Attributes:** `status` (8 states: `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, `paused`), `items[]`, `billing_cycle_anchor`, `collection_method`, `cancel_at_period_end`

**Endpoints:** Create, Update, Retrieve, List, Cancel, Resume, Search

**B2B Pattern:** Use `collection_method=send_invoice` with `days_until_due=30` for net-30 enterprise billing. Use subscription items for multi-service bundles. Use `cancel_at_period_end` for graceful contract endings.

See: [stripe-subscriptions-deep-dive.md](stripe-subscriptions-deep-dive.md)

---

## 6. Invoices

Invoices are the billing documents that drive payment collection. They support draft editing, line item management, finalization, and multiple payment collection methods.

**Key Attributes:** `status` (`draft` → `open` → `paid` / `uncollectible` / `void`), `collection_method`, `lines[]`, `amount_due`, `hosted_invoice_url`

**Endpoints:** Create, Update, Retrieve, List, Delete, Finalize, Pay, Void, Send, Add Lines, Create Preview, Search (18 total)

**B2B Pattern:** Create one-off invoices for setup fees. Use `collection_method=send_invoice` for enterprise clients who pay by check/wire. Use `add_lines` to itemize deliverables.

See: [stripe-invoices-deep-dive.md](stripe-invoices-deep-dive.md)

---

## 7. Checkout Sessions

Checkout Sessions create Stripe-hosted or embedded payment pages for one-time payments, subscription signups, or saving payment methods.

**Key Attributes:** `mode` (`payment` | `setup` | `subscription`), `ui_mode` (`hosted_page` | `embedded_page` | `elements`), `line_items[]`, `success_url`, `return_url`

**Endpoints:** Create, Update, Retrieve, List, Expire, List Line Items

**B2B Pattern:** Use `mode=subscription` for client onboarding flows. Use `mode=setup` to save payment methods before billing starts. Pass `metadata` and `client_reference_id` for tenant tracking.

See: [stripe-checkout-sessions-deep-dive.md](stripe-checkout-sessions-deep-dive.md)

---

## 8. Billing Portal

The Billing Portal provides customer self-service for managing subscriptions, payment methods, and invoice history.

**Key Attributes:** Portal Configurations define features (subscription cancel/update, payment method update, invoice history). Portal Sessions create short-lived URLs for customer access.

**Endpoints:** Configuration CRUD, Session Create

**B2B Pattern:** Enable `subscription_cancel` with `cancellation_reason` to capture churn data. Enable `subscription_update` to let clients upgrade/downgrade plans. Configure `default_return_url` to redirect back to your platform.

See: [stripe-billing-portal-deep-dive.md](stripe-billing-portal-deep-dive.md)

---

## 9. Webhooks

Webhooks deliver real-time event notifications for subscription lifecycle changes, payment outcomes, invoice finalization, and dispute creation.

**Key Attributes:** `enabled_events[]`, `url`, `secret` (for signature verification), `status`

**Endpoints:** Create, Update, Retrieve, List, Delete

**B2B Pattern:** Subscribe to `invoice.paid`, `invoice.payment_failed`, `customer.subscription.updated`, `customer.subscription.deleted` at minimum. Verify signatures on every webhook to prevent spoofing.

See: [stripe-webhooks-deep-dive.md](stripe-webhooks-deep-dive.md)

---

## 10. Payment Methods

Payment Methods represent customer payment credentials (cards, ACH, bank transfers). Use SetupIntents to save methods for future off-session billing.

**Key Attributes:** `type` (55+ types; B2B-relevant: `card`, `us_bank_account`, `sepa_debit`, `bacs_debit`), `billing_details`, `customer`

**Endpoints:** Create, Update, Retrieve, List, Attach, Detach

**B2B Pattern:** Use SetupIntents with `usage=off_session` to save cards for recurring invoices. Use `us_bank_account` for ACH-based enterprise billing with lower fees.

See: [stripe-payment-methods-deep-dive.md](stripe-payment-methods-deep-dive.md)

---

## 11. Payment Intents

PaymentIntents orchestrate the payment flow — creation, confirmation, 3D Secure authentication, capture, and cancellation.

**Key Attributes:** `status` (7 states: `requires_payment_method` → `requires_confirmation` → `requires_action` → `processing` → `requires_capture` → `succeeded` / `canceled`), `amount`, `currency`, `payment_method`

**Endpoints:** Create, Update, Retrieve, List, Confirm, Capture, Cancel, Search

**B2B Pattern:** Use `capture_method=manual` for authorization holds on large contracts. Use `setup_future_usage=off_session` to save the method for recurring charges. Use `off_session=true` for server-initiated billing.

See: [stripe-payment-intents-deep-dive.md](stripe-payment-intents-deep-dive.md)

---

## 12. Charges & Refunds

### Charges

A Charge represents a completed payment attempt. In modern Stripe, Charges are created automatically by PaymentIntents — direct Charge creation via `POST /v1/charges` is **deprecated**.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Prefixed `ch_` |
| `amount` | integer | Amount in cents; min $0.50 USD |
| `currency` | enum | Three-letter ISO code |
| `status` | enum | `succeeded`, `pending`, `failed` |
| `captured` | boolean | Whether funds have been captured |
| `amount_captured` | integer | Amount actually captured |
| `amount_refunded` | integer | Amount refunded |
| `disputed` | boolean | Whether charge has been disputed |
| `customer` | string | Associated customer ID |
| `payment_intent` | string | Associated PaymentIntent |
| `payment_method_details` | object | Card brand, last4, funding type |
| `outcome` | object | `risk_level`, `risk_score` (0-99), `network_status` |
| `statement_descriptor` | string | Text on customer statement (22-char max) |
| `metadata` | object | Key-value pairs |

**Endpoints:**

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/charges` | Create (DEPRECATED — use PaymentIntents) |
| `POST` | `/v1/charges/:id` | Update (customer, description, metadata) |
| `GET` | `/v1/charges/:id` | Retrieve |
| `GET` | `/v1/charges` | List (filter by customer, payment_intent) |
| `POST` | `/v1/charges/:id/capture` | Capture uncaptured charge |
| `GET` | `/v1/charges/search` | Search via Stripe Query Language |

**Capture behavior:** Uncaptured charges expire after 7 days and are marked as refunded. `amount` on capture must be ≤ original.

### Refunds

Refunds return funds to the original payment method. Partial refunds are supported.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Prefixed `re_` |
| `amount` | integer | Refund amount in cents |
| `charge` | string | The charge being refunded |
| `payment_intent` | string | The PaymentIntent being refunded |
| `reason` | enum | `duplicate`, `fraudulent`, `requested_by_customer`, `expired_uncaptured_charge` |
| `status` | enum | `pending`, `requires_action`, `succeeded`, `failed`, `canceled` |
| `metadata` | object | Key-value pairs |

**Endpoints:**

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/refunds` | Create (specify `charge` OR `payment_intent`) |
| `POST` | `/v1/refunds/:id` | Update (metadata only) |
| `GET` | `/v1/refunds/:id` | Retrieve |
| `GET` | `/v1/refunds` | List |
| `POST` | `/v1/refunds/:id/cancel` | Cancel (only for `requires_action` status) |

**Key behaviors:**
- Multiple partial refunds allowed until fully refunded
- `reason=fraudulent` adds card/email to Radar block lists
- B2B relevance: Partial refunds are common for mid-cycle contract adjustments

---

## 13. Coupons, Promotion Codes & Discounts

### Coupons

Coupons define percent-off or amount-off discounts applied to subscriptions, invoices, checkout sessions, and quotes. They do NOT work with one-off charges or PaymentIntents.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Custom-settable at creation |
| `amount_off` | integer | Fixed discount in cents (requires `currency`) |
| `percent_off` | float | Percentage discount (0–100) |
| `duration` | enum | `forever`, `once`, `repeating` |
| `duration_in_months` | integer | Used with `repeating` |
| `name` | string | Customer-facing (max 40 chars) |
| `max_redemptions` | integer | Total cap |
| `redeem_by` | timestamp | Expiration date |
| `valid` | boolean | Whether still usable |

**Endpoints:** Create, Update (name/metadata only — amount/duration immutable), Retrieve, List, Delete.

```bash
# Create a 20% discount for 6 months (B2B onboarding discount)
curl https://api.stripe.com/v1/coupons \
  -u "sk_test_key:" \
  -d "percent_off=20" \
  -d "duration=repeating" \
  -d "duration_in_months=6" \
  -d "name=Enterprise Onboarding"
```

### Promotion Codes

Customer-redeemable codes wrapping a coupon. Multiple codes can reference the same coupon.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Prefixed `promo_` |
| `code` | string | Customer-facing code (max 500 chars) |
| `active` | boolean | Whether active |
| `restrictions` | object | `first_time_transaction`, `minimum_amount`, `minimum_amount_currency` |
| `customer` | string | Restrict to specific customer |
| `max_redemptions` | integer | Redemption cap |

**Endpoints:** Create, Update (active, metadata, restrictions), Retrieve, List.

**B2B relevance:** Use promotion codes for partner channel discounts and customer-specific negotiated rates. The `minimum_amount` restriction maps well to enterprise deal thresholds.

---

## 14. Usage Records & Metered Billing

Metered billing is critical for per-lead, per-action, or consumption-based B2B pricing. Stripe offers two systems:

### Billing Meters (Current)

The modern usage-based billing system. A Meter defines what to track, Meter Events record individual usage, and Meter Event Summaries aggregate for billing.

| Resource | Endpoints | Description |
|---|---|---|
| Meters | Create, Retrieve, Update, List, Deactivate, Reactivate | Define usage metric (e.g., "leads_delivered") |
| Meter Events | Create | Record individual usage occurrence |
| Meter Event Summaries | List | Aggregated usage per billing period |

```bash
# Record a lead delivery event
curl https://api.stripe.com/v1/billing/meter_events \
  -u "sk_test_key:" \
  -d "event_name=leads_delivered" \
  -d "payload[stripe_customer_id]=cus_xxx" \
  -d "payload[value]=1"
```

### Usage Records (Legacy)

The older mechanism for subscription items with `usage_type=metered`. Reports usage quantities within a billing period.

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/subscription_items/:id/usage_records` | Create a usage record |
| `GET` | `/v1/subscription_items/:id/usage_record_summaries` | List usage summaries |

> **Gap:** Both Billing Meters and Usage Records source files returned 404 errors in the scraped documentation. The parameter tables above are reconstructed from contextual references in other endpoints. The detailed Meter Event payload schema, aggregation modes, and deduplication behavior are not available in the source material.

**B2B Pattern:** For per-lead pricing, create a Price with `recurring.usage_type=metered` and report each lead delivery as a meter event. The subscription invoice at period end automatically calculates the total.

---

## 15. Tax Rates & Tax IDs

### Tax Rates

Tax rates applied to invoices, subscriptions, and checkout sessions.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Prefixed `txr_` |
| `display_name` | string | Shown on invoices (max 50 chars) |
| `percentage` | float | Rate (0–100) |
| `inclusive` | boolean | Whether tax is included in the price |
| `country` | string | ISO 3166-1 alpha-2 |
| `state` | string | ISO 3166-2 subdivision code |
| `jurisdiction` | string | Tax reporting label (max 50 chars) |
| `active` | boolean | Inactive rates persist on existing subscriptions |
| `tax_type` | enum | e.g., VAT, sales_tax |

**Endpoints:** Create (requires `display_name`, `inclusive`, `percentage`), Update, Retrieve, List.

### Tax IDs

Store tax identification numbers (VAT, EIN, GST, etc.) on customers. Displayed on invoices and credit notes.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Prefixed `txi_` |
| `type` | enum | 110+ types (`eu_vat`, `us_ein`, `gb_vat`, `au_abn`, etc.) |
| `value` | string | The tax ID number |
| `verification` | object | `status` (`pending` / `verified` / `unverified`), `verified_name`, `verified_address` |
| `owner` | object | `type` (`self` / `customer`) |

**Endpoints:** Create, Retrieve, List, Delete — both on `/v1/customers/:id/tax_ids` and `/v1/tax_ids`.

**B2B relevance:** EU B2B transactions require VAT IDs for reverse charge. US enterprises need EIN display. Verification is automatic for `eu_vat` type. Multiple tax IDs per customer supported.

---

## 16. Connect (Platforms & Marketplaces)

Stripe Connect enables platforms to process payments on behalf of connected businesses. Relevant for agencies managing billing for multiple clients or marketplaces facilitating service transactions.

### Account Types

| Type | Dashboard | Onboarding | Branding | Best For |
|---|---|---|---|---|
| Standard | Full Stripe dashboard | Stripe-hosted | Stripe | Independent businesses with their own Stripe |
| Express | Limited dashboard | Stripe-hosted | Customizable | Service providers managed by your platform |
| Custom | None | You build it | Yours | White-label platforms |

### Key Resources

**Accounts** — Represent connected businesses.

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/accounts` | Create connected account |
| `POST` | `/v1/accounts/:id` | Update |
| `GET` | `/v1/accounts/:id` | Retrieve |
| `GET` | `/v1/accounts` | List |
| `DELETE` | `/v1/accounts/:id` | Delete |

Key attributes: `charges_enabled`, `payouts_enabled`, `requirements` (fields needed for activation), `capabilities`.

**Transfers** — Move funds from your platform to a connected account.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | Yes | Amount in cents |
| `currency` | enum | Yes | ISO currency code |
| `destination` | string | Yes | Connected account ID |

**Application Fees** — Automatically collected when charges are made through your platform.

Key attributes: `amount`, `account`, `charge`, `refunds`.

**B2B relevance:** For agency platforms that bill end-clients and pay out to service providers, Connect manages the funds flow. Use `application_fee_amount` on PaymentIntents to collect platform revenue.

See: [stripe-connect-overview.md](stripe-connect-overview.md)

---

## 17. Disputes

Disputes (chargebacks) occur when a customer questions a charge with their card issuer.

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Prefixed `du_` |
| `amount` | integer | Disputed amount (may differ from charge) |
| `charge` | string | Disputed charge |
| `reason` | enum | `fraudulent`, `duplicate`, `subscription_canceled`, `product_not_received`, `product_unacceptable`, `general`, etc. |
| `status` | enum | `needs_response`, `under_review`, `won`, `lost`, `prevented`, `warning_needs_response`, `warning_under_review`, `warning_closed` |
| `evidence` | object | 27 evidence fields (billing_address, customer_communication, service_documentation, etc.) |
| `evidence_details` | object | `due_by` (deadline), `has_evidence`, `past_due`, `submission_count` |

**Endpoints:**

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/disputes/:id` | Update (submit evidence; `submit=false` stages without submitting) |
| `GET` | `/v1/disputes/:id` | Retrieve |
| `GET` | `/v1/disputes` | List (filter by charge, payment_intent) |
| `POST` | `/v1/disputes/:id/close` | Close/accept loss (IRREVERSIBLE) |

**B2B relevance:** Lower frequency than B2C but higher dollar amounts. For service businesses, the `service_documentation` and `customer_communication` evidence fields are most important. The `submit` staging mechanism allows building evidence incrementally before final submission.

---

## 18. Payment Links

Payment Links are shareable URLs that create a Stripe-hosted payment page without building a checkout flow.

**When to use:** Quick invoice links for one-off payments from enterprise clients, collecting setup fees via email/Slack, or simple payment collection without frontend integration.

**Key features:** Supports one-time payments and subscriptions, customizable branding, quantity adjustable, reusable across multiple customers.

**Endpoints:** Create, Update, Retrieve, List.

**B2B relevance:** Moderate — useful for collecting one-off payments or onboarding clients who aren't ready for a full integration. Less control than Checkout Sessions but faster to set up.

> **Gap:** Payment Links source files returned 404 in the scraped documentation. Detailed parameter tables are not available.

---

## 19. Quotes

Quotes model pricing proposals that can be sent to customers before creating subscriptions or invoices. They support a lifecycle: `draft` → `open` (finalized) → `accepted` / `canceled`.

**Key features:**
- Line items with pricing details
- Downloadable as PDF
- Automatic conversion to invoice/subscription on acceptance
- Supports `collection_method`, `automatic_tax`, `subscription_data`
- Expiration dates

**Endpoints:** Create, Update, Retrieve, List, Accept, Cancel, Finalize, List Line Items, List Upfront Line Items, PDF.

**B2B relevance:** High — directly maps to enterprise sales workflows. Use for formal pricing proposals, contract negotiations, and SOW-based billing. Quote → accepted → subscription is the standard enterprise deal flow.

---

## 20. Terminal, Issuing & Treasury

### Terminal (In-Person Payments)

Terminal provides SDKs and hardware for accepting in-person payments via physical card readers.

**Key resources:** Readers, Locations, Connection Tokens, Configurations, Hardware Orders.

**B2B relevance:** Low — primarily retail/in-person. Relevant only if your service business has a physical presence (e.g., insurance office with walk-in clients).

### Issuing (Card Creation)

Stripe Issuing lets you create, manage, and distribute virtual and physical payment cards programmatically.

**Key resources:** Cards, Cardholders, Authorizations, Transactions, Disputes.

**B2B relevance:** Moderate — relevant for expense management, vendor payments, or platforms issuing cards to service providers.

### Treasury (Banking-as-a-Service)

Treasury provides financial accounts that hold funds, enabling money movement (inbound/outbound transfers).

**Key resources:** Financial Accounts, Inbound/Outbound Transfers, Received Credits/Debits, Transactions.

**B2B relevance:** Moderate — relevant for platforms holding/managing funds on behalf of business customers. Enables embedded banking experiences.

> **Gap:** Terminal, Issuing, and Treasury source files returned 404 in the scraped documentation. Only contextual information is available.

---

## 21. Identity, Radar, Sigma & Reporting

### Identity (Verification)

Identity provides identity verification for users through document checks and ID number verification.

**Key resources:** Verification Sessions (`requires_input` → `processing` → `verified` / `canceled`), Verification Reports.

**B2B relevance:** Low-to-moderate — useful for KYC on business owners or high-value B2B onboarding.

### Radar (Fraud Detection)

Radar provides machine learning-powered fraud detection and risk scoring for payments.

**Key resources:** Reviews (manual review of flagged payments), Value Lists (custom block/allow lists), Early Fraud Warnings.

**B2B relevance:** Low — B2B transactions have lower fraud rates, but Radar's `outcome.risk_score` (0-99) on charges is useful for monitoring.

### Sigma (SQL Queries)

Sigma lets you run SQL queries against your Stripe data on a recurring schedule.

**Key resources:** Scheduled Queries (create, list, retrieve).

**B2B relevance:** Moderate — useful for custom billing reports, revenue analytics, and financial reconciliation.

### Reporting

Reporting generates financial reports (balance changes, payouts, etc.) as downloadable files.

**Key resources:** Report Runs, Report Types.

**B2B relevance:** Moderate — useful for automated financial reporting and audit trails.

> **Gap:** Radar, Sigma, and Reporting source files returned 404 in the scraped documentation. Identity Verification Sessions object was available with full attribute details.

---

## 22. Climate & Financial Connections

### Climate

Stripe Climate enables purchasing carbon removal credits through Stripe.

**Key resources:** Orders, Products, Suppliers.

**B2B relevance:** Very low — niche sustainability feature. Not relevant to core billing.

### Financial Connections

Financial Connections provides access to linked bank accounts for ACH payments, balance checks, and account verification.

**Key resources:** Accounts, Account Owners, Sessions, Transactions.

**B2B relevance:** Moderate — relevant for ACH-based B2B payment collection and bank account verification during enterprise client onboarding.

> **Gap:** Climate and Financial Connections source files returned 404 in the scraped documentation.

---

## 23. B2B Billing Integration Patterns

### Pattern 1: Agency Retainer Model

Monthly fixed-fee billing for service clients.

```
Product: "Marketing Retainer"
  └─ Price: $5,000/month (recurring, per_unit)
      └─ Subscription: Customer "Acme Corp"
          ├─ collection_method: send_invoice
          ├─ days_until_due: 30
          └─ metadata: { client_id: "acme", vertical: "insurance" }
```

### Pattern 2: Per-Lead / Per-Action Pricing

Usage-based billing where each lead or action is tracked and billed.

```
Product: "Lead Delivery"
  └─ Price: $25/lead (recurring, metered)
      └─ Subscription Item (metered)
          └─ Meter Events: reported per lead via API
              └─ Invoice: auto-generated at period end with usage total
```

### Pattern 3: Setup Fee + Ongoing Billing

One-time onboarding charge plus recurring subscription.

```
# Option A: Invoice item on first subscription invoice
Subscription.create(
  customer: "cus_xxx",
  items: [{ price: "price_monthly_retainer" }],
  add_invoice_items: [{ price: "price_setup_fee" }]  # one-time
)

# Option B: Separate one-off invoice
Invoice.create(customer: "cus_xxx")
InvoiceItem.create(customer: "cus_xxx", amount: 250000, description: "Setup Fee")
Invoice.finalize(invoice_id)
```

### Pattern 4: Tiered Usage Pricing

Volume-based pricing where unit cost decreases at higher volumes.

```
Price (billing_scheme: tiered, tiers_mode: graduated):
  Tier 1: 1-100 leads  → $30/lead
  Tier 2: 101-500 leads → $20/lead
  Tier 3: 501+ leads    → $12/lead
```

`graduated` = each tier priced independently (first 100 at $30, next 400 at $20, etc.)
`volume` = all units priced at the tier reached (501 leads = all at $12)

### Pattern 5: Client Self-Service Portal

Let clients manage their own subscriptions, payment methods, and invoices.

```
# 1. Configure portal features
PortalConfiguration.create(
  features: {
    subscription_cancel: { enabled: true, mode: "at_period_end",
      cancellation_reason: { enabled: true, options: ["too_expensive", "missing_features", "switched_service", "unused", "other"] }
    },
    subscription_update: { enabled: true, default_allowed_updates: ["price", "quantity"] },
    payment_method_update: { enabled: true },
    invoice_history: { enabled: true }
  }
)

# 2. Generate session URL per client request
session = PortalSession.create(customer: "cus_xxx", return_url: "https://app.example.com/billing")
redirect_to(session.url)
```

### Pattern 6: Multi-Tenant Metadata Strategy

Use metadata consistently across all objects for tenant tracking and reporting.

| Object | Recommended Metadata Keys |
|---|---|
| Customer | `tenant_id`, `client_id`, `company_name`, `vertical`, `account_manager` |
| Subscription | `tenant_id`, `plan_tier`, `contract_start`, `contract_end` |
| Invoice | `tenant_id`, `billing_period`, `campaign_id` |
| PaymentIntent | `tenant_id`, `invoice_type` |

### Pattern 7: Net-30 / Net-60 Enterprise Invoicing

```
# Create subscription with send_invoice collection
Subscription.create(
  customer: "cus_enterprise",
  items: [{ price: "price_monthly" }],
  collection_method: "send_invoice",
  days_until_due: 30  # or 60 for net-60
)
```

The customer receives an email with a link to pay. Invoice status progresses: `draft` → `open` → `paid` (or `past_due` if unpaid by due date).

---

## 24. Gaps & Missing Documentation

> **Gap:** Billing Meters (meters, meter events, meter event summaries) and Usage Records source files all returned 404. These are critical for usage-based billing and the detailed parameter schemas are not available in the scraped source material.

> **Gap:** Payment Links source files returned 404. No detailed parameter tables available.

> **Gap:** Terminal, Issuing, Treasury, Radar Reviews, Sigma Scheduled Queries, Climate Orders, Financial Connections Accounts, and Reporting Report Runs source files returned 404 or were empty. Only contextual information is available for Tier 3 sections.

> **Gap:** Invoice Line Item object file returned 404. Line item structure is reconstructed from the Add Lines endpoint response.

> **Gap:** Upcoming Invoice endpoint (`GET /v1/invoices/upcoming`) returned 404 — appears to be API-version-gated. The Create Preview endpoint (`POST /v1/invoices/create_preview`) is available as an alternative.

> **Gap:** Webhook signature verification details (algorithm, timestamp tolerance, replay protection) are not present in the scraped endpoint documentation. The `secret` field is only returned at webhook endpoint creation. Verification implementation details would need to come from Stripe's integration guides rather than API reference docs.

> **Gap:** Stripe's automatic tax calculation (`automatic_tax`) is referenced across Subscriptions, Invoices, and Checkout Sessions, but the detailed configuration (Stripe Tax setup, tax registration requirements, supported jurisdictions) is not covered in the API reference docs.

> **Gap:** Error codes, rate limiting details, and retry strategies are not present in the scraped documentation. These are typically in Stripe's separate error handling guides.

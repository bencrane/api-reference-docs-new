# Stripe Subscriptions API Reference

**Canonical reference for B2B SaaS billing — subscription lifecycle, creation, updates, cancellation, and advanced patterns.**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

---

## Table of Contents

1. [The Subscription Object](#1-the-subscription-object)
2. [Status Lifecycle](#2-status-lifecycle)
3. [Create a Subscription](#3-create-a-subscription)
4. [Update a Subscription](#4-update-a-subscription)
5. [Retrieve a Subscription](#5-retrieve-a-subscription)
6. [List Subscriptions](#6-list-subscriptions)
7. [Cancel a Subscription](#7-cancel-a-subscription)
8. [Resume a Subscription](#8-resume-a-subscription)
9. [Search Subscriptions](#9-search-subscriptions)
10. [Subscription Items](#10-subscription-items)
11. [Subscription Schedules](#11-subscription-schedules)
12. [B2B Billing Patterns](#12-b2b-billing-patterns)

---

## 1. The Subscription Object

The Subscription object represents a recurring billing arrangement between a customer and your business. It manages the full lifecycle from creation through cancellation, including trials, pauses, and payment retries.

### Core Attributes

| Attribute | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the subscription (e.g., `sub_1MowQV...`). |
| `status` | enum | Current status. One of: `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, `paused`. |
| `customer` | string (expandable) | ID of the customer who owns this subscription. |
| `items` | object | List of subscription items, each containing a price and quantity. |
| `default_payment_method` | string, nullable (expandable) | The default payment method for the subscription. Overrides the customer's default. |
| `description` | string, nullable | Free-form description of the subscription. Max 500 characters. Visible on invoices. |
| `metadata` | object | Set of key-value pairs for storing additional information. |
| `latest_invoice` | string, nullable (expandable) | The most recent invoice this subscription has generated. |

### Billing Configuration

| Attribute | Type | Description |
|---|---|---|
| `automatic_tax` | object | Automatic tax settings for this subscription. |
| `currency` | enum | Three-letter ISO currency code (e.g., `usd`). |
| `billing_cycle_anchor` | timestamp | The reference point that aligns future billing cycle dates. |
| `billing_cycle_anchor_config` | object, nullable | Configuration for the billing cycle anchor. |
| `collection_method` | enum | Either `charge_automatically` (default) or `send_invoice`. |
| `days_until_due` | integer, nullable | Number of days a customer has to pay invoices. Only applies when `collection_method` is `send_invoice`. |

### Cancellation

| Attribute | Type | Description |
|---|---|---|
| `cancel_at` | timestamp, nullable | A date in the future at which the subscription will automatically be canceled. |
| `cancel_at_period_end` | boolean | If `true`, the subscription will be canceled at the end of the current period. |
| `canceled_at` | timestamp, nullable | If the subscription has been canceled, the date of that cancellation. |
| `cancellation_details` | object, nullable | Details about why the subscription was canceled. Contains `comment` (string), `feedback` (enum), and `reason` (enum). |

### Period and Trial

| Attribute | Type | Description |
|---|---|---|
| `current_period_start` | timestamp | Start of the current billing period (accessed via items). |
| `current_period_end` | timestamp | End of the current billing period (accessed via items). |
| `start_date` | timestamp | Date when the subscription was first created. |
| `ended_at` | timestamp, nullable | If the subscription has ended, the date it ended. |
| `trial_start` | timestamp, nullable | Start date of the trial period. |
| `trial_end` | timestamp, nullable | End date of the trial period. |
| `trial_settings` | object, nullable | Settings related to subscription trials, including end-of-trial behavior. |

### Payment and Invoicing

| Attribute | Type | Description |
|---|---|---|
| `default_source` | string, nullable (expandable) | Default source to charge for invoices. Deprecated in favor of `default_payment_method`. |
| `default_tax_rates` | array, nullable | Tax rates applied to every invoice created by this subscription. |
| `discounts` | array (expandable) | Discounts applied to the subscription. |
| `invoice_settings` | object | Invoice-level settings for this subscription (e.g., custom fields, rendering options). |
| `pause_collection` | object, nullable | If set, indicates that payment collection is paused. Contains `behavior` and `resumes_at`. |
| `payment_settings` | object, nullable | Payment-related settings for the subscription, including retry rules. |
| `pending_setup_intent` | string, nullable (expandable) | A SetupIntent being used to collect a payment method for the subscription. |
| `pending_update` | object, nullable | If an update has been applied that requires payment and is awaiting confirmation. |
| `proration_behavior` | string | Controls how prorations are handled. |
| `schedule` | string, nullable (expandable) | The schedule attached to the subscription, if any. |

### Connect Attributes

| Attribute | Type | Description |
|---|---|---|
| `application_fee_percent` | float, nullable | Percentage of the subscription invoice total to transfer to the application owner's account. Connect only. |
| `on_behalf_of` | string, nullable | The account on whose behalf charges are made. Connect only. |
| `transfer_data` | object, nullable | Transfer configuration for the subscription. Connect only. |

---

## 2. Status Lifecycle

### Status Transition Diagram

```
                          ┌─────────────────────────────────┐
                          │          CREATION                │
                          └────────────┬────────────────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                    ┌─────────│   incomplete     │──────────┐
                    │         └─────────────────┘           │
                    │ payment succeeds              23 hrs, │
                    │                            no payment │
                    ▼                                       ▼
          ┌──────────────┐                    ┌──────────────────────┐
     ┌────│    active     │                   │ incomplete_expired   │
     │    └──────────────┘                    │     (TERMINAL)       │
     │           ▲                            └──────────────────────┘
     │           │
     │           │ trial ends (payment OK)
     │           │
     │    ┌──────────────┐
     │    │   trialing    │────────────────────┐
     │    └──────────────┘                     │
     │                              trial ends │
     │                         (no payment     │
     │                           method)       │
     │                                         ▼
     │                               ┌──────────────┐
     │                               │    paused     │
     │                               └──────┬───────┘
     │                                      │ resume
     │                                      │
     │           ┌──────────────────────────┘
     │           │
     │           ▼
     │    ┌──────────────┐
     │    │    active     │
     │    └──────────────┘
     │
     │ payment fails
     │
     ▼
┌──────────────┐
│   past_due    │
└──────┬───────┘
       │
       ├─── retry exhaustion ──┬──▶ ┌──────────────┐
       │                       │    │   canceled    │
       │                       │    │  (TERMINAL)   │
       │                       │    └──────────────┘
       │                       │
       │                       └──▶ ┌──────────────┐
       │                            │    unpaid     │
       │                            └──────────────┘
       │
       │
  ┌────┴─────────────────────────────────────┐
  │ active ──(cancel request)──▶ canceled    │
  │                              (TERMINAL)  │
  └──────────────────────────────────────────┘
```

### Status Definitions

**`incomplete`** — The initial payment attempt failed when using `charge_automatically` as the collection method. The subscription enters this state when the first invoice cannot be paid. During this 23-hour window, only `metadata` and `default_source` can be updated. If the payment is not completed within 23 hours, the subscription transitions to `incomplete_expired`.

**`incomplete_expired`** — Terminal state. The subscription was in `incomplete` status for 23 hours without a successful payment. No further actions can be taken on this subscription.

**`trialing`** — The subscription is in an active trial period. No invoices are generated during the trial. When the trial ends, the subscription moves to `active` if payment succeeds, or `paused` if no payment method is on file.

**`active`** — The normal operating state. Invoices are generated and collected according to the billing cycle. The subscription remains active as long as payments succeed.

**`past_due`** — A payment attempt has failed, but Stripe has not exhausted all retry attempts. Behavior depends on the `collection_method`: with `charge_automatically`, Stripe retries according to your retry settings; with `send_invoice`, the invoice remains open for the customer to pay.

**`canceled`** — Terminal state. The subscription has been explicitly canceled or transitioned here after retry exhaustion (depending on your settings). No further updates to the subscription or its metadata are possible.

**`unpaid`** — The subscription has been configured so that after retry exhaustion, instead of canceling, it moves to `unpaid`. No subsequent invoices are attempted and existing unpaid invoices are auto-closed. The subscription can be reactivated by paying the outstanding invoice.

**`paused`** — The subscription only enters this state when a trial ends and no valid payment method is attached. While paused, no invoices are generated. Use the Resume endpoint to move back to `active`.

> **Gap:** The Stripe API does not currently support a general-purpose "pause" action for active subscriptions. The `paused` status is exclusively triggered by trial-end scenarios. For general pause/resume behavior, use `pause_collection` on the subscription object instead.

---

## 3. Create a Subscription

```
POST /v1/subscriptions
```

### Required Parameters

| Parameter | Type | Description |
|---|---|---|
| `items` | array | **Required.** Up to 20 subscription items, each specifying a `price` and optional `quantity`. |

### Key Optional Parameters

| Parameter | Type | Description |
|---|---|---|
| `customer` | string | The ID of the customer to subscribe. |
| `automatic_tax` | object | Automatic tax configuration. |
| `currency` | enum | Three-letter ISO currency code. Must match the price currency. |
| `default_payment_method` | string | Payment method ID to use as default for this subscription. |
| `description` | string | Free-form text (max 500 chars). |
| `metadata` | object | Key-value pairs for your use. |
| `payment_behavior` | enum | One of: `allow_incomplete` (default), `default_incomplete`, `error_if_incomplete`, `pending_if_incomplete` (updates only). |

### Additional Parameters

| Parameter | Type | Description |
|---|---|---|
| `add_invoice_items` | array | One-time invoice items to add on the first invoice. |
| `application_fee_percent` | float | Connect only. Percentage of invoice total to transfer. |
| `backdate_start_date` | timestamp | Backdate the subscription start. |
| `billing_cycle_anchor` | timestamp | Future timestamp to anchor the billing cycle. |
| `billing_mode` | string | Billing mode configuration. |
| `billing_thresholds` | object | Usage threshold configuration. |
| `cancel_at` | timestamp | Schedule future cancellation. |
| `cancel_at_period_end` | boolean | Cancel at end of current period. |
| `collection_method` | enum | `charge_automatically` or `send_invoice`. |
| `days_until_due` | integer | Days until invoice is due. Required if `collection_method` is `send_invoice`. |
| `default_source` | string | Deprecated. Use `default_payment_method`. |
| `default_tax_rates` | array | Tax rates to apply. |
| `discounts` | array | Discounts to apply to the subscription. |
| `invoice_settings` | object | Invoice configuration. |
| `off_session` | boolean | Indicates the customer is not in your checkout flow. |
| `on_behalf_of` | string | Connect only. The account to charge on behalf of. |
| `payment_settings` | object | Payment and retry configuration. |
| `pending_invoice_item_interval` | object | Interval for pending invoice items to be invoiced. |
| `proration_behavior` | enum | `always_invoice`, `create_prorations` (default), `none`. |
| `transfer_data` | object | Connect only. Transfer configuration. |
| `trial_end` | timestamp | Timestamp when the trial ends. |
| `trial_from_plan` | boolean | Use the plan's `trial_period_days` value. |
| `trial_period_days` | integer | Number of trial days. |
| `trial_settings` | object | Trial configuration including end behavior. |

### Example: Create a subscription with monthly pricing

```bash
curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_...:" \
  -d customer=cus_ABC123 \
  -d "items[0][price]"=price_monthly_pro \
  -d "items[0][quantity]"=5 \
  -d default_payment_method=pm_card_visa \
  -d "metadata[contract_id]"=contract_2024_001
```

### Example: Create a subscription with a trial period

```bash
curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_...:" \
  -d customer=cus_ABC123 \
  -d "items[0][price]"=price_enterprise_annual \
  -d trial_period_days=30 \
  -d "trial_settings[end_behavior][missing_payment_method]"=pause
```

### Limits

- Maximum **500 active or scheduled subscriptions** per customer.
- Maximum **20 items** per subscription.

> **Gap:** The `payment_behavior` value `pending_if_incomplete` is only available on subscription updates, not on creation. If you need pending behavior at creation time, use `allow_incomplete` and handle the `incomplete` status via webhooks.

---

## 4. Update a Subscription

```
POST /v1/subscriptions/:id
```

### Key Parameters

| Parameter | Type | Description |
|---|---|---|
| `items` | array | Update, add, or remove subscription items. |
| `default_payment_method` | string | Change the default payment method. |
| `proration_behavior` | enum | `always_invoice`, `create_prorations` (default), `none`. |
| `payment_behavior` | enum | Same as create, plus `pending_if_incomplete`. |

### Proration Behavior

- **`create_prorations`** (default): Creates proration line items on the next invoice. No immediate charge.
- **`always_invoice`**: Creates proration line items AND immediately generates and attempts to collect an invoice.
- **`none`**: No prorations are created. The new price takes effect on the next billing cycle.

### Price Change Behavior

When switching prices on a subscription item:

- The **billing date does not change** unless:
  - The billing interval changes (e.g., monthly to annual)
  - The subscription moves from free to paid
  - A trial starts or ends
- Quantity and price changes are prorated by default
- When changing the `price` on an item, the `quantity` resets to **1** unless explicitly provided

### Example: Upgrade a subscription plan

```bash
curl https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d "items[0][id]"=si_existing_item \
  -d "items[0][price]"=price_enterprise_annual \
  -d proration_behavior=always_invoice
```

> **Gap:** Rapidly updating a subscription's quantity (many times per hour) may trigger rate limiting. For high-frequency metered usage, consider usage-based billing with `usage_records` on metered prices instead of quantity updates.

---

## 5. Retrieve a Subscription

```
GET /v1/subscriptions/:id
```

Returns the full Subscription object. Use `expand[]` to include nested objects:

```bash
curl https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d "expand[]"=latest_invoice \
  -d "expand[]"=customer \
  -d "expand[]"=default_payment_method
```

---

## 6. List Subscriptions

```
GET /v1/subscriptions
```

### Filter Parameters

| Parameter | Type | Description |
|---|---|---|
| `collection_method` | enum | Filter by collection method. |
| `created` | timestamp / range | Filter by creation date. Supports `gt`, `gte`, `lt`, `lte`. |
| `current_period_end` | timestamp / range | Filter by current period end date. |
| `current_period_start` | timestamp / range | Filter by current period start date. |
| `customer` | string | Filter by customer ID. |
| `price` | string | Filter by price ID. |
| `status` | enum | Filter by status. |

### Example: List active subscriptions for a customer

```bash
curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_...:" \
  -d customer=cus_ABC123 \
  -d status=active \
  -d limit=10
```

---

## 7. Cancel a Subscription

```
DELETE /v1/subscriptions/:id
```

Cancels a subscription immediately. The customer will not be charged again, and the subscription status transitions to `canceled`.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `cancellation_details` | object | Optional. Includes `comment` (string) and `feedback` (enum). |
| `invoice_now` | boolean | If `true`, generates a final invoice for any un-invoiced metered usage and prorations. |
| `prorate` | boolean | If `true`, generates a prorated credit for unused time. |

### Example: Cancel with a final invoice

```bash
curl -X DELETE https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d invoice_now=true \
  -d prorate=true \
  -d "cancellation_details[comment]"="Customer requested cancellation" \
  -d "cancellation_details[feedback]"=too_expensive
```

### Post-Cancellation Behavior

- The subscription cannot be updated after cancellation (including metadata).
- Any **pending invoice items** attached to the customer are still charged on the next invoice unless explicitly deleted.
- Stripe stops automatic collection on all open invoices for the canceled subscription.

> **Gap:** For graceful end-of-period cancellation (common in B2B contracts), use `cancel_at_period_end=true` on an update call instead of the DELETE endpoint. The DELETE endpoint cancels immediately and is irreversible.

---

## 8. Resume a Subscription

```
POST /v1/subscriptions/:id/resume
```

Resumes a paused subscription.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `billing_cycle_anchor` | enum | `now` (resets the billing cycle) or `unchanged` (keeps the original anchor). |
| `proration_behavior` | enum | `always_invoice`, `create_prorations`, `none`. |

### Example: Resume with a reset billing cycle

```bash
curl -X POST https://api.stripe.com/v1/subscriptions/sub_ABC123/resume \
  -u "sk_test_...:" \
  -d billing_cycle_anchor=now \
  -d proration_behavior=none
```

---

## 9. Search Subscriptions

```
GET /v1/subscriptions/search
```

Search subscriptions using Stripe's query language. Supports searching by `status`, `metadata`, and other fields.

### Example: Search by metadata

```bash
curl https://api.stripe.com/v1/subscriptions/search \
  -u "sk_test_...:" \
  -d query="metadata['contract_id']:'contract_2024_001'"
```

> **Gap:** Search results may be up to 1 minute behind real-time. Do not rely on the Search endpoint for immediate post-creation lookups. Use Retrieve instead.

---

## 10. Subscription Items

Subscription items represent individual line items within a subscription, each tied to a specific price.

### Create a Subscription Item

```
POST /v1/subscription_items
```

Adds a new item to an existing subscription. Existing items are not modified.

| Parameter | Type | Description |
|---|---|---|
| `subscription` | string | **Required.** The subscription ID. |
| `price` | string | **Required.** The price ID. |
| `quantity` | integer | Optional. Defaults to 1. |

```bash
curl https://api.stripe.com/v1/subscription_items \
  -u "sk_test_...:" \
  -d subscription=sub_ABC123 \
  -d price=price_addon_storage \
  -d quantity=10
```

### Update a Subscription Item

```
POST /v1/subscription_items/:id
```

When changing the `price` on a subscription item, the `quantity` resets to **1** unless you explicitly provide a `quantity` value.

```bash
curl https://api.stripe.com/v1/subscription_items/si_ABC123 \
  -u "sk_test_...:" \
  -d price=price_addon_storage_v2 \
  -d quantity=10
```

### Delete a Subscription Item

```
DELETE /v1/subscription_items/:id
```

Removes an item from the subscription. This does **not** cancel the subscription itself.

### List Subscription Items

```
GET /v1/subscription_items
```

| Parameter | Type | Description |
|---|---|---|
| `subscription` | string | **Required.** The subscription to list items for. |

---

## 11. Subscription Schedules

Subscription schedules allow you to define multi-phase billing configurations that automatically transition between different prices, quantities, or settings over time.

### Key Concepts

- A schedule contains an array of **`phases`**, each with its own items, duration, and billing settings.
- The **`end_behavior`** property controls what happens after the last phase completes (`release`, `cancel`, or `none`).
- Each phase can have different prices, quantities, trial settings, and coupon configurations.
- Limit: up to **500 subscription schedules** per customer.

### Example: Two-phase schedule (trial then annual)

```bash
curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_...:" \
  -d customer=cus_ABC123 \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"=price_trial_monthly \
  -d "phases[0][iterations]"=3 \
  -d "phases[1][items][0][price]"=price_enterprise_annual \
  -d "phases[1][iterations]"=1
```

> **Gap:** Subscription schedules cannot be combined with certain subscription update operations. Once a schedule is attached, direct subscription updates may conflict with or be overridden by the schedule. Always manage billing changes through the schedule when one is active.

---

## 12. B2B Billing Patterns

### Net-30 Enterprise Billing

Send invoices with a 30-day payment window, common for enterprise contracts.

```bash
curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_...:" \
  -d customer=cus_enterprise_ABC \
  -d "items[0][price]"=price_enterprise_annual \
  -d collection_method=send_invoice \
  -d days_until_due=30
```

### Graceful Contract Endings

Cancel at the end of the current billing period instead of immediately, preserving service through the paid period.

```bash
curl https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d cancel_at_period_end=true
```

### Mid-Contract Plan Changes with Proration

Upgrade a customer mid-cycle with immediate invoicing of the prorated difference.

```bash
curl https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d "items[0][id]"=si_current_item \
  -d "items[0][price]"=price_higher_tier \
  -d proration_behavior=always_invoice
```

### Multi-Service Bundles

Add multiple items to a single subscription to represent bundled services.

```bash
curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_...:" \
  -d customer=cus_ABC123 \
  -d "items[0][price]"=price_platform_base \
  -d "items[0][quantity]"=1 \
  -d "items[1][price]"=price_api_calls \
  -d "items[1][quantity]"=1000 \
  -d "items[2][price]"=price_storage_gb \
  -d "items[2][quantity]"=50
```

### Trial-to-Paid Conversion for Enterprise Pilots

Offer a 30-day pilot that pauses if no payment method is provided at trial end, giving sales time to close the deal.

```bash
curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_...:" \
  -d customer=cus_enterprise_pilot \
  -d "items[0][price]"=price_enterprise_monthly \
  -d trial_period_days=30 \
  -d "trial_settings[end_behavior][missing_payment_method]"=pause
```

### Pause/Resume for Seasonal Businesses

Use `pause_collection` to temporarily stop invoicing without canceling the subscription.

```bash
# Pause collection
curl https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d "pause_collection[behavior]"=void \
  -d "pause_collection[resumes_at]"=1711929600

# Resume collection (remove pause)
curl https://api.stripe.com/v1/subscriptions/sub_ABC123 \
  -u "sk_test_...:" \
  -d "pause_collection"=""
```

> **Gap:** The `pause_collection` feature voids or marks invoices uncollectible during the pause, but the billing cycle still advances. Customers are not charged for the paused period, but the subscription's `current_period_end` continues to move forward. For true "freeze the clock" behavior, consider canceling and recreating the subscription.

---

*End of Stripe Subscriptions API Reference.*

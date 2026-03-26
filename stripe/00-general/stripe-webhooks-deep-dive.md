# Stripe Webhooks API Reference

**Canonical API reference for Stripe Webhooks — B2B SaaS billing focus**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

---

## Table of Contents

1. [Webhook Endpoint Object](#1-webhook-endpoint-object)
2. [Create Webhook Endpoint](#2-create-webhook-endpoint)
3. [Update Webhook Endpoint](#3-update-webhook-endpoint)
4. [Retrieve Webhook Endpoint](#4-retrieve-webhook-endpoint)
5. [List Webhook Endpoints](#5-list-webhook-endpoints)
6. [Delete Webhook Endpoint](#6-delete-webhook-endpoint)
7. [Signature Verification](#7-signature-verification)
8. [Retry Behavior](#8-retry-behavior)
9. [Critical B2B Billing Events](#9-critical-b2b-billing-events)
10. [B2B Patterns](#10-b2b-patterns)

---

## 1. Webhook Endpoint Object

| Parameter | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the webhook endpoint |
| `api_version` | string, nullable | API version events are rendered as. If null, uses your account default |
| `description` | string, nullable | Optional description of the endpoint |
| `enabled_events` | array of strings | Events the endpoint receives. `['*']` for all events, or specific event types |
| `metadata` | object | Set of key-value pairs for storing additional information |
| `secret` | string | Signing secret used to verify webhook signatures. **Only returned at creation** |
| `status` | string | `enabled` or `disabled` |
| `url` | string | The URL of the webhook endpoint |
| `application` | string, nullable | ID of the Connect application associated with this endpoint |
| `created` | integer | Timestamp of when the endpoint was created |
| `livemode` | boolean | Whether the object exists in live mode |

---

## 2. Create Webhook Endpoint

**`POST /v1/webhook_endpoints`**

### Parameters

| Parameter | Required | Type | Description |
|---|---|---|---|
| `enabled_events` | **Yes** | array of strings | 224+ event types, or `['*']` for all |
| `url` | **Yes** | string | The URL of the webhook endpoint |
| `api_version` | No | string | API version events are rendered as |
| `description` | No | string | Description of the endpoint |
| `metadata` | No | object | Key-value pairs |
| `connect` | No | boolean | Whether this endpoint receives events from connected accounts (Connect only) |

### Response

Returns the webhook endpoint object **with the `secret` field populated**. This is the only time the secret is returned in full.

```bash
curl https://api.stripe.com/v1/webhook_endpoints \
  -u sk_test_key: \
  -d url="https://example.com/webhooks/stripe" \
  -d "enabled_events[]"="invoice.payment_failed" \
  -d "enabled_events[]"="customer.subscription.updated" \
  -d "enabled_events[]"="customer.subscription.deleted"
```

---

## 3. Update Webhook Endpoint

**`POST /v1/webhook_endpoints/:id`**

| Parameter | Required | Type | Description |
|---|---|---|---|
| `description` | No | string | Updated description |
| `enabled_events` | No | array of strings | Replace the current list of enabled events |
| `metadata` | No | object | Update metadata |
| `url` | No | string | Update the endpoint URL |
| `disabled` | No | boolean | Set to `true` to disable the endpoint |

---

## 4. Retrieve Webhook Endpoint

**`GET /v1/webhook_endpoints/:id`**

Returns the webhook endpoint object. The `secret` field is **not** included in retrieve responses.

---

## 5. List Webhook Endpoints

**`GET /v1/webhook_endpoints`**

Standard list pagination parameters: `ending_before`, `starting_after`, `limit`.

---

## 6. Delete Webhook Endpoint

**`DELETE /v1/webhook_endpoints/:id`**

Returns a confirmation object with `id` and `deleted: true`.

---

## 7. Signature Verification

Every webhook delivery includes a `Stripe-Signature` header. Use the endpoint signing secret to verify that the payload was sent by Stripe and has not been tampered with. Stripe uses HMAC-SHA256 for signatures.

```bash
# Stripe-Signature header format:
# t=timestamp,v1=signature

# Verification steps:
# 1. Extract timestamp and signature from header
# 2. Construct signed payload: "{timestamp}.{raw_body}"
# 3. Compute HMAC-SHA256 with endpoint secret
# 4. Compare computed signature to v1 value
# 5. Check timestamp is within tolerance (default 5 minutes)
```

### Node.js Example

```ts
import Stripe from 'stripe';
const stripe = new Stripe('sk_test_key');

app.post('/webhook', express.raw({type: 'application/json'}), (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;
  try {
    event = stripe.webhooks.constructEvent(req.body, sig, 'whsec_...');
  } catch (err) {
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }
  // Handle event
  res.json({received: true});
});
```

**Important:** The request body must be the raw body (not parsed JSON). Using `express.json()` middleware before this route will break signature verification.

---

## 8. Retry Behavior

- Stripe retries failed webhooks (non-2xx responses) over **3 days** with exponential backoff.
- After all retries are exhausted, the endpoint may be automatically **disabled**.
- Events are delivered **at least once** — your handler may receive duplicates. Use idempotency (check the event `id` against previously processed events) to handle this.
- Your endpoint should return a `2xx` status code within **20 seconds** to avoid a timeout/retry.

---

## 9. Critical B2B Billing Events

### Subscription Lifecycle

| Event | Description |
|---|---|
| `customer.subscription.created` | New subscription created |
| `customer.subscription.updated` | Subscription changed (plan, quantity, status, etc.) |
| `customer.subscription.deleted` | Subscription canceled and period ended |
| `customer.subscription.paused` | Subscription paused |
| `customer.subscription.resumed` | Subscription resumed from pause |
| `customer.subscription.trial_will_end` | Trial ending in 3 days |
| `customer.subscription.pending_update_applied` | Pending update applied |
| `customer.subscription.pending_update_expired` | Pending update expired without applying |

### Invoice Lifecycle

| Event | Description |
|---|---|
| `invoice.created` | Draft invoice created |
| `invoice.finalized` | Invoice finalized, ready for payment |
| `invoice.paid` | Invoice successfully paid |
| `invoice.payment_failed` | Payment attempt on invoice failed |
| `invoice.payment_action_required` | Payment requires customer action (e.g., 3D Secure) |
| `invoice.sent` | Invoice emailed to customer |
| `invoice.voided` | Invoice voided |
| `invoice.marked_uncollectible` | Invoice marked as uncollectible |
| `invoice.upcoming` | Fires ~3 days before subscription renewal |

### Payment

| Event | Description |
|---|---|
| `payment_intent.succeeded` | Payment completed successfully |
| `payment_intent.payment_failed` | Payment attempt failed |
| `payment_intent.canceled` | PaymentIntent canceled |
| `payment_intent.requires_action` | Payment requires additional customer action |

### Customer

| Event | Description |
|---|---|
| `customer.created` | New customer created |
| `customer.updated` | Customer object updated |
| `customer.deleted` | Customer deleted |
| `customer.source.created` | Payment source added to customer |
| `customer.source.updated` | Payment source updated |
| `customer.source.deleted` | Payment source removed |

### Checkout

| Event | Description |
|---|---|
| `checkout.session.completed` | Checkout session completed successfully |
| `checkout.session.expired` | Checkout session expired (default 24 hours) |
| `checkout.session.async_payment_succeeded` | Async payment (e.g., ACH) succeeded after session |
| `checkout.session.async_payment_failed` | Async payment failed after session |

### Billing Portal

| Event | Description |
|---|---|
| `billing_portal.session.created` | Portal session created |
| `billing_portal.configuration.created` | Portal configuration created |
| `billing_portal.configuration.updated` | Portal configuration updated |

### Disputes

| Event | Description |
|---|---|
| `charge.dispute.created` | Dispute opened |
| `charge.dispute.updated` | Dispute updated (evidence submitted, etc.) |
| `charge.dispute.closed` | Dispute resolved |
| `charge.dispute.funds_reinstated` | Disputed funds returned to you |
| `charge.dispute.funds_withdrawn` | Disputed funds withdrawn from your account |

---

## 10. B2B Patterns

### Minimum Webhook Set for B2B Billing

For a typical B2B SaaS with subscription billing, the minimum set of webhooks to listen for:

- `customer.subscription.created` — Provision access
- `customer.subscription.updated` — Sync plan/quantity changes
- `customer.subscription.deleted` — Revoke access
- `invoice.paid` — Confirm payment, update billing records
- `invoice.payment_failed` — Trigger dunning flow
- `checkout.session.completed` — Handle new signups via Checkout

### Handling `invoice.payment_failed` for Dunning

When this event fires, the subscription enters a `past_due` status (if configured). Your application should:

1. Notify the customer that payment failed
2. Provide a link to update their payment method (Billing Portal or custom page)
3. Track retry attempts (Stripe retries automatically based on your Smart Retries or manual retry settings)
4. On final failure, decide whether to cancel or pause the subscription

### Syncing Subscription Status Changes

Listen for `customer.subscription.updated` and inspect `data.object.status`. Key statuses to handle:

- `active` — Full access
- `past_due` — Payment failed, grace period
- `canceled` — Subscription ended
- `unpaid` — All retries exhausted
- `paused` — Temporarily paused
- `trialing` — In trial period

### Processing `checkout.session.completed` for Onboarding

After a customer completes Checkout:

1. Retrieve the session with `expand: ['subscription', 'customer']`
2. Map the Stripe customer to your internal user/org
3. Store the `subscription.id` for future reference
4. Provision the appropriate plan based on `line_items`

---

> **Gap:** Webhook signature verification algorithm details, timestamp tolerance, and replay protection are not in the scraped API reference docs. The verification section above is based on standard Stripe integration patterns.

> **Gap:** The full list of 224+ event types is truncated in the source. The events listed above are the most relevant for B2B billing.

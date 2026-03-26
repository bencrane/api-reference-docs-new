# Stripe Invoices API Reference

**Canonical reference for the Stripe Invoices API, optimized for B2B SaaS billing integrations.**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

## Table of Contents

1. [The Invoice Object](#1-the-invoice-object)
2. [Status Lifecycle](#2-status-lifecycle)
3. [Create an Invoice](#3-create-an-invoice)
4. [Update an Invoice](#4-update-an-invoice)
5. [Finalize an Invoice](#5-finalize-an-invoice)
6. [Pay an Invoice](#6-pay-an-invoice)
7. [Void an Invoice](#7-void-an-invoice)
8. [Send an Invoice](#8-send-an-invoice)
9. [Delete an Invoice](#9-delete-an-invoice)
10. [Create a Preview Invoice](#10-create-a-preview-invoice)
11. [Add Lines to an Invoice](#11-add-lines-to-an-invoice)
12. [Invoice Items](#12-invoice-items)
13. [B2B Billing Patterns for Invoices](#13-b2b-billing-patterns-for-invoices)

---

## 1. The Invoice Object

The Invoice object represents a statement of amounts owed by a customer. Invoices are created automatically from subscriptions or manually for one-off charges. They track line items, taxes, discounts, and payment status through a defined lifecycle.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | — | Unique identifier for the invoice. For preview invoices, prefixed with `upcoming_in`. |
| `status` | enum, nullable | — | Current status: `draft`, `open`, `paid`, `uncollectible`, `void`. |
| `auto_advance` | boolean | No | Controls whether Stripe performs automatic collection (finalization, payment attempts, reminders). |
| `automatic_tax` | object | No | Settings for automatic tax calculation on this invoice. |
| `collection_method` | enum | No | How payment is collected: `charge_automatically` or `send_invoice`. |
| `confirmation_secret` | object, nullable, expandable | — | Contains the PaymentIntent `client_secret` for confirming payment on the client side. |
| `currency` | enum | — | Three-letter ISO currency code, in lowercase. |
| `customer` | string, expandable | — | ID of the customer who will be billed. |
| `customer_account` | string, nullable | — | ID of the Account object representing this customer. |
| `description` | string, nullable | No | An arbitrary string attached to the invoice. Referenced as "memo" in the Stripe Dashboard. |
| `hosted_invoice_url` | string, nullable | — | URL for the hosted invoice page where the customer can view and pay. `null` if the invoice has not been finalized. |
| `lines` | object | — | Line items on the invoice. Sorted: pending invoice items in reverse chronological order, then subscription items in reverse chronological order, then manually added items in chronological order. |
| `metadata` | object, nullable | No | Set of key-value pairs for storing structured data. Up to 50 keys, each with a string value up to 500 characters. |
| `parent` | object, nullable | — | The parent object (e.g., subscription) that generated this invoice. |
| `payments` | object, expandable | — | List of payment attempts for this invoice. |
| `period_end` | timestamp | — | End of the period that this invoice covers. |
| `period_start` | timestamp | — | Start of the period that this invoice covers. |
| `total` | integer | — | Total after discounts and taxes, in the smallest currency unit (e.g., cents). |
| `amount_due` | integer | — | Final amount due after credits and discounts are applied. |
| `amount_paid` | integer | — | Amount that has been paid. |
| `amount_remaining` | integer | — | Amount still owed. |
| `amount_overpaid` | integer | — | Amount paid in excess of `amount_due`. |
| `amount_shipping` | integer | — | Shipping cost amount. |
| `billing_reason` | enum | — | Why the invoice was created: `subscription_create`, `subscription_cycle`, `subscription_update`, `subscription`, `manual`, `upcoming`, `subscription_threshold`, `quote_accept`. |
| `due_date` | timestamp, nullable | No | Date on which payment is due. Only relevant when `collection_method` is `send_invoice`. |
| `default_payment_method` | string, nullable, expandable | No | ID of the default PaymentMethod for the invoice. |
| `default_source` | string, nullable, expandable | No | ID of the default payment source for the invoice (legacy). |
| `default_tax_rates` | array | No | Tax rates applied to the invoice as a whole. |
| `discounts` | array, expandable | No | Coupons or promotion codes applied to the invoice. |
| `footer` | string, nullable | No | Footer displayed on the invoice. |
| `invoice_pdf` | string, nullable | — | URL for the invoice PDF download. `null` if the invoice has not been finalized. |
| `number` | string, nullable | — | Unique invoice number assigned upon finalization. |
| `payment_settings` | object | No | Configuration for payment collection on the invoice. |
| `rendering` | object | No | Options for invoice PDF rendering. |
| `shipping_cost` | object, nullable | No | Shipping cost details. |
| `shipping_details` | object, nullable | No | Shipping address for the invoice. |
| `statement_descriptor` | string, nullable | No | Extra information about a charge for the customer's bank statement. |
| `status_transitions` | object | — | Timestamps for status transitions: `finalized_at`, `marked_uncollectible_at`, `paid_at`, `voided_at`. |
| `subtotal` | integer | — | Total before discounts and taxes. |
| `subtotal_excluding_tax` | integer, nullable | — | Subtotal excluding tax. |
| `total_excluding_tax` | integer, nullable | — | Total excluding tax. |
| `total_taxes` | integer | — | Total tax amount. |
| `total_discount_amounts` | array | — | Breakdown of discount amounts applied. |
| `application` | string, nullable, expandable | — | (Connect) ID of the Connect application that created the invoice. |
| `application_fee_amount` | integer, nullable | No | (Connect) Application fee amount in cents. |
| `issuer` | object | No | (Connect) The connected account that issues the invoice. |
| `on_behalf_of` | string, nullable, expandable | No | (Connect) The account on whose behalf the invoice is billed. |
| `transfer_data` | object, nullable | No | (Connect) Transfer data for the invoice payment. |
| `attempt_count` | integer | — | Number of payment attempts made for this invoice. |
| `attempted` | boolean | — | Whether an attempt has been made to pay the invoice. |
| `automatically_finalizes_at` | timestamp, nullable | — | Time at which the invoice will be automatically finalized. |
| `next_payment_attempt` | timestamp, nullable | — | Time of the next scheduled payment attempt. |
| `starting_balance` | integer | — | Customer balance before the invoice was finalized. |
| `ending_balance` | integer, nullable | — | Customer balance after the invoice was finalized. |
| `custom_fields` | array, nullable | No | Custom fields displayed on the invoice PDF. |
| `webhooks_delivered_at` | timestamp, nullable | — | Time at which webhooks for this invoice were successfully delivered. |

### Automatic Invoice Behavior

- Automatic invoices finalize **1 hour after the last successful webhook delivery** (or 1 hour after creation if no webhooks are configured).
- Customer credit balance is applied **before** determining `amount_due`.
- If `amount_due` is less than the **minimum charge amount** for the invoice currency, the invoice is automatically marked as paid and the amount is added to the customer's credit balance.

---

## 2. Status Lifecycle

```
                  finalize
  ┌─────────┐   ───────────>   ┌─────────┐
  │  draft   │                  │  open    │
  └─────────┘                  └────┬────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    v               v               v
              ┌──────────┐   ┌─────────────────┐  ┌──────┐
              │   paid   │   │ uncollectible   │  │ void │
              └──────────┘   └─────────────────┘  └──────┘
```

| Status | Description |
|--------|-------------|
| `draft` | Fully editable. Not yet sent or charged. Line items, metadata, and all fields can be modified. |
| `open` | Finalized and immutable for monetary values and `collection_method`. Payment has been attempted (for `charge_automatically`) or the invoice has been sent (for `send_invoice`). |
| `paid` | Successfully paid in full. |
| `uncollectible` | Marked as unlikely to be paid. Used for bad debt tracking. |
| `void` | Cancelled. The invoice maintains a paper trail (unlike deletion). Irreversible. |

---

## 3. Create an Invoice

```
POST /v1/invoices
```

Creates a new draft invoice. The invoice must be finalized before it can be paid or sent.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `customer` | string | Yes* | ID of the customer to invoice. *Required unless `from_invoice` is provided. |
| `auto_advance` | boolean | No | Whether to automatically finalize and attempt collection. Default: `false`. |
| `automatic_tax` | object | No | Settings for automatic tax calculation. |
| `collection_method` | enum | No | `charge_automatically` (default) or `send_invoice`. |
| `description` | string | No | Invoice memo. Displayed in the Dashboard and on the hosted invoice page. |
| `metadata` | object | No | Key-value pairs for structured data. |
| `subscription` | string | No | ID of the subscription to invoice. |
| `account_tax_ids` | array | No | Tax IDs of the account to include on the invoice. |
| `application_fee_amount` | integer | No | (Connect) Application fee in cents. |
| `automatically_finalizes_at` | timestamp | No | Time at which the invoice should auto-finalize. |
| `currency` | string | No | Three-letter ISO currency code. |
| `custom_fields` | array | No | Custom fields for the invoice PDF. |
| `days_until_due` | integer | No | Number of days until payment is due. Only for `send_invoice`. |
| `default_payment_method` | string | No | ID of the default PaymentMethod. |
| `default_source` | string | No | ID of the default payment source (legacy). |
| `default_tax_rates` | array | No | Tax rates to apply to the entire invoice. |
| `discounts` | array | No | Coupons or promotion codes to apply. |
| `due_date` | timestamp | No | Explicit due date. Only for `send_invoice`. |
| `effective_at` | timestamp | No | Date when the invoice is effective for reporting. |
| `footer` | string | No | Footer text on the invoice PDF. |
| `from_invoice` | object | No | Create from an existing invoice (clone). |
| `issuer` | object | No | (Connect) Account that issues the invoice. |
| `number` | string | No | Custom invoice number. |
| `on_behalf_of` | string | No | (Connect) Account on whose behalf to bill. |
| `payment_settings` | object | No | Payment collection configuration. |
| `pending_invoice_items_behavior` | enum | No | How to handle pending invoice items: `include` (default) or `exclude`. |
| `rendering` | object | No | PDF rendering options. |
| `shipping_cost` | object | No | Shipping cost details. |
| `shipping_details` | object | No | Shipping address. |
| `statement_descriptor` | string | No | Bank statement descriptor. |
| `transfer_data` | object | No | (Connect) Transfer configuration. |

### Example: Create a Draft Invoice

```bash
curl https://api.stripe.com/v1/invoices \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d collection_method=send_invoice \
  -d days_until_due=30 \
  -d auto_advance=false \
  -d "description=Q1 2026 Platform Services" \
  -d "metadata[tenant_id]=tenant_meridian_001" \
  -d "metadata[po_number]=PO-2026-0042" \
  -d "footer=Net 30. Questions? billing@yourcompany.com"
```

---

## 4. Update an Invoice

```
POST /v1/invoices/:id
```

Updates an existing invoice.

- **Draft invoices:** Fully editable. All fields can be modified.
- **Finalized invoices:** Monetary values and `collection_method` are locked. Non-monetary fields like `metadata`, `description`, `footer`, and `auto_advance` can still be updated.

Pass `auto_advance=false` to stop automatic finalizing, payment retries, and reminder emails.

### Example: Disable Auto-Advance on an Open Invoice

```bash
curl https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL \
  -u sk_test_YOUR_KEY: \
  -d auto_advance=false
```

---

## 5. Finalize an Invoice

```
POST /v1/invoices/:id/finalize
```

Finalizes a draft invoice, transitioning its status to `open`. Once finalized, monetary values are locked and the invoice is ready for payment or sending.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `auto_advance` | boolean | No | Whether to automatically attempt collection after finalizing. |

### Example: Finalize an Invoice

```bash
curl -X POST https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL/finalize \
  -u sk_test_YOUR_KEY: \
  -d auto_advance=true
```

---

## 6. Pay an Invoice

```
POST /v1/invoices/:id/pay
```

Manually triggers a payment attempt on an open invoice.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `forgive` | boolean | No | If `true`, forgive the remaining amount and mark the invoice as paid. |
| `mandate` | string | No | ID of the mandate to use for payment. |
| `off_session` | boolean | No | Indicates the customer is not in your checkout flow. |
| `paid_out_of_band` | boolean | No | If `true`, marks the invoice as paid without actually collecting payment (e.g., for wire transfers). |
| `payment_method` | string | No | ID of a specific PaymentMethod to charge. |
| `source` | string | No | ID of a specific source to charge (legacy). |

### Example: Mark as Paid Out of Band (Wire Transfer)

```bash
curl -X POST https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL/pay \
  -u sk_test_YOUR_KEY: \
  -d paid_out_of_band=true
```

---

## 7. Void an Invoice

```
POST /v1/invoices/:id/void
```

Voids a finalized invoice. This is **irreversible**. The invoice maintains a paper trail (unlike deletion), which is important for accounting and regulatory compliance.

- Only finalized (open, paid, or uncollectible) invoices can be voided.
- Consult local regulations before voiding invoices, as some jurisdictions require credit notes instead.

### Example: Void an Invoice

```bash
curl -X POST https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL/void \
  -u sk_test_YOUR_KEY:
```

---

## 8. Send an Invoice

```
POST /v1/invoices/:id/send
```

Sends a finalized invoice to the customer via email. The invoice must have `collection_method` set to `send_invoice`.

In **test mode**, no actual email is sent, but the `invoice.sent` event is still emitted.

### Example: Send an Invoice

```bash
curl -X POST https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL/send \
  -u sk_test_YOUR_KEY:
```

---

## 9. Delete an Invoice

```
DELETE /v1/invoices/:id
```

Permanently deletes an invoice. **Only draft invoices can be deleted.** Finalized invoices must be voided instead using the Void endpoint.

### Example: Delete a Draft Invoice

```bash
curl -X DELETE https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL \
  -u sk_test_YOUR_KEY:
```

---

## 10. Create a Preview Invoice

```
POST /v1/invoices/create_preview
```

Generates a preview of an upcoming invoice, including renewal charges, pending invoice items, prorations, and discounts. The preview invoice is **not** actually created in Stripe and cannot be paid or edited.

This is useful for showing customers what their next invoice will look like before it is generated.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `customer` | string | No | ID of the customer to preview. |
| `subscription` | string | No | ID of the subscription to preview. |
| `subscription_details` | object | No | Subscription parameters to preview (e.g., plan changes, proration). |
| `coupon` | string | No | Coupon to apply to the preview. |
| `currency` | string | No | Currency for the preview. Uses latest exchange rates for conversion. |
| `invoice_items` | array | No | Additional invoice items to include in the preview. |

### Example: Preview Next Subscription Invoice

```bash
curl -X POST https://api.stripe.com/v1/invoices/create_preview \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d subscription=sub_1abc2DEF3ghi4JKL
```

> **Gap:** The Upcoming Invoice endpoint (`GET /v1/invoices/upcoming`) returned 404 during documentation. This endpoint appears to be API-version-gated. Use `POST /v1/invoices/create_preview` as the recommended alternative.

---

## 11. Add Lines to an Invoice

```
POST /v1/invoices/:id/add_lines
```

Adds line items to a draft invoice.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `lines` | array | Yes | Array of line item objects to add. |

- The invoice must be in `draft` status.
- Maximum of **250 line items** per invoice.

### Example: Add Line Items to a Draft Invoice

```bash
curl -X POST https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL/add_lines \
  -u sk_test_YOUR_KEY: \
  -d "lines[0][amount]=50000" \
  -d "lines[0][description]=Platform license — Q1 2026" \
  -d "lines[1][amount]=15000" \
  -d "lines[1][description]=API overage — 150k requests"
```

> **Gap:** The Invoice Line Item object file returned 404 during documentation. Line item structure has been reconstructed from Add Lines response data.

---

## 12. Invoice Items

Invoice items represent individual charges or credits that are added to invoices. They can be attached to a specific draft invoice or left unattached to be automatically included on the customer's next invoice.

### Create an Invoice Item

```
POST /v1/invoiceitems
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `customer` | string | Yes | ID of the customer to charge. |
| `amount` | integer | Conditional | Amount in cents. Can be **negative** to represent a credit. Required if `pricing` is not provided. |
| `currency` | string | Conditional | Three-letter ISO currency code. Required if `amount` is provided. |
| `description` | string | No | Description displayed on the invoice. |
| `invoice` | string | No | ID of a draft invoice to attach this item to. If omitted, the item is added to the customer's next invoice. |
| `metadata` | object | No | Key-value pairs. |
| `period` | object | No | Billing period: `start` and `end` timestamps. |
| `pricing` | object | No | Pricing details (alternative to `amount`). |
| `proration` | boolean | No | Whether this item represents a proration adjustment. |
| `quantity_decimal` | string | No | Decimal quantity (e.g., `"1.5"`). |

- Maximum of **250 invoice items** per invoice.
- If no `invoice` is specified, the item is automatically added to the customer's next invoice.

### Update an Invoice Item

```
POST /v1/invoiceitems/:id
```

Updates an existing invoice item. Only allowed before the attached invoice is finalized.

### Delete an Invoice Item

```
DELETE /v1/invoiceitems/:id
```

Removes an invoice item. Only allowed before the attached invoice is finalized.

### Retrieve an Invoice Item

```
GET /v1/invoiceitems/:id
```

### List Invoice Items

```
GET /v1/invoiceitems
```

### Example: Create a Credit Invoice Item

```bash
curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d amount=-10000 \
  -d currency=usd \
  -d "description=Service credit — March 2026 SLA breach"
```

---

## 13. B2B Billing Patterns for Invoices

### One-Off Setup Fee Invoice

Create a standalone invoice for onboarding or implementation fees.

```bash
# 1. Create a draft invoice
curl https://api.stripe.com/v1/invoices \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d collection_method=send_invoice \
  -d days_until_due=15 \
  -d "description=Implementation & onboarding fee" \
  -d "metadata[type]=setup_fee"

# 2. Add the setup fee line item
curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d invoice=in_DRAFT_ID \
  -d amount=250000 \
  -d currency=usd \
  -d "description=Platform implementation fee"

# 3. Finalize the invoice
curl -X POST https://api.stripe.com/v1/invoices/in_DRAFT_ID/finalize \
  -u sk_test_YOUR_KEY: \
  -d auto_advance=true

# 4. Send the invoice
curl -X POST https://api.stripe.com/v1/invoices/in_DRAFT_ID/send \
  -u sk_test_YOUR_KEY:
```

### Net-30 Enterprise Billing

Standard B2B payment terms with `send_invoice` collection method.

```bash
curl https://api.stripe.com/v1/invoices \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d collection_method=send_invoice \
  -d days_until_due=30 \
  -d auto_advance=true \
  -d "description=March 2026 — Enterprise Platform Services" \
  -d "footer=Payment due within 30 days. Wire transfer details enclosed." \
  -d "metadata[billing_period]=2026-03" \
  -d "metadata[contract_id]=contract_001"
```

### Itemized Invoice with Multiple Deliverables

Break down charges across multiple line items for transparency.

```bash
# Create the draft invoice
curl https://api.stripe.com/v1/invoices \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d collection_method=send_invoice \
  -d days_until_due=30 \
  -d "description=Q1 2026 Services Summary"

# Add line items for each deliverable
curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d invoice=in_DRAFT_ID \
  -d amount=100000 \
  -d currency=usd \
  -d "description=Platform license — Q1 2026"

curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d invoice=in_DRAFT_ID \
  -d amount=35000 \
  -d currency=usd \
  -d "description=Premium support — Q1 2026"

curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d invoice=in_DRAFT_ID \
  -d amount=15000 \
  -d currency=usd \
  -d "description=API overage — 150k requests above plan"
```

### Credit Notes and Negative Invoice Items

Apply credits or adjustments using negative amounts.

```bash
# Add a credit to a draft invoice
curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d invoice=in_DRAFT_ID \
  -d amount=-25000 \
  -d currency=usd \
  -d "description=SLA credit — 99.5% uptime missed in February"

# Add a credit to the customer's next invoice (no invoice specified)
curl https://api.stripe.com/v1/invoiceitems \
  -u sk_test_YOUR_KEY: \
  -d customer=cus_R4bK7mZvqL2nXp \
  -d amount=-10000 \
  -d currency=usd \
  -d "description=Goodwill credit — migration assistance"
```

### Manual Pay for Wire Transfers

For enterprise customers who pay via wire transfer or ACH outside of Stripe.

```bash
# After confirming receipt of wire transfer, mark the invoice as paid
curl -X POST https://api.stripe.com/v1/invoices/in_1abc2DEF3ghi4JKL/pay \
  -u sk_test_YOUR_KEY: \
  -d paid_out_of_band=true
```

This is common in B2B where enterprise procurement teams require specific payment rails. The invoice moves to `paid` status without Stripe processing the actual payment, maintaining an accurate record.

### Recommended Metadata Keys for B2B Invoices

| Key | Purpose |
|-----|---------|
| `tenant_id` | Internal tenant or organization identifier. |
| `po_number` | Customer's purchase order number for reconciliation. |
| `contract_id` | Link to the governing contract or SOW. |
| `billing_period` | Human-readable billing period (e.g., `2026-03`). |
| `type` | Invoice category: `setup_fee`, `recurring`, `overage`, `credit`. |

> **Gap:** Upcoming Invoice endpoint (`GET /v1/invoices/upcoming`) returned 404 — appears API-version-gated. Use `POST /v1/invoices/create_preview` as the recommended alternative.

> **Gap:** Invoice Line Item object file returned 404. Structure reconstructed from Add Lines response.

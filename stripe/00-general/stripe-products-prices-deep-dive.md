# Stripe Products & Prices API Reference

**Comprehensive guide to Stripe's Products and Prices APIs for B2B SaaS billing — object schemas, endpoints, parameter tables, and real-world pricing model examples.**

Generated: 2026-03-26

**Parent:** [master-docs-overview.md](master-docs-overview.md)

---

## Table of Contents

1. [Products](#products)
   - [The Product Object](#the-product-object)
   - [Create a Product](#create-a-product)
   - [Update a Product](#update-a-product)
   - [Retrieve a Product](#retrieve-a-product)
   - [List Products](#list-products)
   - [Delete a Product](#delete-a-product)
   - [Search Products](#search-products)
2. [Prices](#prices)
   - [The Price Object](#the-price-object)
   - [Create a Price](#create-a-price)
   - [Update a Price](#update-a-price)
   - [Retrieve a Price](#retrieve-a-price)
   - [List Prices](#list-prices)
   - [Search Prices](#search-prices)
3. [B2B SaaS Pricing Models](#b2b-saas-pricing-models)
   - [Monthly Retainer](#1-monthly-retainer)
   - [Per-Lead Metered Billing](#2-per-lead-metered-billing)
   - [One-Time Setup Fee](#3-one-time-setup-fee)
   - [Tiered Usage — Graduated](#4-tiered-usage--graduated)
   - [Tiered Usage — Volume](#5-tiered-usage--volume)
   - [Custom Unit Amount](#6-custom-unit-amount)

---

## Products

### The Product Object

Products describe the specific goods or services you offer to your customers. Products are used in conjunction with Prices to configure pricing in Subscriptions, Invoices, Payment Links, and Checkout Sessions.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | auto | Unique identifier for the product. Can be custom-set at creation time. |
| `active` | boolean | — | Whether the product is currently available for purchase. Defaults to `true`. |
| `name` | string | **yes** | The product's name, meant to be displayable to the customer. |
| `description` | string, nullable | — | The product's long-form description, meant to be displayable to the customer. |
| `default_price` | string, nullable, expandable | — | The ID of the default Price for this product. |
| `metadata` | object | — | Set of key-value pairs for storing additional information. Up to 50 keys, each up to 40 characters. Values up to 500 characters. |
| `tax_code` | string, nullable, expandable | — | A tax code ID. Determines the tax category for the product. |
| `images` | array of strings | — | A list of up to 8 URLs of images for this product, meant to be displayable to the customer. |
| `marketing_features` | array of objects | — | A list of up to 15 marketing features for this product. Each feature has a `name` field (up to 80 characters). |
| `package_dimensions` | object, nullable | — | The dimensions of this product for shipping purposes. Contains `height`, `length`, `weight`, `width`. |
| `shippable` | boolean, nullable | — | Whether this product is shipped (i.e., physical goods). |
| `statement_descriptor` | string, nullable | — | Extra information about a product which will appear on your customer's credit card statement. Max 22 characters. |
| `unit_label` | string, nullable | — | A label that represents units of this product. Used with metered billing. Example: "seat", "API call". |
| `url` | string, nullable | — | A URL of a publicly-accessible webpage for this product. |
| `created` | timestamp | auto | Time at which the object was created. |
| `updated` | timestamp | auto | Time at which the object was last updated. |
| `livemode` | boolean | auto | Has the value `true` if the object exists in live mode or `false` if it exists in test mode. |

---

### Create a Product

**`POST /v1/products`**

Creates a new product object.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | **yes** | The product's name. |
| `active` | boolean | — | Whether the product is available for purchase. Defaults to `true`. |
| `description` | string | — | The product's description. |
| `id` | string | — | Custom unique identifier for the product. |
| `metadata` | object | — | Key-value pairs for additional information. |
| `tax_code` | string | — | A tax code ID. |
| `default_price_data` | object | — | Data used to generate a new Price object inline. Contains `currency`, `unit_amount`, `recurring`, etc. |
| `images` | array of strings | — | A list of image URLs. |
| `marketing_features` | array of objects | — | A list of marketing features. |
| `package_dimensions` | object | — | Shipping dimensions. |
| `shippable` | boolean | — | Whether the product is shipped. |
| `statement_descriptor` | string | — | Statement descriptor. |
| `unit_label` | string | — | Unit label for metered billing. |
| `url` | string | — | URL for the product. |

```bash
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="Marketing Platform" \
  -d description="Full-service B2B marketing automation platform" \
  -d "metadata[tier]"="enterprise"
```

---

### Update a Product

**`POST /v1/products/:id`**

Updates the specified product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

```bash
curl https://api.stripe.com/v1/products/prod_ABC123 \
  -u sk_test_XXXX: \
  -d description="Updated description for marketing platform" \
  -d active=true
```

---

### Retrieve a Product

**`GET /v1/products/:id`**

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list.

```bash
curl https://api.stripe.com/v1/products/prod_ABC123 \
  -u sk_test_XXXX:
```

---

### List Products

**`GET /v1/products`**

Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.

**Filter parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `active` | boolean | Only return products that are active or inactive. |
| `created` | object or timestamp | Filter by creation date. Supports `gt`, `gte`, `lt`, `lte`. |
| `ids` | array of strings | Only return products with the given IDs. Up to 100. |
| `shippable` | boolean | Only return products that can or cannot be shipped. |
| `limit` | integer | Number of objects to return (1–100, default 10). |
| `starting_after` | string | Cursor for pagination. |
| `ending_before` | string | Cursor for pagination. |

```bash
curl https://api.stripe.com/v1/products?active=true&limit=25 \
  -u sk_test_XXXX:
```

---

### Delete a Product

**`DELETE /v1/products/:id`**

Delete a product. Deleting a product is only possible if it has no prices associated with it.

> **Gap:** There is no bulk delete endpoint. To delete a product that has prices, you must first individually archive or delete all associated prices. There is no cascade delete.

```bash
curl -X DELETE https://api.stripe.com/v1/products/prod_ABC123 \
  -u sk_test_XXXX:
```

---

### Search Products

**`GET /v1/products/search`**

Search for products using Stripe's Search Query Language. Supports searching by `active`, `description`, `name`, `shippable`, `url`, `metadata`, and `created`.

```bash
curl https://api.stripe.com/v1/products/search \
  -u sk_test_XXXX: \
  --data-urlencode "query=active:'true' AND metadata['tier']:'enterprise'"
```

> **Gap:** Search results may lag behind recent changes by up to 1 minute. Search is eventually consistent and should not be used for real-time lookups.

---

## Prices

### The Price Object

Prices define the unit cost, currency, and billing cycle for both one-time and recurring purchases. Each Price is linked to a single Product. You can have multiple active and inactive Prices per Product.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | auto | Unique identifier for the price. |
| `active` | boolean | — | Whether the price can be used for new purchases. Defaults to `true`. |
| `billing_scheme` | enum | — | Describes how to compute the price per period. `per_unit` or `tiered`. Defaults to `per_unit`. **Immutable after creation.** |
| `currency` | enum | **yes** | Three-letter ISO currency code in lowercase. **Immutable after creation.** |
| `custom_unit_amount` | object, nullable | — | When set, provides configuration for per-customer customizable unit pricing. Contains `enabled`, `minimum`, `maximum`, `preset`. |
| `lookup_key` | string, nullable | — | A stable lookup identifier that you define. Useful for referencing prices without hard-coding IDs. |
| `metadata` | object | — | Key-value pairs for additional information. |
| `nickname` | string, nullable | — | A brief, internal description of the price, not visible to customers. |
| `product` | string, expandable | **yes** | The ID of the product this price is associated with. **Immutable after creation.** |
| `recurring` | object, nullable | — | The recurring components of a price. **Immutable after creation.** |
| `recurring.interval` | enum | — | Billing frequency: `day`, `week`, `month`, `year`. |
| `recurring.interval_count` | integer | — | Number of intervals between billings. E.g., `interval=month` and `interval_count=3` bills every 3 months. |
| `recurring.trial_period_days` | integer, nullable | — | Default number of trial days when subscribing. |
| `recurring.usage_type` | enum | — | `licensed` (charge for full quantity) or `metered` (charge for reported usage). Defaults to `licensed`. |
| `tax_behavior` | enum, nullable | — | `inclusive`, `exclusive`, or `unspecified`. **Immutable once set to `inclusive` or `exclusive`.** |
| `tiers` | array, nullable, expandable | — | Each element represents a pricing tier. Only present if `billing_scheme=tiered`. |
| `tiers_mode` | enum, nullable | — | `volume` or `graduated`. Required if `billing_scheme=tiered`. |
| `transform_quantity` | object, nullable | — | Apply a transformation to the reported usage or quantity. Contains `divide_by` and `round`. |
| `type` | enum | auto | `one_time` or `recurring`. Determined by presence of `recurring` parameter. **Immutable after creation.** |
| `unit_amount` | integer, nullable | — | Unit cost in the smallest currency unit (e.g., cents). **Immutable after creation.** |
| `unit_amount_decimal` | decimal string, nullable | — | Unit cost with decimal precision. Useful for per-unit costs below 1 cent. **Immutable after creation.** |
| `currency_options` | object, nullable, expandable | — | Prices defined in each supported currency. |
| `created` | timestamp | auto | Time at which the object was created. |
| `livemode` | boolean | auto | `true` if the object exists in live mode. |

---

### Create a Price

**`POST /v1/prices`**

Creates a new price for an existing product.

**Required parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `currency` | string | **yes** | Three-letter ISO currency code. |
| `product` | string | **yes** (unless `product_data`) | The ID of the product. |
| One of: `unit_amount`, `unit_amount_decimal`, `custom_unit_amount` | varies | **yes** (unless tiered) | The unit cost. |

**Optional parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `active` | boolean | Whether the price is available for new purchases. |
| `billing_scheme` | enum | `per_unit` or `tiered`. |
| `metadata` | object | Key-value pairs. |
| `nickname` | string | Internal description. |
| `recurring` | object | Recurring billing configuration. |
| `tax_behavior` | enum | `inclusive`, `exclusive`, `unspecified`. |
| `tiers` | array | **Required** if `billing_scheme=tiered`. Pricing tier definitions. |
| `tiers_mode` | enum | **Required** if `billing_scheme=tiered`. `volume` or `graduated`. |
| `lookup_key` | string | Stable lookup identifier. |
| `transfer_lookup_key` | boolean | If `true`, transfers the `lookup_key` from an existing price to this one. |
| `transform_quantity` | object | Transformation to apply to quantity. |
| `currency_options` | object | Multi-currency pricing. |
| `product_data` | object | Inline product creation data (alternative to `product`). |

> **Gap:** The following fields are **immutable after creation**: `unit_amount`, `currency`, `product`, `recurring`, `billing_scheme`, `type`. To change pricing, you must create a new Price and deactivate the old one. Subscriptions referencing the old Price must be migrated individually.

```bash
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_ABC123 \
  -d unit_amount=500000 \
  -d "recurring[interval]"=month \
  -d nickname="Enterprise monthly"
```

---

### Update a Price

**`POST /v1/prices/:id`**

Updates the specified price. Only the following fields are mutable:

| Parameter | Type | Description |
|-----------|------|-------------|
| `active` | boolean | Whether the price can be used for new purchases. |
| `metadata` | object | Key-value pairs. |
| `nickname` | string | Internal description. |
| `tax_behavior` | enum | Only mutable if currently `unspecified`. |
| `lookup_key` | string | Stable lookup identifier. |

```bash
curl https://api.stripe.com/v1/prices/price_XYZ789 \
  -u sk_test_XXXX: \
  -d active=false \
  -d nickname="Deprecated - Enterprise monthly v1"
```

---

### Retrieve a Price

**`GET /v1/prices/:id`**

Retrieves the details of an existing price. Also accepts valid legacy Plan IDs for backward compatibility.

```bash
curl https://api.stripe.com/v1/prices/price_XYZ789 \
  -u sk_test_XXXX:
```

---

### List Prices

**`GET /v1/prices`**

Returns a list of prices, sorted by creation date (most recent first).

**Filter parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `active` | boolean | Only return active or inactive prices. |
| `currency` | string | Only return prices in the given currency. |
| `product` | string | Only return prices for the given product. |
| `type` | enum | `one_time` or `recurring`. |
| `lookup_keys` | array of strings | Only return prices with these lookup keys. |
| `recurring` | object | Filter by recurring fields (`interval`, `usage_type`). |
| `created` | object or timestamp | Filter by creation date. |
| `limit` | integer | Number of objects to return (1–100, default 10). |

```bash
curl "https://api.stripe.com/v1/prices?product=prod_ABC123&active=true" \
  -u sk_test_XXXX:
```

---

### Search Prices

**`GET /v1/prices/search`**

Search for prices using Stripe's Search Query Language. Supports searching by `active`, `currency`, `lookup_key`, `metadata`, `product`, `type`, and `created`.

```bash
curl https://api.stripe.com/v1/prices/search \
  -u sk_test_XXXX: \
  --data-urlencode "query=product:'prod_ABC123' AND type:'recurring'"
```

> **Gap:** Search results may lag behind recent changes by up to 1 minute. Search is eventually consistent.

---

## B2B SaaS Pricing Models

The following examples demonstrate common B2B SaaS billing patterns using Stripe Products and Prices. Each model includes the full curl commands needed for implementation.

---

### 1. Monthly Retainer

A fixed monthly fee — the most common B2B pricing model. The customer pays a flat amount each billing cycle.

**Use case:** "Marketing Retainer" at $5,000/month.

```bash
# Step 1: Create the Product
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="Marketing Retainer" \
  -d description="Full-service marketing retainer — strategy, execution, and reporting" \
  -d "metadata[billing_model]"="flat_rate"

# Step 2: Create the Price
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_RETAINER \
  -d unit_amount=500000 \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=licensed \
  -d nickname="Marketing retainer - $5k/mo"
```

**Key details:**
- `unit_amount=500000` — Amount in cents ($5,000.00)
- `recurring.usage_type=licensed` — Charges the full amount each cycle regardless of usage
- `recurring.interval=month` — Bills once per month

---

### 2. Per-Lead Metered Billing

Usage-based pricing where the customer is billed based on actual consumption reported via the Stripe Meter or Usage Records API.

**Use case:** "Lead Delivery" at $25 per lead.

```bash
# Step 1: Create the Product
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="Lead Delivery" \
  -d description="Qualified lead delivery service — billed per lead" \
  -d unit_label="lead" \
  -d "metadata[billing_model]"="metered"

# Step 2: Create the Price
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_LEADS \
  -d unit_amount=2500 \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=metered \
  -d nickname="Per-lead delivery - $25/lead"
```

**Key details:**
- `unit_label="lead"` — Appears on invoices as the unit of measurement
- `recurring.usage_type=metered` — Charges based on usage reported during the billing period
- Usage must be reported via the Usage Records API or Stripe Meter before the billing period ends

> **Gap:** Metered prices do not support `quantity` at subscription creation. You must report usage separately. If no usage is reported in a billing period, the charge is $0.

---

### 3. One-Time Setup Fee

A non-recurring charge typically used for onboarding, implementation, or setup. Combined with a recurring price on the same subscription for a complete billing setup.

**Use case:** "Onboarding" at $2,500 one-time.

```bash
# Step 1: Create the Product
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="Onboarding" \
  -d description="Platform onboarding — data migration, configuration, and training" \
  -d "metadata[billing_model]"="one_time"

# Step 2: Create the Price
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_ONBOARDING \
  -d unit_amount=250000 \
  -d nickname="Onboarding fee - $2,500"
```

**Key details:**
- No `recurring` parameter — this makes it a `type=one_time` price
- One-time prices can be added to subscriptions as invoice items; they appear on the first invoice only
- Commonly paired with a recurring price in the same subscription

---

### 4. Tiered Usage — Graduated

With graduated tiers, each unit is priced at the rate of the tier it falls into. The first N units are at the lowest rate, the next batch at the next rate, and so on.

**Use case:** API calls priced at graduated tiers — 1-100 at $30/ea, 101-500 at $20/ea, 501+ at $12/ea.

```bash
# Step 1: Create the Product
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="API Calls" \
  -d description="Graduated tiered API call pricing" \
  -d unit_label="call" \
  -d "metadata[billing_model]"="tiered_graduated"

# Step 2: Create the Price with graduated tiers
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_APICALLS \
  -d billing_scheme=tiered \
  -d tiers_mode=graduated \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=metered \
  -d "tiers[0][up_to]"=100 \
  -d "tiers[0][unit_amount]"=3000 \
  -d "tiers[1][up_to]"=500 \
  -d "tiers[1][unit_amount]"=2000 \
  -d "tiers[2][up_to]"=inf \
  -d "tiers[2][unit_amount]"=1200 \
  -d nickname="API calls - graduated tiers"
```

**Key details:**
- `billing_scheme=tiered` — Enables tier-based pricing
- `tiers_mode=graduated` — Each unit is priced according to the tier it falls in
- The last tier must have `up_to=inf`
- **Example: 250 calls = (100 x $30) + (150 x $20) = $3,000 + $3,000 = $6,000**

> **Gap:** Tiers also support `flat_amount` per tier (a fixed fee added when the tier is reached). The `unit_amount` and `flat_amount` can be combined within the same tier. This is commonly used for platform fees at each tier threshold.

---

### 5. Tiered Usage — Volume

With volume tiers, ALL units are priced at the rate of the single tier the total quantity falls into. The tier is determined by total usage, and every unit gets that tier's price.

**Use case:** Same tier thresholds but volume-based — 1-100 at $30/ea, 101-500 at $20/ea, 501+ at $12/ea.

```bash
# Step 1: Create the Product (reuse existing or create new)
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="API Calls - Volume" \
  -d description="Volume tiered API call pricing" \
  -d unit_label="call" \
  -d "metadata[billing_model]"="tiered_volume"

# Step 2: Create the Price with volume tiers
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_APICALLS_VOL \
  -d billing_scheme=tiered \
  -d tiers_mode=volume \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=metered \
  -d "tiers[0][up_to]"=100 \
  -d "tiers[0][unit_amount]"=3000 \
  -d "tiers[1][up_to]"=500 \
  -d "tiers[1][unit_amount]"=2000 \
  -d "tiers[2][up_to]"=inf \
  -d "tiers[2][unit_amount]"=1200 \
  -d nickname="API calls - volume tiers"
```

**Key details:**
- `tiers_mode=volume` — All units are priced at the single tier the total quantity falls into
- **Example: 250 calls = 250 x $20 = $5,000** (falls in the 101–500 tier, so ALL 250 units are at $20)
- Compare with graduated: graduated would charge $6,000 for the same 250 calls

> **Gap:** Volume pricing creates a "cliff" effect at tier boundaries. A customer using 100 units pays $3,000, but a customer using 101 units pays $2,020. Consider whether this incentive structure is appropriate for your business model.

---

### 6. Custom Unit Amount

Allows customers to specify their own price within constraints you define. Commonly used for donations, tips, pay-what-you-want models, or negotiated enterprise pricing.

**Use case:** Let customers choose their own amount for a service credit, with a minimum of $100 and a suggested default of $500.

```bash
# Step 1: Create the Product
curl https://api.stripe.com/v1/products \
  -u sk_test_XXXX: \
  -d name="Service Credit" \
  -d description="Prepaid service credit — choose your own amount" \
  -d "metadata[billing_model]"="custom_amount"

# Step 2: Create the Price with custom unit amount
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_CREDIT \
  -d "custom_unit_amount[enabled]"=true \
  -d "custom_unit_amount[minimum]"=10000 \
  -d "custom_unit_amount[maximum]"=1000000 \
  -d "custom_unit_amount[preset]"=50000 \
  -d nickname="Service credit - custom amount"
```

**Key details:**
- `custom_unit_amount.enabled=true` — Enables customer-defined pricing
- `minimum=10000` — Floor of $100.00 (in cents)
- `maximum=1000000` — Ceiling of $10,000.00 (in cents)
- `preset=50000` — Pre-populated default of $500.00 (in cents)
- Cannot be combined with `unit_amount` or `unit_amount_decimal`
- Works with Stripe Checkout and Payment Links; the customer enters their amount during checkout

> **Gap:** Custom unit amounts are only supported in Checkout Sessions and Payment Links. They are not supported when creating subscriptions directly via the API — you must use a Checkout Session with `mode=subscription` or `mode=payment`.

---

## Quick Reference: Pricing Model Comparison

| Model | Type | billing_scheme | tiers_mode | usage_type | Immutable Fields |
|-------|------|----------------|------------|------------|------------------|
| Monthly retainer | recurring | per_unit | — | licensed | unit_amount, currency, recurring |
| Per-lead metered | recurring | per_unit | — | metered | unit_amount, currency, recurring |
| Setup fee | one_time | per_unit | — | — | unit_amount, currency |
| Graduated tiers | recurring | tiered | graduated | metered | tiers, currency, recurring, billing_scheme |
| Volume tiers | recurring | tiered | volume | metered | tiers, currency, recurring, billing_scheme |
| Custom amount | one_time | per_unit | — | — | custom_unit_amount, currency |

---

## Common Patterns and Considerations

### Combining Prices on a Single Subscription

B2B subscriptions often combine multiple pricing models. For example:

- **Setup + retainer:** Add a one-time onboarding price as an invoice item, plus a recurring monthly retainer
- **Base fee + metered overage:** One `licensed` recurring price for the base fee, plus one `metered` recurring price for overage
- **Multi-product bundle:** Multiple products each with their own prices on a single subscription

### Price Migration Strategy

Because core price fields are immutable, plan changes follow this workflow:

1. Create a new Price with the desired configuration
2. Update the Subscription to replace the old Price with the new one
3. Deactivate the old Price (`active=false`) to prevent new subscriptions
4. Do NOT delete old Prices — they are still referenced by historical invoices

> **Gap:** There is no API endpoint for bulk-migrating subscriptions from one Price to another. Each subscription must be updated individually. For large migrations, implement a worker that iterates through subscriptions using the List Subscriptions endpoint with a `price` filter.

### Lookup Keys for Stable References

Use `lookup_key` to decouple your application code from specific Price IDs:

```bash
# Create a price with a lookup key
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_ABC123 \
  -d unit_amount=500000 \
  -d "recurring[interval]"=month \
  -d lookup_key="standard_monthly" \
  -d nickname="Standard monthly v2"

# When creating a new version, transfer the lookup key
curl https://api.stripe.com/v1/prices \
  -u sk_test_XXXX: \
  -d currency=usd \
  -d product=prod_ABC123 \
  -d unit_amount=600000 \
  -d "recurring[interval]"=month \
  -d lookup_key="standard_monthly" \
  -d transfer_lookup_key=true \
  -d nickname="Standard monthly v3"
```

This way, your application always references `standard_monthly` and never needs to update hard-coded Price IDs.

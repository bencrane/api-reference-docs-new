# Enigma Attribute Tier Map

Exhaustive attribute → tier → credit mapping for every documented attribute on every entity type. Companion to [`ENIGMA_CANONICAL_REFERENCE.md`](ENIGMA_CANONICAL_REFERENCE.md).

> **Source of truth:** `enigma/04-resources/03-pricing-and-credit-use.md` (the `_schemaExtended` introspection summary) cross-referenced against the per-attribute files in `enigma/09-data-attributes/`.
>
> **Pricing tiers:** Free = 0 credits, Core = 1 credit, Plus = 3 credits, Premium = 5 credits per entity. Highest-tier-wins per entity.
>
> **Programmatic lookup:** Run `_schemaExtended { types { name pricingTier fields { name pricingTier } } }` against `https://api.enigma.com/graphql` for the live tier assignments.

---

## Brand

| Entity | Attribute | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|---|
| Brand | `name` | `BrandName` | Core | 1 | Customer-facing brand name; ranked by dataset quality and frequency. |
| Brand | `address` | `Address` | Core | 1 | USPS-standard physical address (street, city, state, zip, county, MSA, CSA, lat/lng, h3Index). |
| Brand | `addressDeliverability` | `AddressDeliverability` | Plus | 3 | USPS deliverability, RDI (residential/commercial), CMRA virtual flag, delivery type. |
| Brand | `brandActivity` | `BrandActivity` | Plus | 3 | Notable activities (e.g., Cannabis). [Source attribute file empty; tier from introspection summary.] |
| Brand | `locationDescription` | `BrandLocationDescription` | Core | 1 | Geographic summary (top 5 states or specific city/state). |
| Brand | `revenueQuality` | `BrandRevenueQuality` | Plus | 3 | Revenue anomaly flags (drops to zero, 20% decrease, 250% increase) with High/Medium severity. |
| Brand | `cardTransactions` | `BrandCardTransaction` | Plus | 3 | Card transaction metrics for 1m/3m/12m periods (8 quantity types). |
| Brand | `emailAddress` | `EmailAddress` | Core | 1 | Email associated with the business. |
| Brand | `industry` | `Industry` | Core | 1 | NAICS (2017, 2022), SIC, MCC, GICS, Enigma classifications. |
| Brand | `isMarketable` | `BrandIsMarketable` | Core | 1 | Boolean: open locations + recent revenue + recent reviews. |
| Brand | `onlinePresence` | `WebsiteOnlinePresence` | Core | 1 | "Yes" or null for online sales / payments. |
| Brand | `phoneNumber` | `PhoneNumber` | Core | 1 | 12-digit string (NANP-compliant). |
| Brand | `registeredEntity` | `RegisteredEntity` | Premium | 5 | Standardized name, type, formation date/year. |
| Brand | `registration` | `Registration` | Premium | 5 | Per-state SoS registration with status fields. |
| Brand | `role` | `Role` | Plus | 3 | People/legal entities holding roles (jobTitle, jobFunction, managementLevel). |
| Brand | `technologiesUsed` (web) | `WebsiteTechnologiesUsed` | Premium | 5 | Web tech: Adyen, Braintree, PayPal, Shopify, Stripe. |
| Brand | `txnMerchant` | `TxnMerchant` | Plus | 3 | Card-network merchant identifiers tied to the brand. |
| Brand | `watchlistEntry` | `WatchlistEntry` | Premium | 5 | OFAC SDN + Consolidated Sanctions list entries. |
| Brand | `website` | `Website` | Core | 1 | Full URL with decomposed parts (domain, subdomain, TLD, path, fragment). |
| Brand | `websiteContent` | `WebsiteContent` | Plus | 3 | Website state at point in time (HTTP status, favicon); crawled ≥ every 90 days. |

---

## Operating Location

| Entity | Attribute | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|---|
| Operating Location | `name` | `OperatingLocationName` | Core | 1 | Location-specific name (e.g., "Target - Crossgates Mall"). |
| Operating Location | `address` | `Address` | Core | 1 | USPS-standard address. |
| Operating Location | `addressDeliverability` | `AddressDeliverability` | Plus | 3 | USPS deliverability + CMRA virtual flag. |
| Operating Location | `cardTransactions` | `OperatingLocationCardTransaction` | Plus | 3 | Raw + projected card transaction quantities; 1m/3m/12m periods; 8 quantity types. |
| Operating Location | `emailAddress` | `EmailAddress` | Core | 1 | Email associated with the location. |
| Operating Location | `isMarketable` | `OperatingLocationIsMarketable` | Core | 1 | Boolean marketability (active status + recent revenue + recent reviews). |
| Operating Location | `locationType` | `OperatingLocationLocationType` | Core | 1 | retail, office, headquarters, hospitality, medical, etc. (15+ values). |
| Operating Location | `operatingStatus` | `OperatingLocationOperatingStatus` | Core | 1 | Open / Temporarily Closed / Closed / Unknown. |
| Operating Location | `onlinePresence` | `WebsiteOnlinePresence` | Core | 1 | E-commerce indicator. |
| Operating Location | `phoneNumber` | `PhoneNumber` | Core | 1 | 12-digit string. |
| Operating Location | `rank` | `OperatingLocationRank` | Plus | 3 | Card-revenue rank within H3 res-4 + same Enigma industry; needs ≥10 nearby same-industry businesses. |
| Operating Location | `revenueQuality` | `OperatingLocationRevenueQuality` | Plus | 3 | Revenue anomaly flags with High/Medium severity. |
| Operating Location | `registeredEntity` | `RegisteredEntity` | Premium | 5 | Linked legal entity via location relationship. |
| Operating Location | `registration` | `Registration` | Premium | 5 | Per-state SoS registration. |
| Operating Location | `reviewSummary` | `ReviewSummary` | Plus | 3 | Public review counts, score average, first/last review date. |
| Operating Location | `role` | `Role` | Plus | 3 | Roles held by people/entities at this location. |
| Operating Location | `technologiesUsed` | `OperatingLocationTechnologiesUsed` | Premium | 5 | POS/payments tech: Clover, PayPal, Shopify, Square, Stripe, Toast. |
| Operating Location | `watchlistEntry` | `WatchlistEntry` | Premium | 5 | OFAC list entries. |
| Operating Location | `website` | `Website` | Core | 1 | URL with decomposed parts. |
| Operating Location | `websiteContent` | `WebsiteContent` | Plus | 3 | Website crawl state. |

---

## Legal Entity

| Entity | Attribute | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|---|
| Legal Entity | `name` | `LegalEntityName` | Free | 0 | Legal entity name. |
| Legal Entity | `type` | `LegalEntityType` | Free | 0 | Legal classification (Person, Corporation, LLC, etc.). |
| Legal Entity | `address` | `Address` | Core | 1 | USPS-standard address; types include site, registered, mailing, registered_agent_address, registered_business_address. |
| Legal Entity | `addressDeliverability` | `AddressDeliverability` | Plus | 3 | USPS deliverability. |
| Legal Entity | `bankruptcy` | `LegalEntityBankruptcy` | Premium | 5 | Federal bankruptcy filings (Chapter 7/11/12/13/15) from PACER. Add-on. |
| Legal Entity | `emailAddress` | `EmailAddress` | Core | 1 | Email — primarily via Contacts attribute (file delivery, not API). |
| Legal Entity | `phoneNumber` | `PhoneNumber` | Core | 1 | 12-digit NANP-compliant (e.g., `+18005102856`). 60% business / 69% locations coverage. |
| Legal Entity | `registeredEntity` | `RegisteredEntity` | Premium | 5 | Standardized name, registeredEntityType, formationDate, formationYear. |
| Legal Entity | `registration` | `Registration` | Premium | 5 | Domestic/foreign registration: file number, dates, status, sub_status, status_detail. |
| Legal Entity | `role` | `Role` | Plus | 3 | People/entities holding roles. 44% coverage. |
| Legal Entity | `tin` | `Tin` | Premium | 5 | TIN (focus: EIN). 9-digit string. Add-on requested via `attrs=tin_verification`. |
| Legal Entity | `watchlistEntry` | `WatchlistEntry` | Premium | 5 | OFAC SDN + Non-SDN. With DOB: 99.97% TPR / 0.4% FPR. Without DOB: 99.97% TPR / 5% FPR. |

---

## Person

| Entity | Attribute | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|---|
| Person | `firstName` | `Person.firstName` | Core | 1 | First name. |
| Person | `lastName` | `Person.lastName` | Core | 1 | Last name. |
| Person | `fullName` | `Person.fullName` | Core | 1 | Full name. |
| Person | `dateOfBirth` | `Person.dateOfBirth` | Core | 1 | ISO 8601 date of birth. |
| Person | `personId` | `Person.personId` | Core | 1 | Unique ID. |

> Source `enigma/08-reference/06-objects/Person.md` is an auto-generated placeholder. The fields above come from the `_schemaExtended` introspection summary in `enigma/04-resources/03-pricing-and-credit-use.md` ("Person: firstName, lastName, fullName, dateOfBirth, personId").

---

## Address-as-Entity

The `Address` GraphQL object is its own type and can be returned directly by certain queries (and is one of the values in the `EntityType` enum). It is documented in `enigma/09-data-attributes/01-brand/01-address.md` and is at the **Core tier (1 credit)**. Fields:

| Field | Type | Description |
|---|---|---|
| `streetAddress1` | String | Primary street line. |
| `streetAddress2` | String | Secondary line (apt, suite, floor). |
| `city` | String | City. |
| `county` | String | County. |
| `state` | String | State abbreviation. |
| `zip` | String | ZIP. |
| `country` | String | ISO-3 country code. |
| `csa` | String | Combined Statistical Area. |
| `msa` | String | Metropolitan/Micropolitan Statistical Area. |
| `latitude` | Float | Latitude. |
| `longitude` | Float | Longitude. |
| `h3Index` | String | H3 geospatial index (resolution 10). |
| `fullAddress` | String | Complete formatted address. |
| `id` | UUID | Unique identifier. |
| `firstObservedDate` | String | First observation date. |
| `lastObservedDate` | String | Last observation date. |

Companion `AddressDeliverability` is **Plus tier (3 credits)** with `deliverable` (`deliverable` / `vacant` / `not_deliverable` / null), `deliveryType` (street, multi-tenant building, post office box, firm, rural route or highway contract route, general delivery, null), `rdi` (Residential / Commercial), `virtual` (`virtual_cmra` / `not_virtual` / null).

---

## Common Fields on Every Attribute Object

Per the per-attribute files in `enigma/09-data-attributes/`, every attribute object includes these standard fields (no separate billing — included in the attribute's tier):

| Field | Type | Description |
|---|---|---|
| `id` | UUID | Unique identifier for this attribute observation. |
| `firstObservedDate` | String | Date the attribute was first observed. |
| `lastObservedDate` | String | Date the attribute was last observed. |

---

## CardTransaction Quantity Types

For `BrandCardTransaction` (Plus tier) and `OperatingLocationCardTransaction` (Plus tier), the `quantityType` values are:

| Quantity Type | Meaning |
|---|---|
| `card_revenue_amount` | Sum of all transaction amounts in dollars. |
| `card_transactions_count` | Total number of card transactions. |
| `avg_transaction_size` | Average transaction size in dollars. |
| `card_customers_average_daily_count` | Average number of unique daily customers. |
| `card_revenue_yoy_growth` | Ratio of current period revenue to one year prior. |
| `card_revenue_prior_period_growth` | Ratio of current period revenue to previous period. |
| `refunds_amount` | Total refunds in dollars (negative). |
| `has_transactions` | 1 if any transactions in the period, else 0. |

`period` values: `1m`, `3m`, `12m`. Each record has `periodStartDate`, `periodEndDate`, `rawQuantity` (unscaled), `projectedQuantity` (scaled by panel multiplier).

---

## Registration Status Values

For `Registration` (Premium tier):

| Field | Possible Values |
|---|---|
| `status` | `active`, `inactive`, `unknown` |
| `subStatus` | `good_standing`, `not_good_standing`, `pending_active`, `pending_inactive`, `unknown`, null |
| `statusDetail` | Free-text official message from the state |
| `jurisdictionType` | `domestic`, `foreign` |

Verify package returns all status fields. Identify package returns a restricted subset (`file_number`, `registered_name`, `addresses`, `persons`, `issue_date`, `registration_state`).

---

## Tier Notes & Caveats

1. **Pricing is per-entity.** For multi-attribute queries on the same entity, the highest tier among returned attributes determines the cost.
2. **Free tier = 0 credits.** `LegalEntityName` and `LegalEntityType` are free.
3. **Tier values can change.** The source explicitly notes: "Attribute pricing tiers are subject to change. Refer to the [attribute tier page](https://www.enigma.com/pricing) or run Enigma's GraphQL introspection to get the latest attribute tier assignments."
4. **`brandActivity` is included** at Plus tier per the `_schemaExtended` summary, even though `enigma/09-data-attributes/01-brand/03-brand-activity.md` is empty.
5. **`Tin` tier is Premium** per the `_schemaExtended` summary. The `TinType` enum supports `EIN`, `SSN`, `ITIN`, `TIN` values for input.
6. **`TxnMerchant`** is documented in the introspection summary at the Plus tier but does not have a dedicated file under `09-data-attributes/`.
7. **Connection wrapper objects** (e.g., `BrandOperatingLocationConnection`, `AddressLegalEntityEdge`) do not themselves carry a tier — they wrap the underlying typed objects, which are billed at their own tier.

---

*End of attribute tier map.*

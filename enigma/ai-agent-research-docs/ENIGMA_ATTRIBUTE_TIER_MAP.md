# Enigma Attribute Tier Map

Exhaustive attribute → tier → credit mapping with verified GraphQL types. Companion to [`ENIGMA_CANONICAL_REFERENCE.md`](ENIGMA_CANONICAL_REFERENCE.md).

> **Version:** Updated 2026-04-16 using verified schema details from the now-populated `enigma/08-reference/06-objects/*.md` files (previously placeholders).
>
> **Source of truth:**
> - Tier assignments: `enigma/04-resources/03-pricing-and-credit-use.md` (`_schemaExtended` introspection summary).
> - GraphQL types: `enigma/08-reference/06-objects/*.md` (180 files fetched from `documentation.enigma.com`).
> - Per-attribute detail: `enigma/09-data-attributes/{01-brand,02-operating-location,03-legal-entity}/*.md`.
>
> **Pricing:** Free = 0 credits, Core = 1, Plus = 3, Premium = 5 per entity. Highest-tier-wins per entity.
>
> **Programmatic lookup:** Run `_schemaExtended { types { name pricingTier fields { name pricingTier } } }` against `https://api.enigma.com/graphql` for live tier assignments.

---

## Brand

**GraphQL type:** `Brand`. Implements `NodeFunctions`, `Entity`. Member of `SearchUnion`.

| Attribute (connection field) | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|
| `name` | `BrandName` (via `BrandNameConnection`, default `first: 3`) | Core | 1 | Customer-facing brand name; ranked by dataset quality + frequency. |
| `address` (via `operatingLocations.addresses`) | `Address` | Core | 1 | USPS Pub 28 address (street, city, state, zip, county, MSA, CSA, lat/lng, h3Index). |
| `addressDeliverability` | `AddressDeliverability` | Plus | 3 | USPS deliverability, RDI, CMRA virtual flag, delivery type. |
| `activities` | `BrandActivity` (via `BrandActivityConnection`, default `first: 3`) | Plus | 3 | Compliance-risk activity classification (Cannabis, Firearms, Tobacco, Gambling, MLM, etc.). ~130K classified brands. |
| `locationDescriptions` | `BrandLocationDescription` (via `BrandLocationDescriptionConnection`, default `first: 3`) | Core | 1 | Geographic summary — top 5 states or specific city/state. |
| `revenueQualities` | `BrandRevenueQuality` (via `BrandRevenueQualityConnection`, default `first: 3`) | Plus | 3 | Revenue anomaly flags (zero-drop, 20% decrease, 250% increase); High/Medium severity. |
| `cardTransactions` | `BrandCardTransaction` (via `BrandCardTransactionConnection`, default `first: 3`) | Plus | 3 | 1m/3m/12m revenue metrics; 8 quantity types; raw + projected. |
| `emailAddresses` (via `roles.emailAddresses`) | `EmailAddress` | Core | 1 | Email. Primarily available via file delivery (Contacts attribute), not API. |
| `industries` | `Industry` (via `BrandIndustryConnection`, default `first: 100`) | Core | 1 | NAICS 2017/2022, SIC, MCC, GICS, Enigma descriptions. |
| `isMarketables` | `BrandIsMarketable` (via `BrandIsMarketableConnection`, default `first: 3`) | Core | 1 | Boolean: open locations + recent revenue + recent reviews. |
| `onlinePresence` (via `websites.onlinePresences`) | `WebsiteOnlinePresence` | Core | 1 | `hasOnlineSales`, `hasOnlinePayments` (Yes / null). |
| `phoneNumbers` (via `operatingLocations.phoneNumbers` or `roles.phoneNumbers`) | `PhoneNumber` | Core | 1 | 12-digit NANP (`"+1"` + 11 digits). |
| `registeredEntities` (via `legalEntities.registeredEntities`) | `RegisteredEntity` | Premium | 5 | Standardized name, type, formation date/year. |
| `registrations` (via `legalEntities.registeredEntities.registrations`) | `Registration` | Premium | 5 | SoS filing: file number, dates, status, sub_status, status_detail. |
| `roles` | `Role` (via `BrandRoleConnection`, default `first: 100`) | Plus | 3 | People/entities holding roles at the business. |
| `technologiesUseds` (via `websites.technologiesUseds`) | `WebsiteTechnologiesUsed` | Premium | 5 | Adyen, Braintree, PayPal, Shopify, Stripe. |
| `txnMerchants` | `TxnMerchant` | Plus | 3 | Card-network merchant identifiers tied to the brand. |
| `watchlistEntries` (via `legalEntities.*`) | `WatchlistEntry` | Premium | 5 | OFAC SDN + Consolidated Sanctions list entries. |
| `websites` | `Website` (via `BrandWebsiteConnection`, default `first: 100`) | Core | 1 | URL with domain, subdomain, TLD, path, fragment. |
| `websiteContents` (via `websites.websiteContents`) | `WebsiteContent` | Plus | 3 | Crawl state (HTTP status, favicon); crawled ≥ every 90 days. |

**Scalar fields on Brand object:** `id: ID!`, `internalId: String`, `enigmaId: String`, `tieBreakerMetadata: BrandTieBreakerMetadata`, `searchMetadata: Searchmetadata`, plus 10 `NodeFunctions` aggregation functions (`count`, `countDistinct`, `has`, `sum`, `min`, `max`, `avg`, `collect`, `minDateTime`, `maxDateTime`) and `_fn: JSON`.

---

## Operating Location

**GraphQL type:** `OperatingLocation`. Implements `NodeFunctions`, `Entity`. Member of `SearchUnion`.

| Attribute (connection field) | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|
| `names` | `OperatingLocationName` (via `OperatingLocationNameConnection`, default `first: 3`) | Core | 1 | Location-specific name (e.g., "Target - Crossgates Mall"). |
| `addresses` | `Address` (via `OperatingLocationAddressConnection`, default `first: 100`) | Core | 1 | USPS-standard address. |
| `addressDeliverabilities` (via `addresses.*`) | `AddressDeliverability` | Plus | 3 | USPS deliverability, CMRA virtual flag. |
| `cardTransactions` | `OperatingLocationCardTransaction` (via `OperatingLocationCardTransactionConnection`, default `first: 3`) | Plus | 3 | Raw + projected metrics; 1m/3m/12m periods; 8 quantity types. |
| `emailAddresses` (via `roles.emailAddresses`) | `EmailAddress` | Core | 1 | Email — file delivery only. |
| `isMarketables` | `OperatingLocationIsMarketable` (via `OperatingLocationIsMarketableConnection`, default `first: 3`) | Core | 1 | Boolean marketability. |
| `locationTypes` | `OperatingLocationLocationType` (via `OperatingLocationLocationTypeConnection`, default `first: 3`) | Core | 1 | retail, office, HQ, hospitality, medical, etc. (15+ values). |
| `operatingStatuses` | `OperatingLocationOperatingStatus` (via `OperatingLocationOperatingStatusConnection`, default `first: 3`) | Core | 1 | Open / Temporarily Closed / Closed / Unknown. |
| `onlinePresences` (via `websites.onlinePresences`) | `WebsiteOnlinePresence` | Core | 1 | E-commerce indicator. |
| `phoneNumbers` | `PhoneNumber` (via `OperatingLocationPhoneNumberConnection`, default `first: 100`) | Core | 1 | 12-digit string. |
| `ranks` | `OperatingLocationRank` (via `OperatingLocationRankConnection`, default `first: 3`) | Plus | 3 | Card-revenue rank within H3 res-4 cell + same Enigma industry; needs ≥10 nearby same-industry businesses. |
| `revenueQualities` | `OperatingLocationRevenueQuality` (via `OperatingLocationRevenueQualityConnection`, default `first: 3`) | Plus | 3 | Revenue anomaly flags with High/Medium severity. |
| `registeredEntities` (via `legalEntities.registeredEntities`) | `RegisteredEntity` | Premium | 5 | Linked via Location→LegalEntity→RegisteredEntity. |
| `registrations` (via `legalEntities.registeredEntities.registrations`) | `Registration` | Premium | 5 | Per-state SoS registration. |
| `reviewSummaries` | `ReviewSummary` (via `OperatingLocationReviewSummaryConnection`, default `first: 100`) | Plus | 3 | Review counts, score avg, first/last review date. |
| `roles` | `Role` (via `OperatingLocationRoleConnection`, default `first: 100`) | Plus | 3 | Roles held by people/entities. |
| `technologiesUseds` | `OperatingLocationTechnologiesUsed` (via `OperatingLocationTechnologiesUsedConnection`, default `first: 3`) | Premium | 5 | Clover, PayPal, Shopify, Square, Stripe, Toast. |
| `watchlistEntries` (via `legalEntities.*`) | `WatchlistEntry` | Premium | 5 | OFAC lists. |
| `websites` | `Website` (via `OperatingLocationWebsiteConnection`, default `first: 100`) | Core | 1 | URL with decomposed parts. |
| `websiteContents` (via `websites.websiteContents`) | `WebsiteContent` | Plus | 3 | Website crawl state. |

**Scalar fields:** `id: ID!`, `internalId: String`, `enigmaId: String`, `tieBreakerMetadata: OperatingLocationTieBreakerMetadata`, `searchMetadata: Searchmetadata`, plus `NodeFunctions` aggregation functions and `_fn: JSON`.

---

## Legal Entity

**GraphQL type:** `LegalEntity`. Implements `NodeFunctions`, `Entity`. Member of `SearchUnion`.

| Attribute (connection field) | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|
| `names` | `LegalEntityName` (via `LegalEntityNameConnection`, default `first: 3`) | Free | 0 | Legal entity name (+ full-text search vector). |
| `types` | `LegalEntityType` (via `LegalEntityTypeConnection`, default `first: 3`) | Free | 0 | Person, Corporation, LLC, LP, Non-profit, Professional Corporation, etc. |
| `addresses` | `Address` (via `LegalEntityAddressConnection`, default `first: 100`) | Core | 1 | Types: site, registered, mailing, registered_agent_address, registered_business_address. |
| `addressDeliverabilities` (via `addresses.*`) | `AddressDeliverability` | Plus | 3 | USPS deliverability. |
| `bankruptcies` | `LegalEntityBankruptcy` (via `LegalEntityBankruptcyConnection`, default `first: 3`) | Premium | 5 | Federal bankruptcy filings (Ch 7/11/12/13/15) from PACER. Add-on. |
| `emailAddresses` (via `roles.emailAddresses` or `persons.*`) | `EmailAddress` | Core | 1 | Email — file delivery only. |
| `phoneNumbers` (via `roles.phoneNumbers`) | `PhoneNumber` | Core | 1 | 12-digit NANP (`"+1"` + 11 digits). 60%/69% coverage. |
| `persons` | `Person` (via `LegalEntityPersonConnection`, default `first: 100`) | Core | 1 | Natural persons linked to this entity (officers, registered agents, etc.). |
| `registeredEntities` | `RegisteredEntity` (via `LegalEntityRegisteredEntityConnection`, default `first: 100`) | Premium | 5 | Standardized name, `registeredEntityType`, `formationDate`, `formationYear`. |
| `registrations` (via `registeredEntities.registrations`) | `Registration` | Premium | 5 | Domestic/foreign SoS registration + status fields. |
| `roles` | `Role` (via `LegalEntityRoleConnection`, default `first: 100`) | Plus | 3 | 44% coverage. |
| `tins` | `Tin` (via `LegalEntityTinConnection`, default `first: 100`) | Premium | 5 | TIN with `tinType` (EIN/SSN/ITIN/ATIN/PTIN) and `validity` (`issued`/`not_issued`/`invalid`/null). |
| `isFlaggedByWatchlistEntries` | `WatchlistEntry` (via `LegalEntityIsFlaggedByWatchlistEntryConnection`, default `first: 100`) | Premium | 5 | This entity triggered a watchlist match. |
| `appearsOnWatchlistEntries` | `WatchlistEntry` (via `LegalEntityAppearsOnWatchlistEntryConnection`, default `first: 100`) | Premium | 5 | This entity appears as the sanctioned party. |
| `brands` | (relation to Brand) `LegalEntityBrandConnection`, default `first: 100` | — | (billed at connected Brand's tier) | Owning/operating brand relationship. |
| `operatingLocations` | (relation to OperatingLocation) `LegalEntityOperatingLocationConnection`, default `first: 100` | — | (billed at connected location's tier) | Responsible-for relationship. |
| `legalEntities` | `LegalEntityLegalEntityConnection`, default `first: 100` | Free | 0 | Related legal entities (parent/subsidiary). |

**Scalar fields:** `id: ID!`, `internalId: String`, `enigmaId: String`, `tieBreakerMetadata: LegalEntityTieBreakerMetadata`, `searchMetadata: Searchmetadata`, plus `NodeFunctions` aggregation functions and `_fn: JSON`.

---

## Person

**GraphQL type:** `Person`. Implements `NodeFunctions`, `Entity`. Member of `SearchUnion`.

| Attribute | GraphQL Type | Tier | Credits | Description |
|---|---|---|---|---|
| `firstName` | `String` (via `PersonName` object, Core tier) | Core | 1 | First name. |
| `lastName` | `String` | Core | 1 | Last name. |
| `fullName` | `String` | Core | 1 | Full name. |
| `dateOfBirth` | `String` (YYYY-MM-DD) | Core | 1 | Date of birth. |
| `personId` | `String` | Core | 1 | Unique ID. |
| `names` | `PersonNameConnection` (default `first: 3`) | Core | 1 | Connection to person name records. |
| `legalEntities` | `PersonLegalEntityConnection` (default `first: 100`) | Free | 0 | Connection to related legal entities. |

**Scalar fields on Person object:** `id: ID!`, `internalId: String`, `enigmaId: String`, `tieBreakerMetadata: String` (note: String, unlike other entities' typed TieBreakerMetadata), `searchMetadata: Searchmetadata`, plus `NodeFunctions` aggregation functions and `_fn: JSON`.

---

## Address-as-Entity

The `Address` type is one of the values in the `EntityType` enum and can be returned directly. **Core tier (1 credit).**

| Field | Type | Description |
|---|---|---|
| `streetAddress1` | `String` | Primary street line. |
| `streetAddress2` | `String` | Apt/suite/floor. |
| `city` | `String` | City. |
| `county` | `String` | County. |
| `state` | `String` | State abbreviation. |
| `zip` | `String` | ZIP code. |
| `country` | `String` | ISO-3 country code. |
| `csa` | `String` | Combined Statistical Area. |
| `msa` | `String` | Metropolitan/Micropolitan Statistical Area. |
| `latitude` | `Float` | Latitude. |
| `longitude` | `Float` | Longitude. |
| `h3Index` | `String` | H3 geospatial index (resolution 10). |
| `fullAddress` | `String` | Complete formatted address. |
| `type` | `String` | `site` / `registered` / `mailing` / `registered_agent_address` / `registered_business_address` (in Legal Entity context). |
| `id` | `UUID!` | Unique identifier. |
| `firstObservedDate` | `String` | First observation date. |
| `lastObservedDate` | `String` | Last observation date. |

Companion `AddressDeliverability` is **Plus (3 credits)**:

- `deliverable` ∈ {`deliverable`, `vacant`, `not_deliverable`, null}
- `deliveryType` ∈ {street, multi-tenant building, post office box, firm, rural route or highway contract route, general delivery, null}
- `rdi` ∈ {`Residential`, `Commercial`}
- `virtual` ∈ {`virtual_cmra`, `not_virtual`, null}

---

## Supporting Types with Verified Fields

### Registration (Premium)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `registrationType` | `String` | Legal form as given by registering jurisdiction's SoS. |
| `expirationDate` | `Date` | Optional. |
| `registrationState` | `String` | US state where filed. |
| `jurisdictionType` | `String` | `domestic` or `foreign`. |
| `homeJurisdictionState` | `String` | Two-letter state code. |
| `registeredName` | `String` | Business name on filing. |
| `fileNumber` | `String` | Filing number. |
| `issueDate` | `Date` | YYYY/MM/DD. |
| `status` | `String` | `active` / `inactive` / `unknown`. |
| `subStatus` | `String` | `good_standing`, `not_good_standing`, `pending_active`, `pending_inactive`, `unknown`, null. |
| `statusDetail` | `String` | Official state message. |
| `firstObservedDate`, `lastObservedDate`, `internalId`, `internalRegistrationId` | — | — |

Connections: `addresses`, `roles`, `registeredEntities`. Identify package returns a restricted subset (no status fields); Verify package returns all.

### RegisteredEntity (Premium)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `name` | `String` | Standardized from registrations. |
| `registeredEntityType` | `String` | Standardized legal form. |
| `formationDate` | `Date` | Earliest non-null issue date (YYYY-MM-DD). |
| `formationYear` | `Int` | Year. |

### Tin (Premium)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `tin` | `String` | 9-digit IRS ID. |
| `tinType` | `String` | `EIN`, `SSN`, `ITIN`, `ATIN`, or `PTIN` (currently EIN only). |
| `validity` | `String` | `issued`, `not_issued`, `invalid`, or null. |

Connection: `legalEntities` (`TinLegalEntityConnection`).

### WatchlistEntry (Premium)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `watchlistName` | `String` | SDN or Non-SDN variant. |

**Dual connections:**
- `legalEntitiesIsFlaggedBy: WatchlistEntryIsFlaggedByLegalEntityConnection` — entities that triggered a match.
- `legalEntitiesAppearsOn: WatchlistEntryAppearsOnLegalEntityConnection` — entities named by the watchlist entry itself.
- `addresses: WatchlistEntryAddressConnection`.

### Role (Plus)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `jobTitle` | `String` | Lowercased, expanded abbreviations, accents removed. |
| `jobFunction` | `String` | Standardized (e.g., "Accounting", "Contracts"). |
| `managementLevel` | `String` | Governance: owner, founder, board of directors. Functional: head, c-suite, director-level, vp-level, manager, non-manager. Or null. |
| `externalId` | `JSON` | — |
| `externalUrl` | `String` | — |

Connections: `operatingLocations`, `phoneNumbers`, `emailAddresses`, `legalEntities`, `registrations`, `brands` (6 total). 44% coverage at business and location level.

### PhoneNumber (Core)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `phoneNumber` | `String` | 12-digit NANP: `"+1"` + area code (3) + exchange (3) + line (4). Must have valid U.S. area code. |

Connections: `operatingLocations`, `roles`.

### Website (Core)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `website` | `String` | Complete URL with protocol, subdomain, path. |
| `domain` | `String` | e.g., "enigma" in `documentation.enigma.com`. |
| `subdomain` | `String` | e.g., "documentation". |
| `topLevelDomain` | `String` | e.g., "com". |
| `path` | `String` | URL path. |
| `fragment` | `String` | Anchor/hash. |

Connections: `brands`, `operatingLocations`, `websiteContents`, `technologiesUseds`, `onlinePresences`.

### Industry (Core)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `industryDesc` | `String` | Human-readable description. |
| `industryCode` | `String` | Numeric code (null for enigma_industry_description). |
| `industryType` | `String` | `naics_2017_code`, `naics_2022_code`, `sic_code`, `mcc_code`, `enigma_industry_description`. |

Connections: `brands`, `parentIndustries` (hierarchy).

### EmailAddress (Core)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `emailAddress` | `String` | — |

Connection: `roles` (`EmailAddressRoleConnection`).

> **Note:** Emails primarily come via the Contacts attribute (file delivery). Not fully available via API.

### ReviewSummary (Plus)

| Field | Type | Notes |
|---|---|---|
| `id` | `UUID!` | — |
| `reviewCount` | `Int` | Total review count. |
| `reviewScoreAvg` | `Float` | Weighted average. |
| `firstReviewDate` | `String` | From sample of 100 reviews. |
| `lastReviewDate` | `String` | May lag up to 3 months. |

Connection: `operatingLocations`.

### LegalEntityBankruptcy (Premium)

Fields include `chapterType` (7/11/12/13/15), `caseNumber`, `petition` (voluntary/involuntary), `filingDate`, `entryDate`, `dateConverted`, `dateDismissed`, `dateTerminated`, `debtorDischargedDate`, `planConfirmedDate`, `debtorName`, `judge`, `trustee`. PACER-sourced. 100% coverage at business and location level; history to the 1980s. Sales-team activation required.

### OperatingLocationCache (provisional — no upstream page)

Per `enigma/08-reference/06-objects/OperatingLocationCache.md` (provisional stub), likely fields:

- `operatingLocationId` (likely `ID!` / `String!`)
- `brandId` (likely `ID` / `String`)
- `latitude` (likely `Float`)
- `longitude` (likely `Float`)
- `latest12mCardRevenueProjected` (likely numeric scalar)

Types/nullability unverified. Not referenced from other documented types. **Confirm via schema introspection before use.**

---

## CardTransaction Quantity Types

For `BrandCardTransaction` (Plus) and `OperatingLocationCardTransaction` (Plus):

| Quantity Type | Meaning |
|---|---|
| `card_revenue_amount` | Sum of all transaction amounts in dollars. |
| `card_transactions_count` | Total number of card transactions. |
| `avg_transaction_size` | Average transaction size in dollars. |
| `card_customers_average_daily_count` | Average unique daily customers. |
| `card_revenue_yoy_growth` | Current period revenue / one year prior. |
| `card_revenue_prior_period_growth` | Current period revenue / previous period. |
| `refunds_amount` | Total refunds in dollars (negative). |
| `has_transactions` | 1 if any txns in period, else 0. |

Period values: `1m`, `3m`, `12m`. Each record has `periodStartDate`, `periodEndDate`, `rawQuantity` (unscaled), `projectedQuantity` (scaled by panel multiplier based on geography/industry/size).

---

## Common Fields on Every Attribute Object

Every attribute object includes these standard fields (no separate billing):

| Field | Type | Description |
|---|---|---|
| `id` | `UUID!` | Unique identifier for this attribute observation. |
| `firstObservedDate` | `String` | Date first observed. |
| `lastObservedDate` | `String` | Date last observed. |
| `internal<Type>Id` | `String` | Internal identifier (each type has its own). |

---

## Standard Connection Arguments

Every Connection field on every entity accepts:

- `first: Int` — forward pagination count.
- `last: Int` — backward pagination count.
- `after: String` — cursor (exclusive), requires `first`.
- `before: String` — cursor (exclusive), requires `last`.
- `conditions: ConnectionConditions` — `{filter, orderBy}`.

Default `first` values differ by connection (typically 3 for metadata/rank-like connections, 100 for multi-record connections).

---

## Tier Notes & Caveats

1. **Pricing is per-entity.** The highest tier among returned attributes determines the cost for that entity.
2. **Free tier = 0 credits.** Only `LegalEntityName` and `LegalEntityType` qualify.
3. **Tier values can change.** Per Enigma: "Attribute pricing tiers are subject to change. Refer to the attribute tier page or run Enigma's GraphQL introspection to get the latest attribute tier assignments."
4. **Connection wrapper types** (`*Connection`, `*Edge`) don't carry their own tier — they wrap the underlying typed attribute, which is billed at its own tier.
5. **`Actions` credit category** (Billing page) is separate from attribute-read billing and covers operational tasks like list materializations.
6. **`Person.tieBreakerMetadata` is `String`**, unlike Brand/LegalEntity/OperatingLocation which have typed `<Type>TieBreakerMetadata` objects.
7. **`Mutation` fields** (createList, updateList, deleteList, createListMaterialization, cancelListMaterialization, createSuggestion) are exposed via the `ExternalMutation` type, typically accessed as `externalMutation` on the `Mutation` root. Billing for list mutations falls under the `Actions` credit category.
8. **`WatchlistEntry` has dual legal-entity connections** — always check both `legalEntitiesIsFlaggedBy` and `legalEntitiesAppearsOn` for complete coverage.

---

*End of attribute tier map.*

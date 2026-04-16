# Enigma Canonical Reference

This document is a primary-source reference for the Enigma platform, covering the data model, the three API surfaces (GraphQL, KYB REST, Screening REST), the MCP server, the credit / pricing system, and per-entity attribute coverage.

All material is sourced from the Enigma documentation files under `enigma/` (scraped from Enigma's official documentation site). Each section cites the source files it draws from. Anything not directly stated in the source docs is marked `[inferred]` or `[not documented]`.

> **Source root:** `enigma/` (this repo)
> **Online source root:** `https://documentation.enigma.com/`

---

## Table of Contents

1. [Data Model](#1-data-model)
2. [GraphQL API](#2-graphql-api)
3. [Credit System](#3-credit-system)
4. [Entity Attributes Reference](#4-entity-attributes-reference)
5. [KYB Verification](#5-kyb-verification)
6. [Screening & Compliance](#6-screening--compliance)
7. [MCP Server](#7-mcp-server)
8. [Practical Query Patterns](#8-practical-query-patterns)
9. [Known Challenges & Gotchas](#9-known-challenges--gotchas)

---

## 1. Data Model

> Sources: `enigma/01-getting-started/01-overview.md`, `enigma/01-getting-started/02-the-enigma-data-model.md`, `enigma/04-resources/01-how-enigma-searches-and-matches.md`

Enigma's `graph-model-1` data is built on three core entity types plus a connected Person entity. Entities and relationships are created when Enigma observes activity from a business in real-world records.

### 1.1 Three Core Entity Types

| Entity | Definition | Example |
|---|---|---|
| **Brand** | How a business presents itself to customers (trade names, logos, marketing identities). | "Starbucks" — the global brand customers know. |
| **Legal Entity** | How a business is recognized by governments and regulatory bodies (taxation, compliance, legal accountability). | "Starbucks Corporation" — the entity that pays taxes and files with regulators. |
| **Operating Location** | A physical or virtual space where a business interacts with customers or conducts activity. Connects brands to legal entities and grounds them in specific places. | A single Starbucks store at 123 Main St. |

A brand may operate across many locations, be owned by one or more legal entities, and coexist with sister brands under a shared corporate structure. A legal entity may own multiple brands or operate many locations.

### 1.2 Person as a Connected Entity

A `Person` is one of the entity types in the `EntityType` enum (alongside `BRAND`, `OPERATING_LOCATION`, `LEGAL_ENTITY`, `ADDRESS`). People are connected to businesses through `Role` records (job title, function, management level, department). In KYB responses, persons appear nested inside `registrations` with `name` and `titles` (e.g., `chief executive officer`, `registered agent`).

> Source: `enigma/08-reference/02-enums/EntityType.md`, `enigma/02-verification-and-kyb/04-kyb-response-matched-data.md`

### 1.3 Registered Entity vs. Legal Entity

Per the data attribute docs (`enigma/09-data-attributes/03-legal-entity/07-registered-entity.md`):

- A **Legal Entity** is the abstract entity recognized by U.S. law as having identity and rights — natural persons or artificial entities.
- A **Registered Entity** is a specific legal entity that has formally registered with one or more U.S. Secretaries of State (SoS). The `RegisteredEntity` object captures the standardized name, entity type, and earliest formation date drawn from those registrations.

In the KYB v2 response, `registered_entities` (renamed from `legal_entities` in v1) is the array that returns these registration-grounded entities.

> Source: `enigma/04-resources/05-upgrade-from-kyb-v1-to-v2.md`

### 1.4 Relationships Between Entities

The model captures three primary relationships:

- **Brand-to-Location** — which brands operate at which locations.
- **Brand-to-Legal Entity** — which legal entities own or manage a brand.
- **Location-to-Legal Entity** — which legal entities are responsible for specific operating locations.

These links allow holistic search: you can search for a Brand using the address of one of its Operating Locations, or for a Legal Entity using the brand name it operates under.

### 1.5 Entity Hierarchy (KYB Response Shape)

The KYB v2 response surfaces the data model as a nested structure:

```
registered_entities[]
  ├── registrations[]
  │     ├── persons[]
  │     └── addresses[]
brands[]
  ├── industries[]
  └── operating_locations[]
        └── address
```

> Source: `enigma/02-verification-and-kyb/04-kyb-response-matched-data.md`

### 1.6 The Complex Nature of Businesses

The data model is built to capture real-world complexity:
- Multi-entity corporations (Gap Inc. → Old Navy, Banana Republic)
- Affiliated brands (dealers like "Curry Honda", co-locations like "Sephora at JCPenney")
- Franchises (independent operators under a shared brand — McDonald's, Dairy Queen)
- Agents and professionals ("James Lavelle, State Farm Agent")
- Medical providers (individual doctors within larger health systems)
- People as brands (hairstylists, therapists)
- Legal entities used as brands (when no separate trade name exists)

---

## 2. GraphQL API

> Sources: `enigma/06-query-enigma-with-graphql/01-graphql-api-quickstart.md`, `02-search-and-get-data-via-api.md`, `03-get-aggregate-location-counts.md`, `05-directives.md`, `06-response-status-codes.md`, `07-graphql-api-rate-limits.md`, `enigma/04-resources/02-rate-limits.md`, `enigma/08-reference/03-inputs/SearchInput.md`, `Conditions.md`, `ConnectionConditions.md`, `enigma/08-reference/02-enums/EntityType.md`, `OutputFormat.md`, `TinType.md`, `enigma/08-reference/06-objects/BackgroundTask.md`, `enigma/08-reference/07-queries/search.md`

### 2.1 Endpoint and Authentication

- **Endpoint:** `POST https://api.enigma.com/graphql`
- **Body:** Standard GraphQL conforming to the [GraphQL Specification (October 2021)](https://spec.graphql.org/October2021/).
- **Authentication header:** `x-api-key: YOUR_API_KEY`

### 2.2 Top-Level Queries

| Query | Returns | Purpose |
|---|---|---|
| `search(searchInput: SearchInput!)` | `[SearchUnion]` | Discover and retrieve entities. |
| `aggregate(searchInput: SearchInput!)` | Aggregated counts | Count operating locations and their associated brands or legal entities. |
| `backgroundTask(id: UUID!)` | `BackgroundTask` | Poll an asynchronous task created by a segmentation search. |
| `account` | Account info | Account information. |
| `listMaterialization` | List materialization status | List/segment workflow. |

Mutations (from `enigma/08-reference/05-mutations/`): `cancelListMaterialization`, `createList`, `createListMaterialization`, `createSuggestion`, `deleteList`, `updateList`, `updateListMaterialization`.

### 2.3 SearchInput

`SearchInput` is the required input for `search` and `aggregate`.

| Field | Type | Description |
|---|---|---|
| `prompt` | String | Natural-language description of the business (e.g., "fast food", "pizza restaurant", "mexican restaurant in new york"). **Only supported for `entityType: BRAND`.** |
| `id` | String | Entity ID. Takes precedence over all other input fields. Use with `entityType` to specify which entity the ID belongs to. |
| `name` | String | The name of the business (e.g., "McDonald's"). |
| `address` | `AddressInput` | Single address with `id`, `street1`, `street2`, `city`, `state`, `postalCode`. |
| `addresses` | `[AddressInput]` | Multiple addresses. Either `address` or `addresses` can be specified, not both. **Only supported for `aggregate`.** |
| `person` | `PersonInput` | `firstName`, `lastName`, `dateOfBirth` (ISO 8601 YYYY-MM-DD), `address`, `tin` (if `tin` is provided, `firstName` and `lastName` must also be specified). |
| `phoneNumber` | String | 10-digit U.S. phone in `##########` or `###-###-####` format. |
| `website` | String | A website URL (`enigma.com`, `www.enigma.com`, `https://www.enigma.com/` all accepted). |
| `tin` | `TinInput` | Business TIN. The `name` field must also be provided. |
| `conditions` | `Conditions` | Filter / orderBy / limit / pageToken. |
| `matchThreshold` | Float | Confidence threshold the result must meet, 0.0–1.0. |
| `entityType` | `EntityType` | Entity type to search for. Defaults to `BRAND`. |
| `output` | `OutputSpec` | If specified, the result is delivered as a background task instead of being returned inline. |
| `fields` | `[SearchFieldGroupInput]` | Structured search field groups. |
| `engine` | String | Search engine selection. |
| `enrichmentIdsS3Path` | String | "S3 path to parquet file containing internal_id column for filtering". |

Every search must include at least one of: business name, website, or person first/last name. (`enigma/04-resources/01-how-enigma-searches-and-matches.md`)

### 2.4 EntityType Enum

```graphql
enum EntityType {
  BRAND
  OPERATING_LOCATION
  LEGAL_ENTITY
  PERSON
  ADDRESS
}
```

The `entityType` parameter changes which type of entity is returned. Note: `prompt` search requires `BRAND`; `aggregate` requires `OPERATING_LOCATION`.

### 2.5 matchThreshold

A floating-point confidence threshold (0.0–1.0) that the match must meet. The docs note that based on labeled evaluation data, Enigma's search precision is approximately 94% across all three entity types — actual precision depends on input completeness.

> Practical guidance from source: "Optimized for precision: When there isn't enough evidence to suggest a good match, the system returns no result — in order to avoid false positives." (`enigma/04-resources/01-how-enigma-searches-and-matches.md`)

### 2.6 AddressInput

```graphql
input AddressInput {
  id: ID
  street1: String
  street2: String
  city: String
  state: String
  postalCode: String
}
```

### 2.7 PersonInput and TinInput

```graphql
input PersonInput {
  firstName: String
  lastName: String
  dateOfBirth: String      # ISO 8601 (YYYY-MM-DD)
  address: AddressInput
  tin: TinInput
}

input TinInput {
  tin: String
  tinType: TinType         # EIN, SSN, ITIN, TIN
}
```

### 2.8 Conditions and ConnectionConditions

`Conditions` (used inside `SearchInput`):

| Field | Type | Description |
|---|---|---|
| `filter` | JSON | Filtering criteria (see operators below). |
| `orderBy` | `[String]` | Sort expressions (e.g., `["name DESC", "city ASC"]`). |
| `limit` | Int | Max top-level results. |
| `pageToken` | String | Numeric offset as a string (e.g., `"8"` starts from the 8th result). |

`ConnectionConditions` (used on connection-based fields like `cardTransactions`, `operatingLocations`):

| Field | Type | Description |
|---|---|---|
| `filter` | JSON | Same operators as `Conditions.filter`. |
| `orderBy` | `[String]` | Same orderBy semantics. |

### 2.9 Filter Operators

Source: `enigma/06-query-enigma-with-graphql/02-search-and-get-data-via-api.md`

| Operator | Args | Description |
|---|---|---|
| `EQ` | 2 | Equals. `{EQ: ["name", "McDonald's"]}` |
| `NE` | 2 | Not equals. |
| `GT` / `GTE` | 2 | Greater than / greater than or equal. |
| `LT` / `LTE` | 2 | Less than / less than or equal. |
| `IN` | 2 | Value in list. `{IN: ["operatingStatus", ["Open", "Closed"]]}` |
| `NOT_IN` | 2 | Value not in list. |
| `LIKE` | 2 | Case-sensitive SQL-style match. `%` is the wildcard. |
| `ILIKE` | 2 | Case-insensitive SQL-style match. |
| `AND` | ≥2 | Logical AND of nested expressions. |
| `OR` | ≥2 | Logical OR of nested expressions. |
| `NOT` | 1 | Logical negation of a nested expression. |
| `ADD` / `SUB` / `MUL` / `DIV` | 2 | Arithmetic on a numeric field. |
| `HAS` | 1 | Field is present. `{HAS: ["roles.emailAddresses"]}` |
| `IS_NULL` | 1 | Field is null. |
| `IS_NOT_NULL` | 1 | Field is not null. |

**Field paths use dot notation** for nested fields: `operatingStatuses.operatingStatus`, `addresses.state`, `cardTransactions.period`, `industries.industryType`.

### 2.10 orderBy

`orderBy` is a list of `"<field> [ASC|DESC]"` strings. The ordering applies only to the requested field. Multiple orderings are supported (`["streetAddress1 ASC", "city ASC"]`).

### 2.11 Math Functions (NodeFunctions)

Available on entity objects for aggregating related data:

| Function | Return | Parameters |
|---|---|---|
| `count` | Int | `field` (required), `conditions` (optional) |
| `sum` | Int | `field`, `conditions` |
| `min` | Int | `field`, `conditions` |
| `max` | Int | `field`, `conditions` |
| `avg` | Float | `field`, `conditions` |
| `collect` | String | `field`, `conditions`, `separator` (default `","`) |
| `minDateTime` | DateTime | `field`, `conditions` |
| `maxDateTime` | DateTime | `field`, `conditions` |

`field` uses dot notation (`websites`, `names.rank`, `operatingLocations.brands.id`). `collect` **must be output to a file** — `output` in `SearchInput` must be specified.

`Brand` also exposes `countDistinct` (Int) and `has` (Boolean). (`enigma/08-reference/06-objects/Brand.md`)

### 2.12 Directives

> Source: `enigma/06-query-enigma-with-graphql/05-directives.md`

Directives transform values within a query. Each is attached to a virtual `_fn` field. The first directive in a chain reads the input via `ref` (single dot-notation path) or `refs` (list of paths). Subsequent directives operate on the previous output.

| Directive | Args | Effect |
|---|---|---|
| `@coalesce` | `ref \| refs` | First non-null value. |
| `@compact` | `ref \| refs` | Removes null values from an array. |
| `@slice` | `start: Int`, `end: Int` (negatives allowed), plus `ref` | Subset of an array or string. |
| `@trim` | `ref \| refs` | Strips leading/trailing whitespace. |
| `@upper` | `ref \| refs` | Uppercases. |
| `@lower` | `ref \| refs` | Lowercases. |
| `@map` | `ref \| refs`, `field` | Extracts nested field from each array element. |
| `@join` | `ref \| refs`, `sep: String` (default `""`) | Joins array elements with separator. |
| `@include` | `if: Boolean!` | Standard GraphQL: include field/fragment when true. |
| `@skip` | `if: Boolean!` | Standard GraphQL: omit field/fragment when true. |

Directives are chained left-to-right; aliasing `_fn` (e.g., `displayLabel: _fn @coalesce(...) @upper`) gives the result a meaningful key.

### 2.13 Search Patterns

Four patterns supported by the `search` query:

1. **Text Search** — name, person info, address. Returns inline results.
2. **Lookup** — by entity `id`. Returns the matching entity.
3. **Prompt Search** — natural language (`prompt: "Mexican restaurants"`). Brand entity type only.
4. **Segmentation** — large async results via `output: { filename, format?, s3Path? }`. Returns `202 Accepted` and a background task ID.

> Source: `enigma/06-query-enigma-with-graphql/02-search-and-get-data-via-api.md`

### 2.14 Background Tasks (Segmentation Output)

Triggered by setting `output` on `SearchInput`. The response is `202 Accepted` with structure:

```json
{
  "extensions": {
    "backgroundTasks": [
      { "id": "...", "status": "PROCESSING" }
    ]
  },
  "data": { "search": null }
}
```

Poll with the `backgroundTask` query. Statuses:

| Status | Description | Terminal |
|---|---|---|
| `PROCESSING` | Currently executing. | No |
| `CANCELLED` | Aborted/cancelled. No result. | Yes |
| `FAILED` | Failed after possible retries. No result. | Yes |
| `SUCCESS` | Result is available (a list of pre-signed S3 URLs in `result`). | Yes |

The `BackgroundTask` object exposes (`enigma/08-reference/06-objects/BackgroundTask.md`): `id`, `apiKeyId`, `backgroundTaskType`, `status`, `args` (JSON), `result` (JSON), `progressPercentComplete` (Float), `progressMessage`, `lastError`, `executionAttempts`, `etag`, `createdTimestamp`, `updatedTimestamp`, `lastExecutionTimestamp`, `nextExecutionTimestamp`.

### 2.15 OutputSpec

```graphql
input OutputSpec {
  filename: String     # required when output is set
  format: OutputFormat # CSV or PARQUET
  s3Path: String       # if CSV: unique path to .csv. if PARQUET: directory.
}

enum OutputFormat { PARQUET CSV }
```

### 2.16 Pagination

Cursor-based, follows the [Relay Connection specification](https://relay.dev/graphql/connections.htm).

**Connection structure:**
- `edges[]` — each edge has `node` (data) and `cursor` (string position).
- `pageInfo` — `hasNextPage`, `hasPreviousPage`, `startCursor`, `endCursor`.

**Forward pagination:** `first` (count), `after` (cursor, exclusive).
**Backward pagination:** `last` (count), `before` (cursor, exclusive).

**Validation rules:**
- Cannot specify both `first` and `last` in the same query.
- `after` requires `first`.
- `before` requires `last`.
- All pagination parameters must be `>= 0`.

### 2.17 aggregate Query

> Source: `enigma/06-query-enigma-with-graphql/03-get-aggregate-location-counts.md`

Returns counts. Only supports `entityType: OPERATING_LOCATION`. The only filter supported is `{filter: {EQ: ["operatingStatuses.operatingStatus", "Open"]}}`.

Allowed `count(field: ...)` values: `brand`, `operatingLocation`, `legalEntity`.

```graphql
query Aggregate {
  aggregate(searchInput: { entityType: OPERATING_LOCATION, address: { city: "NEW YORK", state: "NY" } }) {
    brandsCount: count(field: "brand")
    operatingLocationsCount: count(field: "operatingLocation")
    legalEntitiesCount: count(field: "legalEntity")
  }
}
```

### 2.18 HTTP Response Status Codes

> Source: `enigma/06-query-enigma-with-graphql/06-response-status-codes.md`

| Status | Meaning |
|---|---|
| `200 OK` | Successful request. |
| `202 Accepted` | Asynchronous request — see segmentation. |
| `302 Found` | Responses over 6 MB are delivered via HTTP 302 to a pre-signed S3 URL in the `Location` header. |
| `400 Bad Request` | Invalid/unsupported input. Errors in body under `errors`. |
| `401 Unauthorized` | Missing `x-api-key` or the key is invalid/disabled. |
| `402 Payment Required` | Billing errors (e.g., insufficient credits). |

> The source doc only documents 2XX, 302, 400, 401, and 402. Other 4XX/5XX codes (including the documented `429 Slow Down` for rate limits) are referenced elsewhere — see Section 9.

### 2.19 GraphQL Rate Limits

> Sources: `enigma/04-resources/02-rate-limits.md`, `enigma/06-query-enigma-with-graphql/07-graphql-api-rate-limits.md`

All queries count toward the rate limit regardless of type.

| Plan | Rate Limit (RPS) | Burst | Daily (RPD) |
|---|---|---|---|
| Trial | 10 | 20 | 100,000 |
| Pro | 50 | 100 | 500,000 |
| Max | 50 | 100 | 500,000 |
| Enterprise | 100 | 200 | No limit |

Rate-limit response: `429 Slow Down`. GraphQL rate limits are independent of MCP tool rate limits and the KYB rate limit.

### 2.20 Error Shape

The source docs do not provide a detailed `errors[]` schema beyond noting that errors appear under the `errors` key in the response body for 400 responses. `[not documented in detail]`

---

## 3. Credit System

> Source: `enigma/04-resources/03-pricing-and-credit-use.md`

> Note from source: "Attribute pricing tiers are subject to change. Refer to the attribute tier page or run Enigma's GraphQL introspection to get the latest attribute tier assignments." (`https://www.enigma.com/pricing`)

### 3.1 Core Mechanics

- Credits are deducted from the billing account linked to your API key.
- The number of credits depends on the **type of attribute** requested and the data returned.
- **If the requested data is not returned, no credits are used.**
- **Requesting the same data multiple times incurs credits each time.** (No server-side caching.)

### 3.2 Highest-Tier-Wins Rule

If you request **multiple attributes for the same entity in a single query**, you are charged **once per entity, at the tier of the most expensive attribute** included in the response.

### 3.3 Pricing Tiers

Four tiers per the introspection-based summary in the source:

| Tier | Credits per entity |
|---|---|
| Free | 0 |
| Core | 1 |
| Plus | 3 |
| Premium | 5 |

(Credit-per-tier values are stated in the worked examples in the source: `core` → 1 credit, `plus` → 3 credits, `premium` → 5 credits.)

### 3.4 Tier Assignment Table

The tier assignments below are copied directly from the `_schemaExtended` introspection summary in `enigma/04-resources/03-pricing-and-credit-use.md`.

#### Free Tier

| Type | Key Fields |
|---|---|
| `LegalEntityName` | `name`, `legalEntityType`, `legalEntityId` |
| `LegalEntityType` | `type`, `legalEntityType`, `legalEntityId` |

#### Core Tier (1 credit)

| Type | Key Fields |
|---|---|
| `Address` | `streetAddress1`, `streetAddress2`, `city`, `state`, `zip`, `fullAddress`, `latitude`, `longitude`, `county`, `msa`, `csa`, `h3Index`, `rdi` |
| `BrandIsMarketable` | `isMarketable`, `brandId` |
| `BrandLocationDescription` | `locationDescription`, `brandId` |
| `BrandName` | `name`, `brandId` |
| `EmailAddress` | `emailAddress`, `emailAddressId` |
| `Industry` | `industryCode`, `industryDesc`, `industryType`, `industryId` |
| `OperatingLocationIsMarketable` | `isMarketable`, `operatingLocationId` |
| `OperatingLocationLocationType` | `locationType`, `operatingLocationId` |
| `OperatingLocationName` | `name`, `operatingLocationId` |
| `OperatingLocationOperatingStatus` | `operatingStatus`, `operatingLocationId` |
| `Person` | `firstName`, `lastName`, `fullName`, `dateOfBirth`, `personId` |
| `PhoneNumber` | `phoneNumber`, `areaCode`, `exchangeNumber`, `lineNumber`, `phoneNumberId` |
| `Website` | `website`, `domain`, `subdomain`, `topLevelDomain`, `path`, `websiteId` |
| `WebsiteOnlinePresence` | `hasOnlinePayments`, `hasOnlineSales`, `websiteId` |

#### Plus Tier (3 credits)

| Type | Key Fields |
|---|---|
| `AddressDeliverability` | `deliverable`, `deliveryType`, `rdi`, `virtual`, `addressId` |
| `BrandActivity` | `activityType`, `brandId` |
| `BrandCardTransaction` | `period`, `periodStartDate`, `periodEndDate`, `projectedQuantity`, `rawQuantity`, `quantityType`, `brandId` |
| `BrandRevenueQuality` | `issueDescription`, `issueReason`, `issueSeverity`, `brandId` |
| `OperatingLocationCardTransaction` | `period`, `periodStartDate`, `periodEndDate`, `projectedQuantity`, `rawQuantity`, `quantityType`, `operatingLocationId` |
| `OperatingLocationRank` | `position`, `cohortSize`, `period`, `periodStartDate`, `periodEndDate`, `quantityType`, `operatingLocationId` |
| `OperatingLocationRevenueQuality` | `issueDescription`, `issueReason`, `issueSeverity`, `operatingLocationId` |
| `ReviewSummary` | `reviewCount`, `reviewScoreAvg`, `firstReviewDate`, `lastReviewDate`, `reviewSummaryId` |
| `Role` | `jobTitle`, `jobFunction`, `managementLevel`, `roleId` |
| `TxnMerchant` | `name`, `merchantId`, `firstTransactionDate`, `lastTransactionDate`, `txnMerchantId` |
| `WebsiteContent` | `websiteAvailability`, `httpStatusCode`, `faviconUrl`, `faviconImage`, `websiteContentId` |

#### Premium Tier (5 credits)

| Type | Key Fields |
|---|---|
| `LegalEntityBankruptcy` | `chapterType`, `filingDate`, `caseNumber`, `debtorName`, `judge`, `trustee`, `legalEntityId` |
| `OperatingLocationTechnologiesUsed` | `technology`, `category`, `operatingLocationId` |
| `RegisteredEntity` | `name`, `registeredEntityType`, `formationDate`, `formationYear`, `registeredEntityId` |
| `Registration` | `registeredName`, `registrationState`, `jurisdictionType`, `homeJurisdictionState`, `fileNumber`, `issueDate`, `status`, `subStatus`, `statusDetail` |
| `Tin` | `tin`, `tinType`, `validity`, `tinId` |
| `WatchlistEntry` | `watchlistName`, `watchlistEntryId` |
| `WebsiteTechnologiesUsed` | `technology`, `category`, `websiteId` |

### 3.5 Programmatic Tier Lookup

Use the extended schema introspection query to fetch the live tier assignments:

```graphql
query GetSchemaExtended {
  _schemaExtended {
    types {
      name
      pricingTier
      fields {
        name
        pricingTier
      }
    }
  }
}
```

### 3.6 Worked Credit Examples

All examples below are **directly from `enigma/04-resources/03-pricing-and-credit-use.md`**.

**Single Attribute, Single Entity → 1 credit**
- `names` is Core; `conditions: {limit: 1}` returns one Brand. 1 entity × 1 credit (Core) = 1 credit.

**Single Attribute, Multiple Entities → 10 credits**
- `names` (Core), `conditions: {limit: 10}` → 10 entities × 1 credit = 10 credits.

**Multiple Attributes, Single Entity, Single Tier → 1 credit**
- `names` and `isMarketables` are both Core; `conditions: {limit: 1}` → 1 entity × 1 credit (highest tier = Core) = 1 credit.

**Multiple Attributes, Single Entity, Multiple Tiers → 6 credits**
- `names` (Core) + `txnMerchants` (Plus); `conditions: {limit: 2}` → 2 entities × 3 credits (highest tier = Plus) = 6 credits.

**Nested Entities → 51 credits**
- Brand's `names` (Core) → 1 credit for the brand.
- 10 OperatingLocations × (`names` Core + `cardTransactions` Premium = max Premium = 5 credits each) = 50 credits.
- **Total: 1 + 50 = 51 credits.**

### 3.7 Nested Entity Credit Compounding

Each level of the entity tree is billed separately at its highest-tier-wins rate. A query that traverses Brand → OperatingLocation → CardTransactions bills:
- The parent Brand once at its highest-tier attribute.
- Each child OperatingLocation once at its highest-tier attribute (which compounds with the count limit on that connection).

This produces non-obvious totals when child connections have large `first:` values combined with Premium-tier nested attributes.

---

## 4. Entity Attributes Reference

> Sources: all files under `enigma/09-data-attributes/01-brand/`, `02-operating-location/`, `03-legal-entity/`; `enigma/08-reference/06-objects/Brand.md`

### 4.1 Brand Attributes

| Attribute | GraphQL Type | Tier | Description |
|---|---|---|---|
| `name` | `BrandName` | Core | Customer-facing brand name; ranked by dataset quality and frequency. |
| `address` | `Address` | Core | Physical street address (USPS Pub 28 standard). Includes lat/lng, h3Index, MSA/CSA. |
| `addressDeliverability` | `AddressDeliverability` | Plus | USPS deliverability status, RDI, virtual (CMRA) flag. |
| `brandActivity` | `BrandActivity` | Plus | Notable activities (e.g., Cannabis). [Source file empty; tier from §3.4 table.] |
| `locationDescription` | `BrandLocationDescription` | Core | Geographic summary of the brand's footprint. |
| `revenueQuality` | `BrandRevenueQuality` | Plus | Revenue anomalies/issues (drops to zero, 20% decrease, 250% increase) with High/Medium severity. |
| `cardTransactions` | `BrandCardTransaction` | Plus | Card transaction metrics (8 quantity types) for 1m/3m/12m periods. |
| `emailAddress` | `EmailAddress` | Core | Email address for the business or associated person. |
| `industry` | `Industry` | Core | NAICS (2017, 2022), SIC, MCC, GICS, Enigma classifications. |
| `isMarketable` | `BrandIsMarketable` | Core | Boolean — open locations, recent revenue, recent reviews. |
| `onlinePresence` | `WebsiteOnlinePresence` | Core | "Yes" or null for online sales capability. |
| `phoneNumber` | `PhoneNumber` | Core | 12-digit string. |
| `registeredEntity` | `RegisteredEntity` | Premium | Legal entity formed via SoS registration. |
| `registration` | `Registration` | Premium | Per-state SoS registration with status fields. |
| `role` | `Role` | Plus | People/legal entities holding roles at the business. |
| `technologiesUsed` | `WebsiteTechnologiesUsed` | Premium | Web tech: Adyen, Braintree, PayPal, Shopify, Stripe. |
| `watchlistEntry` | `WatchlistEntry` | Premium | OFAC SDN + Consolidated Sanctions list entries. |
| `website` | `Website` | Core | URL with decomposed parts (domain, subdomain, TLD, path, fragment). |
| `websiteContent` | `WebsiteContent` | Plus | Website state at a point in time; crawled at minimum every 90 days. |

### 4.2 Operating Location Attributes

| Attribute | GraphQL Type | Tier | Description |
|---|---|---|---|
| `name` | `OperatingLocationName` | Core | Location-specific name (e.g., "Target - Crossgates Mall"). |
| `address` | `Address` | Core | USPS-standard physical address with geocoding fields. |
| `addressDeliverability` | `AddressDeliverability` | Plus | USPS deliverability + CMRA virtual flag. |
| `cardTransactions` | `OperatingLocationCardTransaction` | Plus | Card transaction metrics; raw + projected quantities; 1m/3m/12m. |
| `emailAddress` | `EmailAddress` | Core | Email associated with the location. |
| `isMarketable` | `OperatingLocationIsMarketable` | Core | Boolean marketability indicator. |
| `locationType` | `OperatingLocationLocationType` | Core | retail, office, headquarters, hospitality, medical, etc. (15+ values). |
| `operatingStatus` | `OperatingLocationOperatingStatus` | Core | Open / Temporarily Closed / Closed / Unknown. |
| `onlinePresence` | `WebsiteOnlinePresence` | Core | E-commerce indicator. |
| `phoneNumber` | `PhoneNumber` | Core | 12-digit string. |
| `rank` | `OperatingLocationRank` | Plus | Ranked card revenue within H3 res-4 area among same Enigma industry; needs ≥10 nearby same-industry businesses. |
| `revenueQuality` | `OperatingLocationRevenueQuality` | Plus | Revenue anomaly flags with High/Medium severity. |
| `registeredEntity` | `RegisteredEntity` | Premium | Linked legal entity via location relationship. |
| `registration` | `Registration` | Premium | Per-state SoS registration with status. |
| `reviewSummary` | `ReviewSummary` | Plus | Public review counts, score average, first/last review date. |
| `role` | `Role` | Plus | Roles held by people/entities at this location. |
| `technologiesUsed` | `OperatingLocationTechnologiesUsed` | Premium | POS/payments tech: Clover, PayPal, Shopify, Square, Stripe, Toast. |
| `watchlistEntry` | `WatchlistEntry` | Premium | OFAC list entries. |
| `website` | `Website` | Core | URL with decomposed parts. |
| `websiteContent` | `WebsiteContent` | Plus | Website crawl state. |

### 4.3 Legal Entity Attributes

| Attribute | GraphQL Type | Tier | Description |
|---|---|---|---|
| `name` | `LegalEntityName` | Free | Legal entity name. |
| `type` | `LegalEntityType` | Free | Legal classification (Person, Corporation, LLC, etc.). |
| `address` | `Address` | Core | Address types include: site, registered, mailing, registered_agent_address, registered_business_address. |
| `addressDeliverability` | `AddressDeliverability` | Plus | USPS deliverability. |
| `bankruptcy` | `LegalEntityBankruptcy` | Premium | Federal bankruptcy filings (Chapter 7/11/12/13/15) from PACER. Sales-team activated; requested via `attrs`. |
| `emailAddress` | `EmailAddress` | Core | Email — primarily via Contacts attribute (file delivery, not API). |
| `phoneNumber` | `PhoneNumber` | Core | 12-digit NANP-compliant (e.g., `+18005102856`). Coverage 60% business / 69% locations. |
| `registeredEntity` | `RegisteredEntity` | Premium | Standardized name, entity type, formation date/year. |
| `registration` | `Registration` | Premium | Domestic/foreign registration with file number, dates, status. |
| `role` | `Role` | Plus | People/entities holding roles. Coverage 44%. |
| `tin` | `Tin` | Premium | TIN (focus: EIN). 9-digit string. Sales-team activated; requested via `attrs=tin_verification`. |
| `watchlistEntry` | `WatchlistEntry` | Premium | OFAC SDN + Non-SDN list entries. With DOB: 99.97% TPR / 0.4% FPR; without DOB: 99.97% TPR / 5% FPR. |

### 4.4 Person Attributes

> Source: §3.4 Free/Core tier table; `enigma/02-verification-and-kyb/04-kyb-response-matched-data.md` (persons attributes).

| Attribute | GraphQL Type | Tier | Description |
|---|---|---|---|
| `firstName` | `Person.firstName` | Core | First name. |
| `lastName` | `Person.lastName` | Core | Last name. |
| `fullName` | `Person.fullName` | Core | Full name. |
| `dateOfBirth` | `Person.dateOfBirth` | Core | Date of birth. |
| `personId` | `Person.personId` | Core | Unique ID. |
| (in KYB) `name` | string | n/a | Officer name on SoS registration. |
| (in KYB) `titles` | `[String]` | n/a | E.g., `chief executive officer`, `registered agent`. |

### 4.5 Common Fields on Every Attribute Object

Per the per-attribute files in `enigma/09-data-attributes/`, every attribute includes:
- `id` (UUID) — unique identifier
- `firstObservedDate` (String) — date first observed
- `lastObservedDate` (String) — date last observed

### 4.6 Notable Field-Level Details

- **`Address`**: The full set of geocoding fields (`latitude`, `longitude`, `h3Index`, `msa`, `csa`, `county`) is at the Core tier. Country is ISO-3.
- **`AddressDeliverability`**: `deliverable` values include `deliverable`, `vacant`, `not_deliverable`, null. `virtual` values include `virtual_cmra`, `not_virtual`, null. `deliveryType`: street, multi-tenant building, post office box, firm, rural route or highway contract route, general delivery, null.
- **`Registration` sub-status values**: `good_standing`, `not_good_standing`, `pending_active`, `pending_inactive`, `unknown`, null. Status: `active`, `inactive`, `unknown`. Verify package returns full status fields; Identify package returns a restricted subset.
- **`CardTransaction` quantity types** (8): `avg_transaction_size`, `card_revenue_amount`, `card_revenue_yoy_growth`, `card_revenue_prior_period_growth`, `card_customers_average_daily_count`, `card_transactions_count`, `refunds_amount`, `has_transactions`. Periods: `1m`, `3m`, `12m`. `rawQuantity` is unscaled; `projectedQuantity` is scaled by a multiplier based on geography/industry/size.
- **`Rank`**: Cohort scoped to H3 resolution-4. Period currently `12m`. Unavailable if fewer than 10 nearby same-industry businesses.

---

## 5. KYB Verification

> Sources: `enigma/02-verification-and-kyb/01-kyb-packages.md`, `02-kyb-api-quickstart.md`, `03-kyb-response-task-results.md`, `04-kyb-response-matched-data.md`, `enigma/04-resources/05-upgrade-from-kyb-v1-to-v2.md`

### 5.1 Endpoint

```
POST https://api.enigma.com/v2/kyb/?package={identify|verify}&attrs={comma_list}
Headers:
  Content-Type: application/json
  x-api-key: YOUR-API-KEY
```

The default package for v2 is `verify`. (In v1 it was `identify`.)

### 5.2 Request Shape

```json
{
  "data": {
    "names": ["Enigma Technologies", "Enigma"],
    "addresses": [
      {
        "street_address1": "245 5th Ave",
        "city": "New York",
        "state": "NY",
        "postal_code": "10016"
      }
    ],
    "persons": [
      {
        "first_name": "Hicham",
        "last_name": "Oudghiri",
        "ssn": "111111111"
      }
    ],
    "tins": ["000000000"]
  }
}
```

### 5.3 KYB Packages

Two packages, composed of attributes + tasks.

| Capability | Identify | Verify |
|---|---|---|
| Entity name(s), type, formation date | ✓ | ✓ |
| Registration: state, date, file number, registered name, person, addresses | ✓ | ✓ |
| Registration: jurisdiction type, home jurisdiction, status fields | ✗ | ✓ |
| Brand names, high-risk activities, industry, websites, operating location names/addresses | ✓ | ✓ |
| `name_verification`, `sos_name_verification`, `address_verification`, `sos_address_verification` | ✓ | ✓ |
| `person_verification` | ✗ | ✓ |
| `domestic_registration` | ✗ | ✓ |

Both packages typically return in under 2 seconds.

### 5.4 Add-On Tasks

All add-ons work with both packages (sales-team activation required). Specified via the `attrs` query parameter.

| Task | Purpose |
|---|---|
| `tin_verification` | Verify EIN matches business name in IRS records. |
| `ssn_verification` | Verify SSN matches person last name in IRS records. |
| `watchlist` | OFAC sanctions screening (consolidated sanctions list). |

### 5.5 Standard Tasks (Detailed Results)

Each task returns `status` (success/failure), `result` (slug), `reason` (descriptive), and (except `watchlist`) a `sources` array indicating the matched values.

| Task | Possible Results |
|---|---|
| `name_verification` | Success: `name_exact_match`, `name_match`. Failure: `name_not_verified`. |
| `sos_name_verification` | Same shape, but only matches names on SoS registrations. |
| `address_verification` | Success: `address_exact_match`, `address_match`. Failure: `address_not_verified`. |
| `sos_address_verification` | Same shape, SoS-only. |
| `person_verification` | Success: `person_match` (last name exact + first initial match). Failure: `person_not_verified`. Verify-only. |
| `domestic_registration` | `domestic_active` (success), `domestic_unknown` (success), `domestic_inactive` (failure), `domestic_not_found` (failure). Verify-only. |
| `ssn_verification` | `ssn_verified`, `ssn_invalid`, `not_completed` (IRS down), `ssn_not_verified`. |
| `tin_verification` | `tin_verified`, `tin_invalid`, `not_completed` (IRS down or duplicate request), `tin_not_verified`. |
| `watchlist` | `watchlist_no_hits` (success), `watchlist_hits` (failure, with hit count). |

> Tasks operate on one match: if `top_n > 1`, task results are not returned.

### 5.6 Response Shape (v2)

Top-level: `response_id` (UUID), `risk_summary.tasks[]`, `data.registered_entities[]`, `data.brands[]`.

`registered_entities[]` attributes:

| Attribute | Description |
|---|---|
| `id` | UUID. |
| `formation_date` | YYYY-MM-DD; earliest non-null issue_date from registrations. |
| `registered_entity_type` | Standardized legal form (Corporation, LLC, etc.). 18 documented possible values. |
| `names[]` | Up to ten standardized names. |
| `brand_ids[]` | Linked Brand IDs. |
| `registrations[]` | Per-state registrations. |

`registrations[]` attributes:

| Attribute | Identify | Verify |
|---|---|---|
| `registration_state`, `registered_name`, `file_number`, `issue_date` | ✓ | ✓ |
| `persons[]`, `addresses[]` | ✓ | ✓ |
| `jurisdiction_type`, `home_jurisdiction_state` | ✗ | ✓ |
| `status`, `sub_status`, `status_detail` | ✗ | ✓ |

`brands[]` attributes:

| Attribute | Description |
|---|---|
| `id`, `registered_entity_ids[]` | UUIDs. |
| `activities` | Notable activities (e.g., Cannabis). |
| `names[]` | Customer-facing names. |
| `industries[]` | `classification_description`, `classification_type` (`naics_2017_code`, `naics_2022_code`, `sic_code`, `mcc_code`, `enigma_industry_description`), `classification_code`. |
| `websites[]` | Full URLs. |
| `operating_locations[]` | `id`, `addresses[]`, `names[]`. |

`addresses[]` attributes (under `registrations` or `operating_locations`):
`street_address1`, `street_address2`, `city`, `state`, `postal_code`, `type` (headquarters / site / registered_agent / registered / officer / mailing), `deliverable`, `virtual`, `delivery_type`, `rdi`.

`persons[]`: `name`, `titles[]`.

### 5.7 Available Add-On Attributes

Requested via the `attrs` parameter:

| Attribute | Included In |
|---|---|
| `bankruptcies` | `registered_entities` |
| `avg_transaction_size`, `card_transactions_count`, `card_revenue_amount`, `card_revenue_yoy_growth`, `card_revenue_prior_period_growth`, `card_customers_average_daily_count`, `has_transactions`, `refunds_amount` | `brands.card_transactions` |
| `revenue_quality` | `brands.card_transactions` |
| `operating_status` | `operating_locations` (Open / Closed / Temporarily Closed / Unknown) |
| `phone_numbers` | `operating_locations` (12-digit string e.g., `+12544454098`) |

### 5.8 Credit Cost for KYB

The pricing tier table in `enigma/04-resources/03-pricing-and-credit-use.md` does not give a per-call KYB price. Per the source: "Credits are calculated based on the type of attribute returned and its pricing tier" — KYB returns are composed of attributes that fall under the same Free / Core / Plus / Premium tier system. Specific per-package KYB pricing is **not documented in the local source files** and would need to be confirmed against `https://www.enigma.com/pricing`.

### 5.9 KYB v1 → v2 Migration Notes

> Source: `enigma/04-resources/05-upgrade-from-kyb-v1-to-v2.md`

Backwards compatible request body for most cases. Notable changes:

- **Removed:** `legal_existence_risk_rating`, `activity_risk_rating`, `watchlist_risk_rating`, `overall_risk_rating` from `risk_summary`. `best_match`, `data_sources`, `match_confidence`, `matched_fields` from data objects. Deprecated `standardized_status` and `registration_status` from registration. `compliance_risk_level` from activities.
- **Renamed:** `legal_entities` → `registered_entities`. `legal_entity_type` → `registered_entity_type`. `enigma_id` → `id` throughout. `enigma_description` → `enigma_industry_description`.
- **Restructured:** Un-nested `status` into `status`, `sub_status`, `status_detail`. Nested `addresses` under `operating_locations` instead of `brands` directly.
- **Added:** `sources` to task objects. `brand_ids` and `registered_entity_ids`.
- **Default package changed:** v1 `identify` → v2 `verify`.
- **Watchlist requesting changed:** v2 uses values in `name`, `person`, `address` fields instead of v1's separate `persons_to_screen` object.
- **Field value changes:** Non-exact task results no longer use "approximate" (e.g., `name_match` instead of `name_approximate_match`). All IDs are UUIDs. NAICS conforms to 2022 (was 2017). Websites returned as full URLs (was domain only).
- **`match_threshold`:** Same range, but the same value can produce different behavior — re-evaluate on representative samples.

---

## 6. Screening & Compliance

> Sources: `enigma/05-screening/01-customer-and-transaction-screening.md`, `02-screening-api-overview.md`, `03-core-screening-endpoints.md`, `04-decision-management.md`, `05-batch-processing.md`

### 6.1 Endpoint

```
Base URL: https://api.enigma.com/evaluation/sanctions/

Headers:
  x-api-key: <YOUR API KEY>
  Account-Name: <YOUR ACCOUNT NAME>
  Content-Type: application/json
```

### 6.2 Core Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/screen` | Screen customers/transactions against watchlists. |
| `POST` | `/entity/<provider>/<collection>/<record_id>/<format>` | Look up a specific sanctioned entity. Format: `raw`, `display`, `structured`, or `attributes`. |
| `POST` | `/decisions/get_one/<decision_id>` | Retrieve a single decision. |
| `POST` | `/decisions/get_many?...` | Paginated decision query. |
| `POST` | `/decisions/update_one` | Update a decision. |
| `POST` | `/configuration/<query_type>` | Create/update a stored configuration. |
| `POST` | `/batch/start` | Upload an Excel file to start a batch job. |
| `POST` | `/batch/status/<run_id>` | Check batch job status. |
| `POST` | `/batch/results/<run_id>?type={raw|web_screen}` | Download batch results. |

### 6.3 Screen Request

```json
{
  "tag": "example screening request",
  "caller_id": "<some-user-hostname-info>",
  "query_type": "enigma_data",
  "configuration_overrides": {
    "entity": {
      "alert_threshold": 0.8,
      "hit_threshold": 0.5,
      "max_results": 30,
      "weights": { "person_name": 3, "dob": 1, "country_of_affiliation": 2, "address": 1, "org_name": 3 }
    },
    "general": { "archive_retention_days": 90, "entity_detail_level": "minimum", "overrides_on": true },
    "list_groups": ["pos/sdn/all", "pos/non_sdn/all"],
    "text": { "alert_threshold": 0.8, "hit_threshold": 0.5 }
  },
  "searches": [
    {
      "type": "ENTITY",
      "tag": "",
      "entity_description": {
        "person_name": ["John Hanafin"],
        "dob": ["19740710"],
        "country_of_affiliation": ["Ireland"]
      }
    }
  ]
}
```

### 6.4 Search Types

| Type | Description |
|---|---|
| `ENTITY` | Structured entity attributes (person or org); weighted attribute matching. |
| `TEXT` | Unstructured text (e.g., transaction messages) with span-based matches. |
| `LLM_ENTITY` | `ENTITY` enhanced with AI-powered live web search. |
| `LLM_TEXT` | `TEXT` enhanced with AI-powered live web search. |

> Per source: "Unstructured text-based search (`type: TEXT`) is not yet open for public evaluation but soon will be."

### 6.5 List Groups

Available `list_groups` values (defaults: `["pos/sdn/all", "pos/non_sdn/all"]`):

- `pos/sdn/all` — OFAC Specially Designated Nationals
- `pos/non_sdn/all` — OFAC Non-SDN Lists
- `enigma/rogues` — Enigma curated rogues list
- `enigma/testing` — Testing list

### 6.6 Entity Description Fields

| Field | Description |
|---|---|
| `person_name` | Full name of individual. |
| `org_name` | Organization name. |
| `dob` | Date of birth, `yyyymmdd`. |
| `address` | Street address, city, state/province, postal code. |
| `country_of_affiliation` | Country affiliation (matched against citizenship, nationality, place of birth for persons; country of domicile for orgs). |

### 6.7 Screen Response

Top-level fields:

| Field | Description |
|---|---|
| `alert` | True if any hit scored ≥ alert_threshold. |
| `caller_id` | Echoed if provided. |
| `configuration_used` | Full configuration applied. |
| `query_type` | Echoed. |
| `request_id` | UUID. |
| `request_timestamp` | ISO timestamp. |
| `search_results[]` | One entry per search. |

Each `search_results[]` entry has `hits[]`, `search_index`, `tag`, `type`, `alert`. Each entity hit has `attributes` (per-attribute value/score), `score` (weighted), `alert`, `entity` (with `id` and lookup URL). Each text hit has `entity_attribute`, `score`, `alert`, `span` (word indices).

### 6.8 Decision Management

To record decisions you must enable case management with `general.use_case_manager: true` (in stored config or per-request `configuration_overrides`). Then each screening request automatically creates a decision record keyed by `request_id`.

`POST /decisions/get_many` query parameters:

| Parameter | Default | Description |
|---|---|---|
| `page` | 0 | 0-indexed page. |
| `amt` | 10 | Results per page. |
| `alert` | (any) | Filter by alert status. |
| `tag` | — | Filter by request tag. |
| `assignee_id` | — | Filter by assigned user ID. |
| `from_date` / `to_date` | — | `YYYY-MM-DDTHH:MM` filter. |
| `status` | — | E.g., `pending_review`, `cleared`. |

`POST /decisions/update_one` body:

```json
{
  "request_id": "...",
  "status": "cleared",
  "assignee_id": "user-456",
  "notes": "Reviewed and cleared - false positive"
}
```

### 6.9 Batch Processing (on request)

> Available upon request — contact your Enigma rep.

`POST /batch/start` with `multipart/form-data`, file field `file`. Supports `.xlsx`, `.xls`. **Currently supports screening individuals only (not organizations).**

Required Excel columns: `#`, `First Name`, `Last Name`. Optional: `Date of Birth` (YYYYMMDD), `Nationality`, `Passport Number`, `Passport Issued Country`.

Returns `{ "run_id": "..." }`. Status values: `QUEUED`, `STARTED`, `SUCCESS`, `FAILURE`, `CANCELED`. Result types: `raw`, `web_screen`.

### 6.10 Performance Claims

From `enigma/05-screening/01-customer-and-transaction-screening.md`:
- ">99% false positive" baseline rate in conventional screening.
- "Reduces false positive sanctions alert volumes by at least 80% relative to conventional screening solutions."
- ">1 billion requests per month" processed.

### 6.11 Credit Cost for Screening

Specific per-call screening pricing is **not documented in the local source files**. The pricing-and-credit-use document covers attribute-tier billing for the GraphQL data graph but does not enumerate screening costs. `[not documented in source]`

---

## 7. MCP Server

> Sources: `enigma/07-use-enigma-with-ai-via-mcp/00-overview.md`, `01-mcp-tools.md`, `02-claude-and-enigma.md`, `03-screening-mcp-tools.md`, `enigma/04-resources/02-rate-limits.md`

### 7.1 Endpoint and Status

- **Remote MCP Server URL:** `https://mcp.enigma.com/http`
- **Status:** Beta
- **Protocol:** Model Context Protocol (MCP). Source describes integration with Claude, ChatGPT, Cursor, VS Code, Claude Code, Gemini CLI, OpenAI Playground, and other agent frameworks via "Custom Connectors".

> The directive references `mcp.enigma.com/http-key`. The Claude integration doc explicitly uses `https://mcp.enigma.com/http`. Treating the latter as authoritative based on the source. `[discrepancy with directive — source value used]`

### 7.2 Authentication

Per `02-claude-and-enigma.md`: connecting to the MCP server opens a browser for authentication using the same login method used for the Enigma Console. The doc does not describe a separate API-key flow for MCP. Session mechanics beyond OAuth-style connection flow are **not documented**.

### 7.3 Business Intelligence Tools (7)

| Tool | Inputs | Outputs |
|---|---|---|
| `search_business` | Business name (req); website / phone / address (opt) | Revenue (12m), transaction count (12m), YoY growth (12m), NAICS codes & industry, tech stack, location count & samples, matching brands, matching legal entities. |
| `get_brand_locations` | Enigma Brand ID (req) | Full street addresses, 12m card revenue per location, lat/lng. |
| `get_brand_card_analytics` | Enigma Brand ID (req) | Past 60 months of card transaction data: revenue, YoY growth, avg daily customers, transaction count, avg transaction amount, refunds. |
| `get_brand_legal_entities` | Enigma Brand ID (req) | All linked legal entities with Legal Entity IDs, state-by-state registrations, active/inactive status, formation dates, DBA names, filing numbers, domestic vs. foreign patterns. |
| `search_negative_news` | Business name (req), business address (req) | Risk level + categorized findings: legal issues, financial problems, labor disputes, management issues, environmental violations, customer complaints, product recalls, cybersecurity incidents, source URLs. |
| `search_gov_archive` | Business name (req), prompt context (recommended) | Business registrations, permits & licenses (Cannabis, Liquor), health inspections/violations, court filings & liens, environmental records, professional licensing. |
| `search_kyb` | Business name (req), business address (opt) | Matching brands and registered (legal) entities; address verification (SoS-specific or any source); name verification (SoS-specific or any source). |

### 7.4 Screening & Compliance Tools (6)

| Tool | Inputs | Outputs |
|---|---|---|
| `screen_customer` | `name` (req), `dob` (YYYYMMDD), `country`, `passport_number`, `passport_country`, `tag`, `list_groups` (default `["pos/sdn/all", "pos/non_sdn/all"]`) | Match confidence scores, potential matches, hit/alert status, source list info. |
| `screen_business` | `org_name` (req), `country_of_affiliation`, `address`, `bic` (triggers separate search), `tag`, `list_groups` | Same shape as `screen_customer`. |
| `screen_entity_search` | `entity_id` (req, e.g., `ofac/sdn/43085`), `format` (`raw`/`display`/`structured`/`attributes`, default `structured`) | Full entity profile from sanctions lists with all attributes. |
| `find_decision` | `request_id` (req) | Decision: request ID, timestamp, alert status, status, assignee, tags, notes. |
| `find_decisions` | `from_date`, `to_date`, `page`, `amt` (default 100), `alert`, `status`, `assignee_id`, `tag` | Paginated decisions oldest→newest. |
| `update_decision` | `request_id` (req), `user_id` (req), `assignee_id`, `status` (`approved`/`rejected`/`pending`/`in_progress`/`on_hold`), `note` | Updated decision confirmation. |

### 7.5 GraphQL Equivalence

| MCP Tool | GraphQL Equivalent | Notes |
|---|---|---|
| `search_business` | `search` query (Brand) with `cardTransactions`, `industries`, `websites`, `operatingLocations` count, `legalEntities` count | Direct equivalent. |
| `get_brand_locations` | `search(searchInput: { id: ..., entityType: BRAND }) { ... operatingLocations { addresses, cardTransactions } }` | Direct equivalent. |
| `get_brand_card_analytics` | `cardTransactions` connection on Brand or OperatingLocation | Direct equivalent. |
| `get_brand_legal_entities` | `legalEntities` connection on Brand → `registeredEntities { registrations }` | Direct equivalent. |
| `search_kyb` | `POST /v2/kyb/` (REST) — not GraphQL | KYB is REST-only. |
| `search_negative_news` | **None — MCP-exclusive.** | No GraphQL or REST equivalent in the local source docs. |
| `search_gov_archive` | **None — MCP-exclusive.** | No GraphQL or REST equivalent in the local source docs. |
| `screen_*`, `*_decision(s)` | `POST /evaluation/sanctions/...` (REST) | REST-only. |

> **Flagged: `search_negative_news` and `search_gov_archive` are MCP-exclusive capabilities** — they appear only in the MCP tools documentation with no detailed API reference in the local source.

### 7.6 MCP Tool Rate Limits

Tool rate limits are independent of each other and independent of the GraphQL rate limit. Daily = rolling 24-hour window; monthly = rolling 30-day window.

#### Pro & Max Plans (identical)

| Tool | Daily (RPD) | Monthly (RPM) |
|---|---|---|
| `search_business` | 500 | 8,000 |
| `get_brand_locations` | 500 | 8,000 |
| `get_brand_legal_entities` | 500 | 8,000 |
| `get_brand_card_analytics` | 500 | 8,000 |
| `search_gov_archive` | 500 | 6,000 |
| `generate_brands_segment` | 100 | 1,000 |
| `generate_locations_segment` | 100 | 1,000 |
| `search_kyb` | 100 | 2,000 |
| `search_negative_news` | 100 | 2,000 |

> Note: The rate-limits table includes `generate_brands_segment` and `generate_locations_segment` — these tools are **not** in the documented tool inventory in `01-mcp-tools.md`. They are referenced only in the rate-limits table. `[discrepancy in source — undocumented tools]`

#### Enterprise Plan

Configurable based on organization needs.

A tool that hits its rate limit returns `429 Slow Down`.

### 7.7 Workflow Examples (from source)

**Decision review workflow:**
```
find_decisions(from_date="2025-01-20T00:00:00", to_date="2025-01-27T23:59:59", alert=true, status="pending")
update_decision(request_id="...", user_id="...", status="approved", note="Reviewed - false positive, name similarity only")
```

**Customer screening:**
```
screen_customer(name="Maria Rodriguez", dob="19850315", country="Mexico")
```

**Business due diligence:**
```
screen_business(org_name="Global Trade Partners LLC", country_of_affiliation="United Arab Emirates", address="Dubai")
```

---

## 8. Practical Query Patterns

> Sources: `enigma/03-growth-and-gtm-solutions/01..05`, `enigma/06-query-enigma-with-graphql/01-graphql-api-quickstart.md`, `04-use-case-examples.md`, `enigma/04-resources/03-pricing-and-credit-use.md`

### 8.1 Search Brand by Name → 1 credit (Core attribute)

```graphql
query SearchBrand($searchInput: SearchInput!) {
  search(searchInput: $searchInput) {
    ... on Brand {
      id
      enigmaId
      names(first: 1) { edges { node { name } } }
      count(field: "operatingLocations")
    }
  }
}
```
Variables: `{ "searchInput": { "entityType": "BRAND", "name": "Starbucks" } }`

### 8.2 Search Brand + 12-month Card Revenue → 3 credits (Plus attribute)

```graphql
query SearchBrand($searchInput: SearchInput!, $cardTransactionConditions: ConnectionConditions!) {
  search(searchInput: $searchInput) {
    ... on Brand {
      id
      names(first: 1) { edges { node { name } } }
      cardTransactions(first: 1, conditions: $cardTransactionConditions) {
        edges { node { projectedQuantity } }
      }
    }
  }
}
```
Variables:
```json
{
  "searchInput": { "entityType": "BRAND", "name": "Starbucks" },
  "cardTransactionConditions": {
    "filter": {
      "AND": [
        {"EQ": ["period", "12m"]},
        {"EQ": ["quantityType", "card_revenue_amount"]},
        {"EQ": ["rank", 0]}
      ]
    }
  }
}
```

### 8.3 Lookup by ID

```graphql
query Search { search(searchInput: { id: "5f53e079-c66a-487e-8a9d-08efc39652ee" }) { ... on Brand { id names { edges { node { name } } } } } }
```

### 8.4 Search by Website

```graphql
query Search { search(searchInput: { website: "enigma.com", entityType: BRAND }) { ... on Brand { id names { edges { node { name } } } } } }
```

### 8.5 Search by Phone

```graphql
query Search { search(searchInput: { phoneNumber: "1234567890", entityType: BRAND }) { ... on Brand { id } } }
```

### 8.6 Search by Address (within a city)

```graphql
query Search {
  search(searchInput: {
    name: "McDonald's",
    entityType: OPERATING_LOCATION,
    address: { city: "ALBANY", state: "NY" }
  }) { ... on OperatingLocation { addresses { edges { node { fullAddress } } } } }
}
```

### 8.7 Prompt (Semantic) Search — Brand only

```graphql
query Search {
  search(searchInput: { prompt: "Mexican restaurants", entityType: BRAND, conditions: { limit: 3 } }) {
    ... on Brand { names { edges { node { name } } } }
  }
}
```

### 8.8 Search by TIN

```graphql
query Search {
  search(searchInput: {
    name: "Enigma Technologies",
    tin: { tin: "123456789", tinType: TIN }
  }) { ... on Brand { id } }
}
```

### 8.9 Get Brand Locations

```graphql
query GetBrandLocations($searchInput: SearchInput!, $cardTransactionConditions: ConnectionConditions!) {
  search(searchInput: $searchInput) {
    ... on Brand {
      operatingLocations(first: 1) {
        edges { node {
          id
          names(first: 1) { edges { node { name } } }
          addresses(first: 1) { edges { node { fullAddress } } }
          cardTransactions(conditions: $cardTransactionConditions, first: 1) { edges { node { projectedQuantity } } }
        }}
      }
    }
  }
}
```
Variables: `{ "searchInput": { "entityType": "BRAND", "id": "5f1147ed-..." }, "cardTransactionConditions": { "filter": { "AND": [...] } } }`

### 8.10 Get Card Revenue (Operating Location, monthly)

```graphql
query Search {
  search(searchInput: { name: "McDonald's", entityType: OPERATING_LOCATION }) {
    ... on OperatingLocation {
      addresses { edges { node { fullAddress } } }
      cardTransactions(conditions: { filter: { AND: [
        {EQ: ["period", "1m"]},
        {EQ: ["quantity_type", "card_revenue_amount"]}
      ]}}) {
        edges { node { quantityType projectedQuantity rawQuantity periodStartDate periodEndDate period } }
      }
    }
  }
}
```

### 8.11 Get Brand Legal Entities + Registrations

```graphql
query GetBrandLegalEntities($searchInput: SearchInput!) {
  search(searchInput: $searchInput) {
    ... on Brand {
      id
      legalEntities(first: 1) {
        edges { node {
          registeredEntities {
            edges { node { registeredEntityType formationDate name } }
          }
        }}
      }
    }
  }
}
```

### 8.12 Person Search

```graphql
query Search {
  search(searchInput: {
    name: "Enigma",
    person: { firstName: "Joe", lastName: "Smith" },
    entityType: BRAND,
    address: { city: "NEW YORK", state: "NY" }
  }) { ... on Brand { id names { edges { node { name } } } } }
}
```

### 8.13 Aggregate Location Counts

```graphql
query Aggregate {
  aggregate(searchInput: {
    entityType: OPERATING_LOCATION,
    address: { city: "NEW YORK", state: "NY" }
  }) {
    brandsCount: count(field: "brand")
    operatingLocationsCount: count(field: "operatingLocation")
    legalEntitiesCount: count(field: "legalEntity")
  }
}
```

### 8.14 Find Locations Operating on a Specific Date

```graphql
query Search {
  search(searchInput: { name: "McDonald's", entityType: BRAND, conditions: { limit: 1 } }) {
    ... on Brand {
      operatingLocations(conditions: { filter: { AND: [
        {EQ: ["addresses.city", "ALBANY"]},
        {EQ: ["addresses.state", "NY"]},
        {EQ: ["operatingStatuses.operatingStatus", "Open"]},
        {LTE: ["operatingStatuses.lastObservedDate", "2024-01-01"]}
      ]}}) {
        edges { node { addresses(first: 1) { edges { node { fullAddress } } } } }
      }
    }
  }
}
```

### 8.15 Async Segmentation (large result via S3)

```graphql
query Search {
  search(searchInput: {
    prompt: "Mexican restaurants",
    entityType: OPERATING_LOCATION,
    output: { filename: "mexican_restaurants_search_query_1" }
  }) {
    ... on OperatingLocation { addresses(first: 1) { edges { node { fullAddress } } } }
  }
}
```

Then poll:

```graphql
query BackgroundTask {
  backgroundTask(id: "285b6f06-c532-4969-bcfd-cdd82f5de373") {
    status
    result
  }
}
```

### 8.16 Operating-Location Market Rank

```graphql
query GetLocationRanks($searchInput: SearchInput!, $cardTransactionConditions: ConnectionConditions!) {
  search(searchInput: $searchInput) {
    ... on OperatingLocation {
      id
      names(first: 1) { edges { node { name } } }
      addresses(first: 1) { edges { node { fullAddress city state } } }
      ranks(first: 1) { edges { node { position cohortSize rank quantityType period } } }
      cardTransactions(first: 1, conditions: $cardTransactionConditions) { edges { node { projectedQuantity } } }
    }
  }
}
```

---

## 9. Known Challenges & Gotchas

### 9.1 Documentation Gaps

- **`search_negative_news` and `search_gov_archive`**: These are listed in MCP tool inventories with input/output summaries, but no GraphQL or REST equivalents exist in the local source. They are MCP-exclusive capabilities; there is no documented way to access the underlying data outside MCP.
- **`generate_brands_segment` / `generate_locations_segment`**: Appear in `enigma/04-resources/02-rate-limits.md` rate-limit tables but are **not** in the documented MCP tool inventory in `01-mcp-tools.md`. Their inputs and outputs are not documented.
- **MCP endpoint discrepancy**: This directive mentions `mcp.enigma.com/http-key`. The Claude integration doc and overview cite `https://mcp.enigma.com/http`. The latter is treated as authoritative.
- **`08-reference/06-objects/Person.md`, `LegalEntity.md`, `OperatingLocation.md`** are auto-generated placeholders that defer to the online Enigma docs. Field-level details for these types must be reconstructed from the data-attribute files or fetched from the official docs.
- **`enigma/09-data-attributes/01-brand/03-brand-activity.md`** is empty in the local source. Tier (Plus) is known from the `_schemaExtended` introspection summary, but field-level details are not documented locally.
- **`enigma/09-operating-location/01-address.md` and `02-address-deliverability.md`** are empty placeholders. The corresponding files exist with full content under `09-data-attributes/02-operating-location/`.
- **MCP session mechanics**: The Claude integration doc only describes the OAuth-style connection flow. There is no documentation of session lifetime, reconnection semantics, or retry behavior for the MCP server beyond "Connection drops during use? Disable and re-enable the Enigma connector."

### 9.2 Pricing & Credit Surprises

- **Highest-tier-wins is per-entity, not per-query.** A query with one Premium attribute on a parent entity charges the parent only once at Premium. But child entities each pay separately at their own highest tier.
- **Nested entity billing compounds.** A query that fetches 10 OperatingLocations under a Brand, each with a Premium attribute, costs 1 (Brand) + 10 × 5 (locations) = 51 credits. Large `first:` values on connections multiply credit cost rapidly.
- **No server-side caching.** Identical requests are billed every time. Clients must implement their own caching.
- **No credits charged when no data is returned.** A search with no results = 0 credits.
- **KYB and screening pricing is not documented in attribute-tier terms.** The local source files do not enumerate per-call costs for KYB or screening operations.

### 9.3 Rate-Limit Edge Cases

- GraphQL, MCP per-tool, and KYB rate limits are independent — exhausting one does not affect others.
- MCP tool limits use **rolling** windows (24-hour daily / 30-day monthly), not calendar-day or calendar-month resets.
- Each MCP tool's quota is independent — `search_business` exhaustion does not affect `screen_customer`.
- Pro and Max plans have identical MCP rate limits.
- Enterprise plan limits are configurable and not published.
- `429 Slow Down` is the rate-limit response code across both GraphQL and MCP.

### 9.4 Search Behavior Notes

- **`prompt` is Brand-only.** Cannot prompt-search Operating Locations or Legal Entities.
- **`aggregate` only supports OPERATING_LOCATION** and only one filter expression: `{EQ: ["operatingStatuses.operatingStatus", "Open"]}`.
- **Every search must include name, website, or person first/last name.** Or `prompt` with `output` for segmentation.
- **`collect()` math function requires `output`** in `SearchInput` (must run as a background task).
- **Pagination cannot mix `first` and `last`**, and `after` requires `first` while `before` requires `last`.
- **Responses over 6 MB return HTTP 302** to a pre-signed S3 URL in the `Location` header. Clients that don't follow redirects will miss the data.

### 9.5 Data Coverage and Quality

- **Card revenue accuracy:** 67% of brands have error rates within ±30% of ground truth. Highest precision in the <$100k and >$1M annual-revenue buckets (>80% precision); moderate in the $100k–$1M range (>60%).
- **Brand-level vs. location-level revenue:** Brand revenue includes both in-store (from operating locations) and online spend; operating location revenue includes only in-store. Comparing brand-level Enigma revenue to ground truth that excludes online (or vice versa) produces large false discrepancies.
- **Phone coverage:** 60% at business level, 69% at location level (`enigma/09-data-attributes/03-legal-entity/06-phone-number.md`).
- **Role coverage:** 44% at business level, 44% at location level.
- **Address coverage:** 97% businesses, 100% locations.
- **Bankruptcy coverage:** 100% businesses, 100% locations; PACER history back to the 1980s.
- **Watchlist accuracy:** With DOB, 99.97% TPR / 0.4% FPR. Without DOB, 99.97% TPR / 5% FPR.
- **Nine states (AL, DE, MS, NJ, NV, OH, OK, SC, WI) don't provide mailing addresses on registrations.**
- **Delaware and New Jersey don't provide registration status in bulk data.**
- **Match precision is ~94%** based on labeled evaluation data — depends heavily on input quality.

### 9.6 Beta & Stability Caveats

- **MCP server is in beta.** Connection drops during use are documented as expected; troubleshooting recommends disable + re-enable.
- **Claude Custom Connectors are in beta.**
- Per the deprecated-items doc (`enigma/08-reference/10-deprecated/deprecated-items.md`): "no specific deprecated items are actively listed in the API reference" as of last update (March 2026). Use `__schema` introspection to detect future deprecations.

### 9.7 Naming and Versioning Pitfalls

- KYB v1 → v2 renamed `legal_entities` → `registered_entities`, `legal_entity_type` → `registered_entity_type`, `enigma_id` → `id`. v1 default package was `identify`; v2 default is `verify`.
- v2 NAICS codes use 2022 standards instead of 2017 — values may not match across versions.
- v2 returns websites as full URLs; v1 returned domain only.
- v2 IDs are UUIDs throughout; v1 used opaque string IDs (e.g., `B00021aac539f`).
- The `match_threshold` value in v1 may produce different results than the same value in v2 — re-evaluate.

### 9.8 Source Status Codes

The response-status-codes doc only enumerates `200`, `202`, `302`, `400`, `401`, `402`. The `429 Slow Down` rate-limit response is documented in rate-limits docs but absent from the dedicated status-codes page. Other 4XX/5XX codes are **not enumerated**. The error-body shape (`errors` key) is mentioned only briefly.

---

*End of canonical reference.*

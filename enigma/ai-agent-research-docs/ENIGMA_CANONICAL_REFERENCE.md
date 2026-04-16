# Enigma Canonical Reference

Primary-source reference for the Enigma platform: data model, GraphQL / KYB / Screening APIs, MCP server + Gov Archive, credit system, per-entity attribute coverage, and Console/account management.

All content is sourced from files under `enigma/` in this repo (mirrors of `https://documentation.enigma.com/`). Each section cites its source files. Inferences or synthesized content are marked `[inferred]`.

> **Version:** Updated 2026-04-16 after filling all 180 previously-empty `08-reference/06-objects/` placeholders, and after ingesting Gov Archive, Console, and Data Reference sections that were previously absent.
>
> **Source root (local):** `enigma/`
> **Source root (online):** `https://documentation.enigma.com/`

---

## Table of Contents

1. [Data Model](#1-data-model)
2. [GraphQL API](#2-graphql-api)
3. [Credit System](#3-credit-system)
4. [Entity Attributes Reference](#4-entity-attributes-reference)
5. [KYB Verification](#5-kyb-verification)
6. [Screening & Compliance](#6-screening--compliance)
7. [MCP Server & Gov Archive](#7-mcp-server--gov-archive)
8. [Practical Query Patterns](#8-practical-query-patterns)
9. [Console & Account Management](#9-console--account-management)
10. [Known Challenges & Gotchas](#10-known-challenges--gotchas)

---

## 1. Data Model

> Sources: `enigma/01-getting-started/01-overview.md`, `02-the-enigma-data-model.md`, `enigma/04-resources/01-how-enigma-searches-and-matches.md`, `enigma/08-reference/00-data-reference.md`, `enigma/08-reference/00-data-reference/entities/*.md`

Enigma's `graph-model-1` organizes U.S. business information as "a graph of interconnected entities — brands, locations, legal structures, and people." Each entity carries:

- **Attributes** — observed facts (brand name, operating status, address)
- **Derived metrics** — computed aggregations from source data (12-month card revenue, YoY growth)
- **On-demand attributes** — AI-powered values computed at query time (custom brand analysis)
- **Relationships** — typed links to other entities (Brand _operates at_ Operating Location, Legal Entity _owns_ Brand)

### 1.1 Primary Entity Types

| Entity | Definition | Example |
|---|---|---|
| **Brand** | How a business presents itself to customers — trade names, logos, marketing identities. | "Starbucks" — the global brand customers know. |
| **Operating Location** | A specific place where business occurs under a brand, typically at a physical address. Grounds abstract brand/entity concepts in physical space. | A Starbucks store at 123 Main St. |
| **Legal Entity** | "An entity which U.S. law recognizes as having an identity and rights, including both natural persons and artificial entities such as businesses." | "Starbucks Corporation" — the legal entity that files taxes. |
| **Person** | A natural person associated with a business as owner, officer, or contact. | An officer listed on a registration. |

A brand may operate at many locations, be owned by multiple legal entities, and coexist with sister brands under shared corporate structure. A legal entity may own multiple brands or operate many locations.

### 1.2 Supporting Entities

Connected to the four primary entities. Each has its own GraphQL object type with its own attributes and connections:

- `Address`
- `EmailAddress`
- `Industry`
- `PhoneNumber`
- `RegisteredEntity` — legal entity that has registered with at least one U.S. Secretary of State
- `Registration` — a single SoS filing (domestic or foreign)
- `ReviewSummary`
- `Role` — a position held by a person or entity at a business
- `Tin` — Taxpayer Identification Number (primarily EIN)
- `WatchlistEntry` — OFAC sanctions match
- `Website`
- `WebsiteContent` — point-in-time website state

### 1.3 Registered Entity vs. Legal Entity

- A **Legal Entity** is the abstract entity U.S. law recognizes (natural person or artificial entity).
- A **Registered Entity** is a legal entity that has formally registered with one or more U.S. Secretaries of State. Its `RegisteredEntity` object carries standardized name, entity type, and earliest formation date derived from registrations.

KYB v2 renamed `legal_entities` → `registered_entities` in the response envelope for this reason.

### 1.4 Relationships

- **Brand ↔ Operating Location** — which brands operate at which locations
- **Brand ↔ Legal Entity** — which legal entities own or manage a brand
- **Operating Location ↔ Legal Entity** — which legal entities are responsible for specific locations
- **Brand ↔ Brand (affiliated)** — dealers, co-locations, franchise networks
- **Person ↔ Legal Entity** — officer/registered-agent relationships
- **Legal Entity ↔ WatchlistEntry** — dual relationships: `isFlaggedBy` (this entity triggered a match) and `appearsOn` (the watchlist entry itself names this entity)

The relationships enable holistic search: you can find a Brand via a Legal Entity's name, a Legal Entity via a Brand, or an Operating Location via a person's name.

### 1.5 KYB Response Entity Hierarchy

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

### 1.6 Real-World Complexity the Model Handles

- Multi-entity corporations (Gap Inc. → Old Navy, Banana Republic)
- Affiliated brands (dealers like "Curry Honda", co-locations like "Sephora at JCPenney")
- Franchise networks (McDonald's 300+ entities, Dairy Queen 400+ entities)
- Agents/professionals ("James Lavelle, State Farm Agent")
- Medical providers (doctors within larger health systems)
- People-as-brands (hairstylists, therapists)
- Legal entities used as brands (no separate trade name)

---

## 2. GraphQL API

> Sources: `enigma/06-query-enigma-with-graphql/*.md`, `enigma/04-resources/02-rate-limits.md`, `enigma/08-reference/03-inputs/*.md`, `enigma/08-reference/02-enums/*.md`, `enigma/08-reference/06-objects/Query.md`, `ExternalMutation.md`, `BackgroundTask.md`, `enigma/08-reference/07-queries/*.md`, `enigma/08-reference/05-mutations/*.md`

### 2.1 Endpoint and Authentication

- **Endpoint:** `POST https://api.enigma.com/graphql`
- **Auth header:** `x-api-key: YOUR_API_KEY`
- **Body:** Standard GraphQL per the [October 2021 spec](https://spec.graphql.org/October2021/).

### 2.2 Root Query Type

The `Query` type exposes five entry-point fields:

| Field | Type | Arguments | Purpose |
|---|---|---|---|
| `search` | `[SearchUnion]` | `searchInput: SearchInput!` | Discover/retrieve entities (Brand, LegalEntity, OperatingLocation, Person, or Address). |
| `aggregate` | `AggregateResult` | `searchInput: SearchInput!` | Count operating locations and their associated brands/legal entities. |
| `backgroundTask` | `BackgroundTask` | `id: String!` | Poll an async task from a segmentation search. |
| `account` | `Account` | (none) | Return the caller's Account object. |
| `listMaterialization` | `ListMaterialization` | `input: GetListMaterializationInput!` | Retrieve info about a materialized list. |

> The `id: String!` argument on `backgroundTask` is a `String`, not `UUID!` — confirmed against `enigma/08-reference/06-objects/Query.md`.

### 2.3 Root Mutations (via ExternalMutation)

The `ExternalMutation` type groups list-management and suggestion mutations:

| Field | Return Type | Input | Purpose |
|---|---|---|---|
| `createList` | `CreateList` | `CreateListInput!` | Create a new list. |
| `updateList` | `UpdateList` | `UpdateListInput!` | Update an existing list. |
| `deleteList` | `DeleteList` | `DeleteListInput!` | Delete a list. |
| `createListMaterialization` | `CreateListMaterialization` | `CreateListMaterializationInput!` | Begin materializing a list. |
| `cancelListMaterialization` | `CancelListMaterialization` | `CancelListMaterializationInput!` | Cancel in-progress materialization. |
| `createSuggestion` | `CreateSuggestion` | `suggestion: SuggestionInput!` | Submit a data-quality suggestion. |

### 2.4 SearchInput

Required input for both `search` and `aggregate`.

| Field | Type | Description |
|---|---|---|
| `prompt` | String | Natural-language description (`"fast food"`, `"pizza restaurant"`). **Brand only.** |
| `id` | String | Entity ID; takes precedence over other fields. Use with `entityType`. |
| `name` | String | Business name (`"McDonald's"`). |
| `address` | `AddressInput` | Single address: `id`, `street1`, `street2`, `city`, `state`, `postalCode`. |
| `addresses` | `[AddressInput]` | Multiple addresses. **`aggregate` only.** |
| `person` | `PersonInput` | `firstName`, `lastName`, `dateOfBirth` (YYYY-MM-DD), `address`, `tin`. |
| `phoneNumber` | String | 10-digit U.S. phone (`##########` or `###-###-####`). |
| `website` | String | URL (`enigma.com`, `www.enigma.com`, `https://www.enigma.com/`). |
| `tin` | `TinInput` | Business TIN. Requires `name`. |
| `conditions` | `Conditions` | filter / orderBy / limit / pageToken. |
| `matchThreshold` | Float | Confidence threshold (0.0–1.0). |
| `entityType` | `EntityType` | `BRAND` (default), `OPERATING_LOCATION`, `LEGAL_ENTITY`, `PERSON`, `ADDRESS`. |
| `output` | `OutputSpec` | Background-task output (CSV/Parquet to S3). |
| `fields` | `[SearchFieldGroupInput]` | Structured search field groups. |
| `engine` | String | Search engine selection. |
| `enrichmentIdsS3Path` | String | S3 path to parquet file containing `internal_id` column for filtering. |

Every search must include at least one of: business name, website, or person first/last name. Or `prompt` + `output` for segmentation.

### 2.5 EntityType Enum

```graphql
enum EntityType { BRAND OPERATING_LOCATION LEGAL_ENTITY PERSON ADDRESS }
```

### 2.6 AddressInput / PersonInput / TinInput

```graphql
input AddressInput {
  id: ID
  street1: String
  street2: String
  city: String
  state: String
  postalCode: String
}

input PersonInput {
  firstName: String
  lastName: String
  dateOfBirth: String      # ISO 8601 YYYY-MM-DD
  address: AddressInput
  tin: TinInput
}

input TinInput {
  tin: String
  tinType: TinType         # EIN | SSN | ITIN | TIN
}
```

### 2.7 Conditions / ConnectionConditions

| Field | Type | Notes |
|---|---|---|
| `filter` | JSON | Filter expression (operators below). |
| `orderBy` | `[String]` | E.g., `["name DESC", "city ASC"]`. |
| `limit` | Int | Max top-level results. (`Conditions` only.) |
| `pageToken` | String | Numeric offset as string (`"8"` starts from the 8th). (`Conditions` only.) |

### 2.8 Filter Operators

| Operator | Args | Example |
|---|---|---|
| `EQ` / `NE` | 2 | `{EQ: ["name", "McDonald's"]}` |
| `GT` / `GTE` / `LT` / `LTE` | 2 | `{GTE: ["firstObservedDate", "2025-01-01"]}` |
| `IN` / `NOT_IN` | 2 | `{IN: ["operatingStatus", ["Open", "Closed"]]}` |
| `LIKE` / `ILIKE` | 2 | SQL-style with `%` wildcard. |
| `AND` / `OR` | ≥2 | Logical operators with nested arrays. |
| `NOT` | 1 | Logical negation. |
| `ADD` / `SUB` / `MUL` / `DIV` | 2 | Arithmetic on numeric fields. |
| `HAS` | 1 | Field present: `{HAS: ["roles.emailAddresses"]}` |
| `IS_NULL` / `IS_NOT_NULL` | 1 | Null checks. |

**Field paths use dot notation**: `operatingStatuses.operatingStatus`, `addresses.state`, `cardTransactions.period`.

### 2.9 orderBy

List of `"<field> [ASC|DESC]"` strings. Applies only to the field it's attached to. Multiple orderings supported.

### 2.10 Math Functions (NodeFunctions Interface)

All entity objects (Brand, LegalEntity, OperatingLocation, Person, Role, Industry, Address, PhoneNumber, Website, WatchlistEntry, Tin, Registration, RegisteredEntity, ReviewSummary, etc.) implement `NodeFunctions`:

| Function | Return | Arguments |
|---|---|---|
| `count` | `Int` | `field: String!`, `conditions: Conditions` |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` |
| `min` | `Int` | `field: String!`, `conditions: Conditions` |
| `max` | `Int` | `field: String!`, `conditions: Conditions` |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` |

`collect()` **must be output to a file** — requires `output` in `SearchInput`.

### 2.11 Directives

> Source: `enigma/06-query-enigma-with-graphql/05-directives.md`

Chained on a virtual `_fn` field. The first directive reads with `ref` (single path) or `refs` (list). Subsequent directives operate on the previous output.

| Directive | Args | Effect |
|---|---|---|
| `@coalesce` | `ref \| refs` | First non-null value. |
| `@compact` | `ref \| refs` | Drop nulls from array. |
| `@slice` | `ref`, `start`, `end` (negatives allowed) | Array/string subset. |
| `@trim` | `ref \| refs` | Strip whitespace. |
| `@upper` / `@lower` | `ref \| refs` | Case change. |
| `@map` | `ref \| refs`, `field` | Extract nested field per element. |
| `@join` | `ref \| refs`, `sep` | Join array into string. |
| `@include` | `if: Boolean!` | Standard GraphQL; include when true. |
| `@skip` | `if: Boolean!` | Standard GraphQL; omit when true. |

### 2.12 Search Patterns

1. **Text Search** — name/person/address; inline results.
2. **Lookup** — by entity `id`; inline result.
3. **Prompt Search** — natural language; **Brand only**.
4. **Segmentation** — large async results via `output`; returns 202 + background task ID.

### 2.13 Background Tasks

Triggered by setting `output` on `SearchInput`. Poll with the `backgroundTask(id: String!)` query.

Statuses (`enigma/06-query-enigma-with-graphql/02-search-and-get-data-via-api.md`):

| Status | Terminal | Meaning |
|---|---|---|
| `PROCESSING` | No | Executing. |
| `CANCELLED` | Yes | Aborted. |
| `FAILED` | Yes | Failed after retries. |
| `SUCCESS` | Yes | Result is a list of pre-signed S3 URLs. |

The `BackgroundTask` object (from `enigma/08-reference/06-objects/BackgroundTask.md`) exposes: `id` (UUID!), `apiKeyId`, `backgroundTaskType`, `status`, `args` (JSON), `result` (JSON), `progressPercentComplete` (Float), `progressMessage`, `lastError`, `executionAttempts`, `etag`, `createdTimestamp`, `updatedTimestamp`, `lastExecutionTimestamp`, `nextExecutionTimestamp`.

> **Note:** The `BackgroundTask.id` field is `UUID!`, but the `backgroundTask(id: ...)` query argument takes `String!`. UUIDs-as-strings work.

### 2.14 OutputSpec

```graphql
input OutputSpec {
  filename: String         # required when output is set
  format: OutputFormat     # CSV | PARQUET
  s3Path: String           # CSV: unique path to .csv; PARQUET: directory
}

enum OutputFormat { PARQUET CSV }
```

### 2.15 Pagination (Relay Connection Spec)

- `edges[]` — `node` (data) + `cursor` (string position).
- `pageInfo` — `hasNextPage`, `hasPreviousPage`, `startCursor`, `endCursor`.
- Forward: `first`, `after` (exclusive).
- Backward: `last`, `before` (exclusive).

Rules: cannot combine `first` and `last`. `after` requires `first`. `before` requires `last`. All ≥ 0.

### 2.16 aggregate Query

Only supports `entityType: OPERATING_LOCATION`. Only supported filter: `{EQ: ["operatingStatuses.operatingStatus", "Open"]}`. `count(field: ...)` accepts `brand`, `operatingLocation`, `legalEntity`.

### 2.17 HTTP Status Codes

> Source: `enigma/06-query-enigma-with-graphql/06-response-status-codes.md`, rate-limits docs

| Status | Meaning |
|---|---|
| `200 OK` | Success. |
| `202 Accepted` | Async background task started. |
| `302 Found` | Responses >6 MB redirect to pre-signed S3 URL in `Location` header. |
| `400 Bad Request` | Invalid input; errors in body under `errors` key. |
| `401 Unauthorized` | Missing/invalid `x-api-key`. |
| `402 Payment Required` | Billing error (e.g., insufficient credits). |
| `429 Slow Down` | Rate limit exceeded. |

### 2.18 Rate Limits

GraphQL, KYB, and MCP tool rate limits are **independent** of each other.

| Plan | RPS | Burst | Daily (RPD) |
|---|---|---|---|
| Trial | 10 | 20 | 100,000 |
| Pro | 50 | 100 | 500,000 |
| Max | 50 | 100 | 500,000 |
| Enterprise | 100 | 200 | No limit |

---

## 3. Credit System

> Source: `enigma/04-resources/03-pricing-and-credit-use.md`, `enigma/11-console/06-billing.md`

### 3.1 Core Mechanics

- Credits are deducted from the billing account linked to your API key.
- Credit count depends on **type of attribute returned** and the data returned.
- **No data returned → no credits charged.**
- **No server-side caching** — identical requests bill every time.

### 3.2 Highest-Tier-Wins Rule (Per Entity)

If a query returns multiple attributes for the same entity, the entity is billed **once at the tier of the most expensive attribute returned**.

### 3.3 Tier Structure

Per Billing doc and `_schemaExtended` introspection:

| Tier | Credits/Entity |
|---|---|
| Free | 0 |
| Core | 1 |
| Plus | 3 |
| Premium | 5 |

The Billing doc adds a fourth credit category: **Actions** — credits consumed by operational tasks (list materializations, etc.) separate from attribute reads.

### 3.4 Full Tier Assignment Table

Copied verbatim from `enigma/04-resources/03-pricing-and-credit-use.md` (the `_schemaExtended` introspection summary).

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

### 3.6 Worked Examples (verbatim from source)

**Single Attribute, Single Entity → 1 credit.** `names` (Core), `limit: 1` → 1 × 1.

**Single Attribute, 10 Entities → 10 credits.** `names` (Core), `limit: 10` → 10 × 1.

**Multiple Core Attributes, 1 Entity → 1 credit.** `names` + `isMarketables` (both Core), `limit: 1` → 1 × 1.

**Mixed Tiers, 2 Entities → 6 credits.** `names` (Core) + `txnMerchants` (Plus), `limit: 2` → 2 × 3 (highest tier wins).

**Nested (Brand → 10 OperatingLocations with Premium) → 51 credits.**
- Brand `names` (Core) → 1 credit for the brand.
- 10 locations × (`names` Core + `cardTransactions` Premium) = 10 × 5 = 50.
- Total: **1 + 50 = 51**.

### 3.7 Nested Billing Compounds

Each entity level bills separately at its highest tier. Large `first:` values on nested connections multiply cost rapidly — especially when Premium attributes are nested under parents.

---

## 4. Entity Attributes Reference

> Sources: `enigma/09-data-attributes/**/*.md`, `enigma/08-reference/06-objects/*.md`, `enigma/08-reference/00-data-reference/entities/*.md`

Every entity object implements the `NodeFunctions` interface (see §2.10) and exposes the 10 aggregation functions plus `_fn` (JSON). All attribute objects include `id` (UUID!), `firstObservedDate` (String), `lastObservedDate` (String), and an `internal<Type>Id` field for internal use. These are omitted from the tables below.

### 4.1 Brand

**Interfaces:** `NodeFunctions`, `Entity`. **Union:** `SearchUnion`.

Scalar/identifier fields: `id` (ID!), `internalId`, `enigmaId`, `tieBreakerMetadata` (`BrandTieBreakerMetadata`), `searchMetadata` (`Searchmetadata`).

Connection fields (tier shown is the tier of the connected attribute):

| Connection | Returns | Tier | Default `first` |
|---|---|---|---|
| `names` | `BrandNameConnection` | Core | 3 |
| `websites` | `BrandWebsiteConnection` | Core | 100 |
| `operatingLocations` | `BrandOperatingLocationConnection` | (Core per OL) | 100 |
| `legalEntities` | `BrandLegalEntityConnection` | Core+ | 100 |
| `affiliatedBrands` | `BrandBrandConnection` | — | 100 |
| `roles` | `BrandRoleConnection` | Plus | 100 |
| `cardTransactions` | `BrandCardTransactionConnection` | Plus | 3 |
| `revenueQualities` | `BrandRevenueQualityConnection` | Plus | 3 |
| `industries` | `BrandIndustryConnection` | Core | 100 |
| `isMarketables` | `BrandIsMarketableConnection` | Core | 3 |
| `activities` | `BrandActivityConnection` | Plus | 3 |
| `locationDescriptions` | `BrandLocationDescriptionConnection` | Core | 3 |

Standard connection args (on every connection): `first: Int`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions`.

### 4.2 Operating Location

**Interfaces:** `NodeFunctions`, `Entity`. **Union:** `SearchUnion`.

Scalar/identifier fields: `id` (ID!), `internalId`, `enigmaId`, `tieBreakerMetadata` (`OperatingLocationTieBreakerMetadata`), `searchMetadata` (`Searchmetadata`).

| Connection | Returns | Tier | Default `first` |
|---|---|---|---|
| `names` | `OperatingLocationNameConnection` | Core | 3 |
| `addresses` | `OperatingLocationAddressConnection` | Core | 100 |
| `phoneNumbers` | `OperatingLocationPhoneNumberConnection` | Core | 100 |
| `brands` | `OperatingLocationBrandConnection` | Core+ | 100 |
| `roles` | `OperatingLocationRoleConnection` | Plus | 100 |
| `legalEntities` | `OperatingLocationLegalEntityConnection` | Free+ | 100 |
| `operatingStatuses` | `OperatingLocationOperatingStatusConnection` | Core | 3 |
| `technologiesUseds` | `OperatingLocationTechnologiesUsedConnection` | Premium | 3 |
| `websites` | `OperatingLocationWebsiteConnection` | Core | 100 |
| `reviewSummaries` | `OperatingLocationReviewSummaryConnection` | Plus | 100 |
| `cardTransactions` | `OperatingLocationCardTransactionConnection` | Plus | 3 |
| `ranks` | `OperatingLocationRankConnection` | Plus | 3 |
| `revenueQualities` | `OperatingLocationRevenueQualityConnection` | Plus | 3 |
| `locationTypes` | `OperatingLocationLocationTypeConnection` | Core | 3 |
| `isMarketables` | `OperatingLocationIsMarketableConnection` | Core | 3 |

### 4.3 Legal Entity

**Interfaces:** `NodeFunctions`, `Entity`. **Union:** `SearchUnion`.

Scalar/identifier fields: `id` (ID!), `internalId`, `enigmaId`, `tieBreakerMetadata` (`LegalEntityTieBreakerMetadata`), `searchMetadata` (`Searchmetadata`).

| Connection | Returns | Tier | Default `first` |
|---|---|---|---|
| `brands` | `LegalEntityBrandConnection` | Core+ | 100 |
| `names` | `LegalEntityNameConnection` | Free | 3 |
| `roles` | `LegalEntityRoleConnection` | Plus | 100 |
| `persons` | `LegalEntityPersonConnection` | Core | 100 |
| `registeredEntities` | `LegalEntityRegisteredEntityConnection` | Premium | 100 |
| `tins` | `LegalEntityTinConnection` | Premium | 100 |
| `operatingLocations` | `LegalEntityOperatingLocationConnection` | Core+ | 100 |
| `isFlaggedByWatchlistEntries` | `LegalEntityIsFlaggedByWatchlistEntryConnection` | Premium | 100 |
| `appearsOnWatchlistEntries` | `LegalEntityAppearsOnWatchlistEntryConnection` | Premium | 100 |
| `addresses` | `LegalEntityAddressConnection` | Core | 100 |
| `legalEntities` | `LegalEntityLegalEntityConnection` | Free | 100 |
| `types` | `LegalEntityTypeConnection` | Free | 3 |
| `bankruptcies` | `LegalEntityBankruptcyConnection` | Premium | 3 |

### 4.4 Person

**Interfaces:** `NodeFunctions`, `Entity`. **Union:** `SearchUnion`.

| Field | Type | Tier |
|---|---|---|
| `id` | `ID!` | — |
| `internalId`, `enigmaId`, `tieBreakerMetadata` (String), `searchMetadata` (Searchmetadata) | — | — |
| `names` | `PersonNameConnection` (default `first: 3`) | Core |
| `legalEntities` | `PersonLegalEntityConnection` (default `first: 100`) | Free+ |

> **Note:** `Person.tieBreakerMetadata` returns `String` (unlike Brand/OperatingLocation/LegalEntity which have typed `<Type>TieBreakerMetadata` objects).

### 4.5 Supporting Entity Details

All below implement `NodeFunctions` but **not** `Entity` (they're not top-level `SearchUnion` members unless noted).

#### Address (Core)

Fields: `streetAddress1`, `streetAddress2`, `fullAddress`, `city`, `state`, `zip`, `county`, `country` (ISO-3), `msa`, `csa`, `latitude`, `longitude`, `h3Index` (resolution 10), `type` (in Legal Entity context: `site` / `registered` / `mailing` / `registered_agent_address` / `registered_business_address`).

#### AddressDeliverability (Plus)

`deliverable` ∈ {`deliverable`, `vacant`, `not_deliverable`, null}. `deliveryType` ∈ {street, multi-tenant building, post office box, firm, rural route or highway contract route, general delivery, null}. `rdi` ∈ {`Residential`, `Commercial`}. `virtual` ∈ {`virtual_cmra`, `not_virtual`, null}.

#### PhoneNumber (Core)

`phoneNumber`: 12-digit NANP-compliant string — `"+1"` + area code (3) + exchange (3) + line (4). Must have valid U.S. area code. Connections: `operatingLocations`, `roles`.

#### Website (Core)

`website` (full URL), `domain`, `subdomain`, `topLevelDomain`, `path`, `fragment`. Connections: `brands`, `operatingLocations`, `websiteContents` (Plus), `technologiesUseds` (Premium), `onlinePresences` (Core).

#### Industry (Core)

`industryDesc`, `industryCode`, `industryType` ∈ {`naics_2017_code`, `naics_2022_code`, `sic_code`, `mcc_code`, `enigma_industry_description`}. Connections: `brands`, `parentIndustries` (hierarchy).

#### EmailAddress (Core)

`emailAddress`. Connection: `roles` (via `EmailAddressRoleConnection`). Per `enigma/09-data-attributes/03-legal-entity/04-email-address.md`: **email addresses are primarily available through the Contacts attribute, which is only available via file delivery, not in the API.**

#### Role (Plus)

`jobTitle` (normalized — lowercase, expanded abbreviations, accents removed), `jobFunction` (standardized — "Accounting", "Contracts"), `managementLevel` (governance: owner, founder, board of directors; or functional: head, c-suite, director-level, vp-level, manager, non-manager), `externalId` (JSON), `externalUrl`. Connections: `operatingLocations`, `phoneNumbers`, `emailAddresses`, `legalEntities`, `registrations`, `brands`. Coverage: 44% business / 44% location.

#### Registration (Premium)

Full documented fields: `registrationType`, `expirationDate` (Date), `registrationState`, `jurisdictionType` (`domestic` / `foreign`), `homeJurisdictionState`, `registeredName`, `fileNumber`, `issueDate` (Date YYYY/MM/DD), `status` (`active` / `inactive` / `unknown`), `subStatus` ∈ {`good_standing`, `not_good_standing`, `pending_active`, `pending_inactive`, `unknown`, null}, `statusDetail` (official state message). Connections: `addresses`, `roles`, `registeredEntities`. Verify package returns status fields; Identify package returns a restricted subset.

#### RegisteredEntity (Premium)

`name` (standardized from registrations), `registeredEntityType`, `formationDate` (earliest non-null issue date, YYYY-MM-DD), `formationYear` (Int).

#### Tin (Premium)

`tin` (9-digit IRS ID), `tinType` ∈ {`EIN`, `SSN`, `ITIN`, `ATIN`, `PTIN`}, `validity` ∈ {`issued`, `not_issued`, `invalid`, null}. Currently provided data is primarily EIN records from SoS registrations and IRS forms. Connection: `legalEntities`.

#### WatchlistEntry (Premium)

`watchlistName` (SDN / Non-SDN variants). **Dual legal-entity connections:** `legalEntitiesIsFlaggedBy` (entities flagged _by_ this entry) and `legalEntitiesAppearsOn` (entities the entry _appears on_). Also: `addresses` connection.

Sources: OFAC SDN + Consolidated Sanctions (FSE, SSI, PLC, CAPTA, NS-MBS, NS-CMIC). With DOB: 99.97% TPR / 0.4% FPR; without DOB: 99.97% TPR / 5% FPR.

#### LegalEntityBankruptcy (Premium)

PACER-sourced. Fields include `chapterType` (7/11/12/13/15), `caseNumber`, `petition` (voluntary/involuntary), `filingDate`, `entryDate`, `dateConverted`, `dateDismissed`, `dateTerminated`, `debtorDischargedDate`, `planConfirmedDate`, `debtorName`, `judge`, `trustee`, plus a `bankruptcy_flag` boolean at the data-attribute level. 100% coverage at business and location level; history back to the 1980s.

#### ReviewSummary (Plus)

`reviewCount`, `reviewScoreAvg`, `firstReviewDate` (from sample of 100 reviews), `lastReviewDate` (may lag up to 3 months). Rank 0 = most recent summary.

#### OperatingLocationRank (Plus)

`position`, `cohortSize`, `periodStartDate`, `periodEndDate`, `period` (currently `12m`), `quantityType`. Ranked within H3 resolution-4 cell + same Enigma industry. Unavailable if fewer than 10 nearby same-industry businesses.

#### OperatingLocationCardTransaction / BrandCardTransaction (Plus)

`period` ∈ {`1m`, `3m`, `12m`}, `periodStartDate`, `periodEndDate`, `rawQuantity` (unscaled), `projectedQuantity` (scaled by panel multiplier), `quantityType` ∈ 8 values below.

Quantity types: `card_revenue_amount`, `card_transactions_count`, `avg_transaction_size`, `card_customers_average_daily_count`, `card_revenue_yoy_growth`, `card_revenue_prior_period_growth`, `refunds_amount`, `has_transactions`.

#### BrandActivity (Plus)

High-compliance-risk activity classification. ~130K brands classified. Categories: Cannabis, Tobacco/Vaping, Firearms/Weapons/Ammunition, Adult Entertainment/Dating, Gambling/Sports Betting, Payments/Money Transfer, MLM, Pawn Shops/Check Cashing/Payday Loans, Cryptocurrencies/Digital Assets, Investments/Financing, Legal Finance (collections, bail bonds), Gift Cards, Health/Lifestyle, Prescription Drugs. Derived from keywords in names/websites/industry descriptions.

#### OperatingLocationLocationType (Core)

15+ values: professional service, retail, civic organization, hospitality, real estate, public venue, headquarters, office, trade service, business service, scientific, educational, supplier, government, residential, manufacturing, religious, agriculture, medical.

#### Technologies Used (Premium)

- **WebsiteTechnologiesUsed:** Adyen, Braintree, PayPal, Shopify, Stripe.
- **OperatingLocationTechnologiesUsed:** Clover, PayPal, Shopify, Square, Stripe, Toast.

Sourced from merchant identifiers in card transaction data via independently verified private vendors.

### 4.6 Coverage Stats (from data-attribute files)

| Attribute | Business Coverage | Location Coverage |
|---|---|---|
| Address | 97% | 100% |
| Phone Number | 60% | 69% |
| Role | 44% | 44% |
| Bankruptcy | 100% | 100% |

Nine states (AL, DE, MS, NJ, NV, OH, OK, SC, WI) don't provide mailing addresses on registrations. Delaware and New Jersey don't provide registration status in bulk data.

---

## 5. KYB Verification

> Sources: `enigma/02-verification-and-kyb/*.md`, `enigma/04-resources/05-upgrade-from-kyb-v1-to-v2.md`

### 5.1 Endpoint

```
POST https://api.enigma.com/v2/kyb/?package={identify|verify}&attrs={comma_list}
Headers: Content-Type: application/json, x-api-key: YOUR-API-KEY
```

Default package in v2 is `verify` (was `identify` in v1). Typical response time: under 2 seconds.

### 5.2 Request Body

```json
{
  "data": {
    "names": ["Enigma Technologies"],
    "addresses": [{"street_address1": "245 5th Ave", "city": "New York", "state": "NY", "postal_code": "10016"}],
    "persons": [{"first_name": "Hicham", "last_name": "Oudghiri", "ssn": "111111111"}],
    "tins": ["000000000"]
  }
}
```

### 5.3 Package Comparison

| | Identify | Verify |
|---|---|---|
| Entity name(s), type, formation date | ✓ | ✓ |
| Registration: state, date, file number, registered name, persons, addresses | ✓ | ✓ |
| Registration: jurisdiction type, home jurisdiction, status fields | ✗ | ✓ |
| Brand names, high-risk activities, industry, websites, operating locations | ✓ | ✓ |
| `name_verification`, `sos_name_verification`, `address_verification`, `sos_address_verification` | ✓ | ✓ |
| `person_verification` | ✗ | ✓ |
| `domestic_registration` | ✗ | ✓ |

### 5.4 Add-On Tasks (sales-team activated, via `attrs` param)

| Task | Purpose |
|---|---|
| `tin_verification` | EIN matches business name (IRS). |
| `ssn_verification` | SSN matches person last name (IRS). |
| `watchlist` | OFAC consolidated sanctions screening. |

### 5.5 Task Results

| Task | Results |
|---|---|
| `name_verification` / `sos_name_verification` | `name_exact_match` (success), `name_match` (success), `name_not_verified` (failure) |
| `address_verification` / `sos_address_verification` | `address_exact_match`, `address_match`, `address_not_verified` |
| `person_verification` (Verify only) | `person_match` (last name exact + first initial), `person_not_verified` |
| `domestic_registration` (Verify only) | `domestic_active`, `domestic_unknown` (success); `domestic_inactive`, `domestic_not_found` (failure) |
| `ssn_verification` | `ssn_verified`; `ssn_invalid`, `not_completed`, `ssn_not_verified` |
| `tin_verification` | `tin_verified`; `tin_invalid`, `not_completed`, `tin_not_verified` |
| `watchlist` | `watchlist_no_hits`; `watchlist_hits` (with hit count) |

> Tasks operate on one match. If `top_n > 1` is specified, task results are not returned.

### 5.6 Response Shape (v2)

```
response_id (UUID)
risk_summary.tasks[]  — each with status, result, reason, sources[]
data.registered_entities[]
  └─ registrations[]
       └─ persons[], addresses[]
data.brands[]
  └─ industries[], operating_locations[]
```

Each task includes `sources[]` (except `watchlist`) showing what in Enigma's data matched.

### 5.7 Add-On Attributes (via `attrs`)

| Attribute | Nests Under |
|---|---|
| `bankruptcies` | `registered_entities` |
| `avg_transaction_size`, `card_transactions_count`, `card_revenue_amount`, `card_revenue_yoy_growth`, `card_revenue_prior_period_growth`, `card_customers_average_daily_count`, `has_transactions`, `refunds_amount` | `brands.card_transactions` |
| `revenue_quality` | `brands.card_transactions` |
| `operating_status` | `operating_locations` |
| `phone_numbers` | `operating_locations` |

### 5.8 v1 → v2 Migration

- **Renamed:** `legal_entities` → `registered_entities`; `legal_entity_type` → `registered_entity_type`; `enigma_id` → `id`; `enigma_description` → `enigma_industry_description`.
- **Removed:** `legal_existence_risk_rating`, `activity_risk_rating`, `watchlist_risk_rating`, `overall_risk_rating`, `best_match`, `data_sources`, `match_confidence`, `matched_fields`, `standardized_status`, `registration_status`, `compliance_risk_level`.
- **Added:** `sources[]` on tasks; `brand_ids`, `registered_entity_ids` links.
- **Restructured:** Un-nested `status` → `status` + `sub_status` + `status_detail`. Addresses now nested under `operating_locations` instead of `brands`.
- **Value changes:** `name_approximate_match` → `name_match`; UUIDs everywhere; NAICS 2022 instead of 2017; websites as full URLs.
- **Default package:** v2 = `verify`.
- **Watchlist:** v2 uses `name`/`person`/`address` fields directly (no separate `persons_to_screen`).

---

## 6. Screening & Compliance

> Sources: `enigma/05-screening/*.md`

### 6.1 Endpoints

```
Base: https://api.enigma.com/evaluation/sanctions/
Headers: x-api-key, Account-Name, Content-Type: application/json
```

| Method | Path | Purpose |
|---|---|---|
| POST | `/screen` | Screen customers/transactions. |
| POST | `/entity/<provider>/<collection>/<record_id>/<format>` | Entity lookup. Format: `raw`/`display`/`structured`/`attributes`. |
| POST | `/decisions/get_one/<decision_id>` | Single decision. |
| POST | `/decisions/get_many?...` | Paginated decisions. |
| POST | `/decisions/update_one` | Update decision. |
| POST | `/configuration/<query_type>` | Create/update stored config. |
| POST | `/batch/start` | Upload Excel for batch screening. |
| POST | `/batch/status/<run_id>` | Batch job status. |
| POST | `/batch/results/<run_id>?type={raw\|web_screen}` | Batch results. |

### 6.2 Search Types

| Type | Description |
|---|---|
| `ENTITY` | Structured attributes (person or org); weighted attribute matching. |
| `TEXT` | Unstructured text with span-based matches. *(Not yet public.)* |
| `LLM_ENTITY` | `ENTITY` + AI-powered live web search. |
| `LLM_TEXT` | `TEXT` + AI-powered live web search. |

### 6.3 List Groups

Defaults: `["pos/sdn/all", "pos/non_sdn/all"]`. Available: `pos/sdn/all` (OFAC SDN), `pos/non_sdn/all` (OFAC Non-SDN), `enigma/rogues`, `enigma/testing`.

### 6.4 Entity Description

Fields: `person_name`, `org_name`, `dob` (`yyyymmdd`), `address`, `country_of_affiliation`.

### 6.5 Decision Management

Requires `general.use_case_manager: true` (stored config or per-request override). Each subsequent screening auto-creates a decision keyed by `request_id`.

`/decisions/get_many` query params: `page` (default 0), `amt` (default 10), `alert` (bool), `tag`, `assignee_id`, `from_date`, `to_date`, `status`.

`/decisions/update_one` body: `request_id` (req), `status`, `assignee_id`, `notes`.

### 6.6 Batch Processing

Available on request (contact Enigma). Currently **screens individuals only (not organizations)**.

Excel columns — required: `#`, `First Name`, `Last Name`. Optional: `Date of Birth` (YYYYMMDD), `Nationality`, `Passport Number`, `Passport Issued Country`.

Statuses: `QUEUED`, `STARTED`, `SUCCESS`, `FAILURE`, `CANCELED`. Result types: `raw`, `web_screen`.

### 6.7 Claimed Performance

- Reduces false positive sanctions alert volumes by at least 80% vs conventional screening.
- >1 billion requests per month processed.
- Baseline false-positive rate for conventional screening: >99% (industry norm).

---

## 7. MCP Server & Gov Archive

> Sources: `enigma/07-use-enigma-with-ai-via-mcp/*.md`, `enigma/10-gov-archive/01-overview.md`, `enigma/04-resources/02-rate-limits.md`

### 7.1 Two MCP Endpoints (Different Auth Flows)

| Endpoint | Auth Flow | Use Case |
|---|---|---|
| `https://mcp.enigma.com/http` | OAuth-style (browser login to Enigma Console) | Claude Custom Connectors, ChatGPT, Cursor, VS Code, Claude Code, Gemini CLI, OpenAI Playground |
| `https://mcp.enigma.com/http-key` | API key (`x-api-key` header) | Custom agent frameworks (OpenAI Agents SDK, LangChain, CrewAI, AutoGen), direct JSON-RPC |

**Status:** Beta.

> The earlier canonical reference flagged `/http-key` as a directive discrepancy — in fact, both endpoints exist. `/http` is for interactive OAuth connectors; `/http-key` is for API-key-authenticated agents. Confirmed in `enigma/10-gov-archive/01-overview.md`.

### 7.2 Business Intelligence Tools (7)

| Tool | Required Inputs | Optional Inputs | Output Highlights |
|---|---|---|---|
| `search_business` | business name | website, phone, address | Revenue 12m, txn count 12m, YoY growth, NAICS + industry, tech stack, location count + samples, matching brands/legal entities. |
| `get_brand_locations` | Enigma Brand ID | — | Addresses, 12m revenue per location, lat/lng. |
| `get_brand_card_analytics` | Enigma Brand ID | — | Past 60 months: revenue, YoY growth, avg daily customers, txn count, avg txn size, refunds. |
| `get_brand_legal_entities` | Enigma Brand ID | — | All linked legal entities, state-by-state registrations, status, formation dates, DBA, file numbers, domestic/foreign. |
| `search_negative_news` | business name, business address | — | Risk level + categorized findings (legal, financial, labor, management, environmental, customer complaints, recalls, cyber, source URLs). |
| `search_gov_archive` | business name | prompt context (recommended), and: `query`, `original_prompt`, `page` (default 1), `limit`, `historical_data` (bool, default false), `category`, `resource_ids[]`, `include_row_details` (bool) | 7,000+ datasets: business registrations, permits, licenses, health inspections, court filings, liens, environmental records, professional licensing. |
| `search_kyb` | business name | address | Matching brands + registered entities; name and address verification (SoS-specific or any source). |

### 7.3 Gov Archive Details

**Plan requirement:** Max or Enterprise only.

**Datasets (7,000+):**
- Business registrations (SoS filings, DBA)
- Permits and licenses (liquor, cannabis, professional)
- Health and safety (food inspections, code violations)
- Court filings and liens (UCC liens, bankruptcy)
- Environmental compliance (EPA, remediation)
- Workplace safety (OSHA violations, citations)
- Government contracts (USA Spending)
- Financial incentives (economic programs, tax credits)

**Direct API access:** JSON-RPC to MCP HTTP endpoint (`/http-key` with API-key header).

**Response structure:** `dataset_info` (source metadata) + `matched_row_info` (matched records). Set `include_row_details: true` for full row_details object with dataset-specific fields.

### 7.4 Screening & Compliance MCP Tools (6)

| Tool | Required | Optional |
|---|---|---|
| `screen_customer` | `name` | `dob` (YYYYMMDD), `country`, `passport_number`, `passport_country`, `tag`, `list_groups` |
| `screen_business` | `org_name` | `country_of_affiliation`, `address`, `bic` (triggers separate BIC search), `tag`, `list_groups` |
| `screen_entity_search` | `entity_id` (e.g. `ofac/sdn/43085`) | `format` (`raw`/`display`/`structured`/`attributes`, default `structured`) |
| `find_decision` | `request_id` | — |
| `find_decisions` | — | `from_date`, `to_date`, `page`, `amt` (default 100), `alert`, `status`, `assignee_id`, `tag` |
| `update_decision` | `request_id`, `user_id` | `assignee_id`, `status` (`approved`/`rejected`/`pending`/`in_progress`/`on_hold`), `note` |

Defaults for `list_groups`: `["pos/sdn/all", "pos/non_sdn/all"]`. Decision tools require case management (`use_case_manager: true`).

### 7.5 GraphQL / REST Equivalence for MCP Tools

| MCP Tool | Equivalent |
|---|---|
| `search_business` | GraphQL `search` on Brand. |
| `get_brand_locations` | GraphQL `search(searchInput: {id, entityType: BRAND})` → `operatingLocations`. |
| `get_brand_card_analytics` | GraphQL `cardTransactions` connection. |
| `get_brand_legal_entities` | GraphQL `legalEntities` → `registeredEntities` → `registrations`. |
| `search_kyb` | REST `POST /v2/kyb/`. |
| `search_negative_news` | No direct equivalent documented. Accessible via MCP only. |
| `search_gov_archive` | Direct JSON-RPC to `mcp.enigma.com/http-key` (MCP endpoint, not GraphQL). 7,000+ underlying datasets. |
| `screen_*`, `*_decision(s)` | REST `POST /evaluation/sanctions/...`. |

### 7.6 MCP Rate Limits

Tool limits are **independent** of each other and of GraphQL. Rolling 24-hour daily / 30-day monthly.

**Pro & Max (identical):**

| Tool | Daily | Monthly |
|---|---|---|
| `search_business`, `get_brand_locations`, `get_brand_legal_entities`, `get_brand_card_analytics` | 500 | 8,000 |
| `search_gov_archive` | 500 | 6,000 |
| `generate_brands_segment`, `generate_locations_segment` | 100 | 1,000 |
| `search_kyb`, `search_negative_news` | 100 | 2,000 |

**Enterprise:** Configurable.

Rate-limited response: `429 Slow Down`.

> `generate_brands_segment` / `generate_locations_segment` appear only in rate-limit tables; no tool definition in the MCP tool inventory. `[documentation gap]`

---

## 8. Practical Query Patterns

> Sources: `enigma/03-growth-and-gtm-solutions/*.md`, `enigma/06-query-enigma-with-graphql/01, 02, 04.md`

### 8.1 Search Brand by Name → 1 credit

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
Variables: `{"searchInput": {"entityType": "BRAND", "name": "Starbucks"}}`

### 8.2 Search Brand + 12m Card Revenue → 3 credits

```graphql
query SearchBrand($searchInput: SearchInput!, $cardTx: ConnectionConditions!) {
  search(searchInput: $searchInput) {
    ... on Brand {
      id
      names(first: 1) { edges { node { name } } }
      cardTransactions(first: 1, conditions: $cardTx) {
        edges { node { projectedQuantity } }
      }
    }
  }
}
```
Variables:
```json
{
  "searchInput": {"entityType": "BRAND", "name": "Starbucks"},
  "cardTx": {"filter": {"AND": [
    {"EQ": ["period", "12m"]},
    {"EQ": ["quantityType", "card_revenue_amount"]},
    {"EQ": ["rank", 0]}
  ]}}
}
```

### 8.3 Lookup by ID

```graphql
query Lookup { search(searchInput: { id: "5f53e079-c66a-487e-8a9d-08efc39652ee" }) { ... on Brand { id names { edges { node { name } } } } } }
```

### 8.4 Search by Website

```graphql
query Search { search(searchInput: { website: "enigma.com", entityType: BRAND }) { ... on Brand { id names { edges { node { name } } } } } }
```

### 8.5 Search by Phone

```graphql
query Search { search(searchInput: { phoneNumber: "1234567890", entityType: BRAND }) { ... on Brand { id } } }
```

### 8.6 Operating Locations by City

```graphql
query Search {
  search(searchInput: {
    name: "McDonald's", entityType: OPERATING_LOCATION,
    address: { city: "ALBANY", state: "NY" }
  }) {
    ... on OperatingLocation { addresses { edges { node { fullAddress } } } }
  }
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

### 8.9 Brand → Operating Locations with Revenue

```graphql
query GetBrandLocations($in: SearchInput!, $cardTx: ConnectionConditions!) {
  search(searchInput: $in) {
    ... on Brand {
      operatingLocations(first: 1) {
        edges { node {
          id
          names(first: 1) { edges { node { name } } }
          addresses(first: 1) { edges { node { fullAddress } } }
          cardTransactions(conditions: $cardTx, first: 1) { edges { node { projectedQuantity } } }
        } }
      }
    }
  }
}
```

### 8.10 Operating Location → Monthly Revenue

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

### 8.11 Brand → Legal Entities → Registrations

```graphql
query GetBrandLegalEntities($in: SearchInput!) {
  search(searchInput: $in) {
    ... on Brand {
      id
      legalEntities(first: 1) {
        edges { node {
          registeredEntities {
            edges { node { registeredEntityType formationDate name } }
          }
        } }
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

### 8.14 Locations Open on a Specific Date

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

### 8.15 Async Segmentation to S3

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

Poll via:

```graphql
query BackgroundTask {
  backgroundTask(id: "285b6f06-c532-4969-bcfd-cdd82f5de373") { status result }
}
```

### 8.16 Operating Location Market Rank

```graphql
query GetLocationRanks($in: SearchInput!, $cardTx: ConnectionConditions!) {
  search(searchInput: $in) {
    ... on OperatingLocation {
      id
      names(first: 1) { edges { node { name } } }
      addresses(first: 1) { edges { node { fullAddress city state } } }
      ranks(first: 1) { edges { node { position cohortSize rank quantityType period } } }
      cardTransactions(first: 1, conditions: $cardTx) { edges { node { projectedQuantity } } }
    }
  }
}
```

### 8.17 Account Query

```graphql
query { account { /* fields on Account object */ } }
```

Returns the caller's Account object (for workspace/API-key identity).

### 8.18 Watchlist Query (dual relationship)

```graphql
query Search {
  search(searchInput: { name: "Acme Shell Co", entityType: LEGAL_ENTITY }) {
    ... on LegalEntity {
      id
      names(first: 1) { edges { node { name } } }
      isFlaggedByWatchlistEntries(first: 10) {
        edges { node { watchlistName } }
      }
      appearsOnWatchlistEntries(first: 10) {
        edges { node { watchlistName } }
      }
    }
  }
}
```

---

## 9. Console & Account Management

> Sources: `enigma/11-console/*.md`

### 9.1 Access Overview

Primary web UI at `https://console.enigma.com/`. Key capabilities:

- Data exploration (brand/entity/person profiles)
- Segment definition + enrichment
- API Playground (GraphQL testing)
- Team management + role assignment
- S3/SFTP file exchange for batch workflows
- SAML SSO configuration
- Workspace organization (Enterprise)
- Credit usage monitoring + invoice management

Settings structure: **Account** (API keys, preferences, data connections), **Access** (users, SSO, workspaces), **Billing** (plan, usage, invoices).

### 9.2 API Keys

**Location:** `Settings > Account > API Keys`. Key is shown only once at creation — must be copied immediately.

Enterprise workspaces have their own workspace-scoped keys. Revocation is **permanent** — applications using the revoked key lose access immediately.

### 9.3 Team Roles (3 levels)

| Capability | Owner | Admin | Member |
|---|---|---|---|
| View/search data | ✓ | ✓ | ✓ |
| Use API | ✓ | ✓ | ✓ |
| Export lists | ✓ | ✓ | ✓ |
| Invite/remove members | ✓ | ✓ | — |
| Change member roles | ✓ | ✓ | — |
| Configure SSO | ✓ | ✓ | — |
| Transfer ownership | ✓ | — | — |

- Each org has exactly **one Owner**. The Owner role cannot be assigned from the dropdown — only via Transfer Ownership.
- New invitees join as Member by default. Only Member ↔ Admin changes available via Console.
- Transfer ownership is irreversible; previous owner becomes Admin.

### 9.4 Workspaces (Enterprise-only)

At `Settings > Access > Workspaces`. Admins/Owners create workspaces to isolate API keys and user access by team/project. Each workspace has independent API keys.

### 9.5 Single Sign-On (SAML 2.0)

SP-initiated SAML 2.0. Supports Okta, Azure AD, Google Workspace, OneLogin, and any SAML 2.0 IdP.

**Required attributes:** `email`, `given_name`, `family_name`, `name`. Attribute names are **case-sensitive**.

**Flow:** User visits `https://console.enigma.com/login` → clicks "Log in with SSO" → enters email → Enigma redirects to IdP → IdP sends SAML assertion → Enigma validates + signs in.

**Limitation:** IdP-initiated flow doesn't work — clicking the Enigma tile in the IdP dashboard fails. Users must always start from the Enigma login page.

**Duplicate provider error:** An IdP can link to only one Enigma org. For transfers, contact support.

### 9.6 File Exchange

At `Settings > Account > Data Connections`. Three connection types:

| Type | When |
|---|---|
| Enigma SFTP | Quick setup, Enigma-managed infrastructure |
| Your SFTP | Internet-accessible SFTP servers under your control |
| Your S3 | AWS workflows, large-scale |

**Constraint:** File paths cannot exceed **110 characters** from bucket/SFTP directory root.

**S3 permissions:** `ListBucket`, `GetObject`, `PutObject`, `DeleteObject`. IAM roles recommended over long-term access keys.

**Optional:** PGP encryption layered on top of TLS/SSH.

### 9.7 Billing & Usage

At `Settings > Billing`. Sections:

- **Plan Management:** View/upgrade tier, payment method via Stripe, Auto-Recharge configuration (credits auto-purchased at configurable threshold), manual credit purchase.
- **Usage Tracking:** Current balance, 30-day consumption graph, breakdown by tier (Core, Plus, Premium, **Actions** — the 4th credit category for operational tasks).
- **Invoice Management:** History with dates, amounts, payment status, downloadable copies.

### 9.8 Profile and Security

Profile updates at `Settings > Account > Preferences` (name only). Password changes via the Security section. **Email address changes require contacting `support@enigma.com`.**

---

## 10. Known Challenges & Gotchas

### 10.1 Documentation Gaps (Remaining)

- **`generate_brands_segment` / `generate_locations_segment`**: Appear only in MCP rate-limit tables (`enigma/04-resources/02-rate-limits.md`). No tool definition in the documented MCP tool inventory. Inputs/outputs unknown.
- **`OperatingLocationCache`**: Dedicated doc page returns the generic landing page upstream. Provisional stub in `enigma/08-reference/06-objects/OperatingLocationCache.md` lists likely fields (operatingLocationId, brandId, latitude, longitude, latest12mCardRevenueProjected) but types/nullability are unverified. Confirm via schema introspection.
- **`Query` object type**: Synthesized from individual query pages (`search`, `aggregate`, `backgroundTask`, `account`, `listMaterialization`) — dedicated object page returns the docs landing page.
- **`ExternalMutation` object type**: Same synthesis from individual mutation pages — dedicated page returns docs landing page.
- **TEXT screening search type**: Documented in `enigma/05-screening/03-core-screening-endpoints.md` but "not yet open for public evaluation."
- **Email Address API coverage**: Per `enigma/09-data-attributes/03-legal-entity/04-email-address.md`, emails are "primarily available through the Contacts attribute, which is only available via file delivery, not in the API."

### 10.2 Pricing & Credit Surprises

- **Highest-tier-wins is per-entity.** Parent entity bills once. Each nested child bills separately at its own highest tier.
- **Nested compounding.** `first: 10` on a location connection × Premium attributes = 10 × 5 = 50 credits just for the nested level.
- **No caching.** Identical requests bill every time.
- **No charge on empty result.** Zero matches = zero credits.
- **Actions category.** The Billing page exposes a 4th category alongside Core/Plus/Premium for operational tasks (list materializations) — separate from attribute-read billing.
- **KYB and screening pricing is not documented in the attribute-tier framework.** They have their own pricing (not enumerated in the local source).

### 10.3 Rate-Limit Edge Cases

- GraphQL, KYB, and MCP tool limits are independent — exhausting one does not affect others.
- MCP limits are **rolling** 24-hour / 30-day windows (not calendar).
- Each MCP tool's quota is independent — `search_business` exhaustion doesn't affect `screen_customer`.
- Pro and Max plans have identical MCP rate limits.
- Enterprise limits are configurable (not published).
- Rate-limited response: `429 Slow Down`.

### 10.4 GraphQL Search Gotchas

- **`prompt` is Brand-only.**
- **`aggregate` supports `OPERATING_LOCATION` only**, with one allowed filter: `{EQ: ["operatingStatuses.operatingStatus", "Open"]}`.
- **Every search must include** name, website, or person first/last name. Or `prompt` + `output` for segmentation.
- **`collect()` math function requires `output`** in `SearchInput` (must be a background task).
- **Pagination:** can't combine `first` + `last`; `after` requires `first`; `before` requires `last`.
- **Responses >6 MB return HTTP 302** to a pre-signed S3 URL in the `Location` header. Clients that don't follow redirects miss the data.
- **`backgroundTask(id: String!)`** takes `String`, not `UUID`. UUIDs work as strings.

### 10.5 Data Coverage and Accuracy

- **Card revenue:** 67% of brands within ±30% of ground truth. Highest precision in <$100k and >$1M revenue buckets (>80%); moderate in $100k–$1M (>60%).
- **Brand vs. location revenue:** Brand revenue includes both in-store + online; location revenue is in-store only. Compare apples-to-apples.
- **Phone coverage:** 60% business / 69% location.
- **Role coverage:** 44% / 44%.
- **Address coverage:** 97% / 100%.
- **Bankruptcy:** 100% at both levels; history to the 1980s.
- **Watchlist accuracy:** with DOB 99.97% TPR / 0.4% FPR; without DOB 99.97% TPR / 5% FPR.
- **Nine states don't provide mailing addresses on registrations:** AL, DE, MS, NJ, NV, OH, OK, SC, WI.
- **Delaware and New Jersey don't provide registration status in bulk.**
- **Match precision** ~94% across all entity types (depends heavily on input quality).

### 10.6 MCP & AI Integration

- **Two endpoints, different auth:** `/http` (OAuth, user-authenticated) vs `/http-key` (API-key, for agents and direct JSON-RPC).
- **MCP server is in beta.** Connection drops are expected; documented troubleshooting is "disable and re-enable."
- **Claude Custom Connectors are in beta.**
- **Gov Archive requires Max or Enterprise plan.** 7,000+ datasets; Pro plan does **not** have access.
- **IdP-initiated SSO doesn't work** — users must start from Enigma login page.
- **Decision tools require `use_case_manager: true`** in config; otherwise decisions are not recorded.

### 10.7 KYB v1 → v2 Pitfalls

- Default package changed (`identify` → `verify`).
- NAICS upgraded 2017 → 2022 — same brand may show different codes.
- `match_threshold` values are not backward-compatible — re-evaluate on representative sample.
- UUIDs throughout v2 (was opaque strings in v1).
- Websites returned as full URLs (was domain-only).
- `name_approximate_match` renamed `name_match`.

### 10.8 Deprecated Items

Per `enigma/08-reference/10-deprecated/deprecated-items.md`: "no specific deprecated items are actively listed in the API reference" as of last update. Use `__schema` introspection with `isDeprecated` and `deprecationReason` to detect future deprecations programmatically.

### 10.9 Error Shape

The response-status-codes doc lists `200`, `202`, `302`, `400`, `401`, `402`, and elsewhere `429`. Other 4XX/5XX codes are not enumerated. Errors appear under the `errors` key in the response body on 400 responses, but the detailed error shape is not schematized in source docs.

---

*End of canonical reference.*

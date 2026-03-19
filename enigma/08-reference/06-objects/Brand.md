# Brand Object Type

## Overview

The `Brand` object represents a business brand entity within the Enigma GraphQL API. It implements the `NodeFunctions` and `Entity` interfaces, enabling comprehensive querying of brand-related data.

## Fields

### Identifiers
- **id** (`ID!`): Unique identifier for the brand
- **internalId** (`String`): Internal system identifier
- **enigmaId** (`String`): Enigma's proprietary identifier

### Metadata
- **tieBreakerMetadata** (`BrandTieBreakerMetadata`): Metadata used for resolving ambiguous matches
- **searchMetadata** (`Searchmetadata`): Search-related metadata
- **_fn** (`JSON`): Extended function field for custom projections

### Related Data Connections

#### Names and Identity
- **names** (`BrandNameConnection`): Brand names (default: 3 results)

#### Locations and Operations
- **websites** (`BrandWebsiteConnection`): Associated websites (default: 100 results)
- **operatingLocations** (`BrandOperatingLocationConnection`): Physical operating locations (default: 100 results)
- **locationDescriptions** (`BrandLocationDescriptionConnection`): Location descriptions (default: 3 results)

#### Business Relationships
- **legalEntities** (`BrandLegalEntityConnection`): Associated legal entities (default: 100 results)
- **affiliatedBrands** (`BrandBrandConnection`): Related brand entities (default: 100 results)
- **roles** (`BrandRoleConnection`): Associated roles (default: 100 results)

#### Financial and Market Data
- **cardTransactions** (`BrandCardTransactionConnection`): Card transaction data (default: 3 results)
- **revenueQualities** (`BrandRevenueQualityConnection`): Revenue quality metrics (default: 3 results)
- **industries** (`BrandIndustryConnection`): Industry classifications (default: 100 results)
- **isMarketables** (`BrandIsMarketableConnection`): Market eligibility status (default: 3 results)

#### Activity
- **activities** (`BrandActivityConnection`): Activity records (default: 3 results)

### Aggregation Functions

These functions support optional `conditions` parameters for filtering:
- **count** (`Int`): Count records by field
- **countDistinct** (`Int`): Count distinct values
- **has** (`Boolean`): Check field existence
- **sum**, **min**, **max** (`Int`): Numeric aggregations
- **avg** (`Float`): Average calculation
- **collect** (`String`): Concatenate field values
- **minDateTime**, **maxDateTime** (`DateTime`): Date-time range functions

## Connection Parameters

All connection fields support standard pagination arguments:
- **first** (`Int`): Limit results from start
- **last** (`Int`): Limit results from end
- **after** (`String`): Cursor-based pagination forward
- **before** (`String`): Cursor-based pagination backward
- **conditions** (`ConnectionConditions`): Filter conditions

## Type Relationships

### Implemented Interfaces
- `NodeFunctions`: Provides aggregation and analysis capabilities
- `Entity`: Base entity interface

### Used By
Multiple edge types reference Brand as the node object, including `BrandBrandEdge`, `BrandEdge`, and various cross-entity edges like `IndustryBrandEdge` and `LegalEntityBrandEdge`.

### Search Integration
The Brand object implements the `SearchUnion` union, making it discoverable through unified search queries.

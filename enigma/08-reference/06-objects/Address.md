# Address Object

## Overview

The `Address` object represents a physical street address associated with a business. It implements the `NodeFunctions` interface and conforms to USPS Publication 28 standards where applicable.

## Description

Addresses can range from complete street addresses with unit numbers to postal codes or city/state combinations. When unit-level information is available, distinct units in the same building are represented as separate address records. The system provides the current postal code even when historical data references a different code.

## Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID!` | Unique identifier (required) |
| `fullAddress` | `String` | Complete address without punctuation (e.g., "1223 18 MILE RD STERLING HEIGHTS MI 48314") |
| `streetAddress1` | `String` | Street number, name, type, and directional (USPS standard format) |
| `streetAddress2` | `String` | Unit, suite, floor, or additional details using USPS abbreviations |
| `city` | `String` | City name |
| `state` | `String` | Two-letter U.S. state or territory code |
| `zip` | `String` | Five-digit postal code |
| `county` | `String` | County designation |
| `country` | `String` | Three-digit ISO3 country code (typically null for USA addresses) |

## Geographic Fields

| Field | Type | Description |
|-------|------|-------------|
| `latitude` | `Float` | Approximate decimal latitude (not provided for all addresses) |
| `longitude` | `Float` | Approximate decimal longitude (not provided for all addresses) |
| `h3Index` | `String` | H3 geohash (resolution 10) for geo-hashing applications |
| `msa` | `String` | Metropolitan/Micropolitan Statistical Area |
| `csa` | `String` | Combined Statistical Area |

## Temporal Fields

| Field | Type |
|-------|------|
| `firstObservedDate` | `String` |
| `lastObservedDate` | `String` |

## Internal Fields

| Field | Type |
|-------|------|
| `internalId` | `String` |
| `internalAddressId` | `String` |

## Related Data Connections

- **operatingLocations**: Associated business operating locations
- **registrations**: Entity registration records at this address
- **deliverabilities**: Mail deliverability information (max 3 results)
- **watchlistEntries**: Watchlist matches at this address
- **legalEntities**: Registered business entities

All connections support pagination with `first`, `last`, `after`, `before` parameters and optional `conditions` filtering.

## Aggregate Functions

The object provides query functions for analytics:
- `count(field, conditions)` / `countDistinct(field, conditions)`
- `sum`, `min`, `max`, `avg` (numeric aggregations)
- `has(field, conditions)` (existence checks)
- `collect(field, separator, conditions)` (value concatenation)
- `minDateTime` / `maxDateTime` (temporal aggregations)

## Related Types

**Used By:**
- `LegalEntityAddressEdge`
- `OperatingLocationAddressEdge`
- `RegistrationAddressEdge`
- `WatchlistEntryAddressEdge`

**Implemented By:**
- `SearchUnion`

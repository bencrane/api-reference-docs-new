# OperatingLocationCache

> Source URL: https://documentation.enigma.com/reference/graphql_api/objects/operating-location-cache
> (The dedicated type page returned the generic docs overview on 2026-04-16. No other page on `documentation.enigma.com` indexes `OperatingLocationCache`, and the `OperatingLocation` object page makes no reference to it. The details below are inferred from a single upstream summary that surfaced when crawling the object index and should be treated as provisional.)

## Overview

`OperatingLocationCache` is described in upstream summaries as a type that "contains cached data for operating locations." It appears to be a denormalized read-optimized projection of an `OperatingLocation`, keyed by `operatingLocationId` and `brandId`, with cached geo coordinates and rolling financial metrics.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `operatingLocationId` | (unknown, likely `ID!` or `String!`) | — | Identifier of the source `OperatingLocation`. |
| `brandId` | (unknown, likely `ID` or `String`) | — | Identifier of the owning `Brand`, if any. |
| `latitude` | (unknown, likely `Float`) | — | Cached latitude of the operating location. |
| `longitude` | (unknown, likely `Float`) | — | Cached longitude of the operating location. |
| `latest12mCardRevenueProjected` | (unknown, likely a numeric scalar) | — | Cached rolling 12-month projected card revenue metric. |

Exact GraphQL types and nullability could not be verified — the dedicated type page was not reachable and these field names come from a secondary summary.

## Interfaces Implemented

Unknown.

## Type Membership

- **Member of Edge(s):** None documented
- **Member of Connection(s):** None documented
- **Member of Union(s):** None documented
- **Referenced by Input(s):** None documented
- **Referenced by Object(s):** Not referenced on the `OperatingLocation` object page; the path from the rest of the schema to this type could not be traced from the public docs.

## Source

- https://documentation.enigma.com/reference/graphql_api/objects/operating-location-cache (returned overview page — no type reference content)
- Field names above surfaced from an object-index summary only; they should be confirmed against the live schema via introspection before being used as a specification.

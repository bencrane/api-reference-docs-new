# BrandIndustryEdge

## Overview

The `BrandIndustryEdge` type represents "a Relay edge containing a `BrandIndustry` and its cursor." This object type is used within the Enigma GraphQL API for pagination and relationship traversal in brand-industry connections.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `node` | `Industry` | The item at the end of the edge |
| `cursor` | `String!` | "A cursor for use in pagination" |
| `id` | `ID` | Unique identifier |
| `brandDoesBusinessWithinIndustryId` | `UUID` | Identifier for the brand-industry relationship |
| `datasetIds` | `JSON` | Dataset identifiers associated with the relationship |
| `firstObservedDate` | `String` | Date when the relationship was first observed |
| `lastObservedDate` | `String` | Date when the relationship was most recently observed |
| `rank` | `Int` | Ranking value for the relationship |
| `internalId` | `String` | Internal identifier |
| `internalBrandDoesBusinessWithinIndustryId` | `String` | Internal identifier for the brand-industry relationship |

## Relationships

- **Part of:** `BrandIndustryConnection` object
- **Contains:** `Industry` object as the node value

## Context

This edge type follows the Relay cursor connection specification, enabling efficient pagination through collections of brand-industry relationships within the broader Enigma data model.

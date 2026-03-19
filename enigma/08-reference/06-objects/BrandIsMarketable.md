# BrandIsMarketable

## Overview

The `BrandIsMarketable` object is a GraphQL type that provides information about whether a brand meets criteria for marketing purposes.

## Description

This type contains a boolean value that indicates whether a brand qualifies as marketable based on specific business metrics.

## Data Source Criteria

A brand achieves marketable status when it satisfies certain conditions, including:
- Presence of active operating locations
- Revenue generation within the previous 12 months
- Customer reviews posted within the previous 12 months

## Field Reference

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID!` | Unique identifier (required) |
| `firstObservedDate` | `String` | Initial observation timestamp |
| `lastObservedDate` | `String` | Most recent observation timestamp |
| `isMarketable` | `Boolean` | Boolean flag indicating marketability status |
| `internalId` | `String` | Internal identifier |
| `internalBrandId` | `String` | Internal brand reference identifier |

## Aggregation Methods

The type implements `NodeFunctions` interface, providing:
- `count()` – Count records matching conditions
- `countDistinct()` – Count unique values
- `has()` – Test field existence
- `sum()` – Sum numeric values
- `min()` / `max()` – Minimum/maximum values
- `avg()` – Calculate averages
- `collect()` – Aggregate field values with separator
- `minDateTime()` / `maxDateTime()` – DateTime extremes

## Relationships

This object appears as a member of the `BrandIsMarketableEdge` type within connection structures.

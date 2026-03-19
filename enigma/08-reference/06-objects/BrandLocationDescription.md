# BrandLocationDescription

## Overview

The `BrandLocationDescription` GraphQL object provides a human-readable summary of a brand's geographic footprint based on its operating locations.

## Description

This object generates textual descriptions showing where a brand operates geographically. For multi-location brands, it displays "up to 5 states where the brand has a significant presence, listed alphabetically." A state qualifies as significant with either more than 10% of locations or more than 5 locations. When additional significant states exist beyond the top 5, the description appends "and others."

For single-location brands, the description shows "the specific city and state of that location" (e.g., "San Francisco, CA").

## Time Structure

This attribute does not include time series data and reflects the current state of brand locations.

## Data Sources

The object derives data from:
- Brand to operating location relationships
- Operating location to address relationships
- Address state and city information

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID!` | Unique identifier |
| `firstObservedDate` | `String` | Initial observation date |
| `lastObservedDate` | `String` | Most recent observation date |
| `locationDescription` | `String` | Text description of geographic presence based on operating locations |
| `internalId` | `String` | Internal reference identifier |
| `internalBrandId` | `String` | Internal brand identifier |
| `count` | `Int` | Count aggregation function |
| `countDistinct` | `Int` | Distinct count aggregation function |
| `has` | `Boolean` | Existence check function |
| `sum` | `Int` | Sum aggregation function |
| `min` | `Int` | Minimum value function |
| `max` | `Int` | Maximum value function |
| `avg` | `Float` | Average value function |
| `collect` | `String` | Collection/concatenation function |
| `minDateTime` | `DateTime` | Minimum datetime function |
| `maxDateTime` | `DateTime` | Maximum datetime function |
| `_fn` | `JSON` | Function metadata |

## Interfaces

- `NodeFunctions` - Provides aggregation and data functions

## Related Types

- Member of: `BrandLocationDescriptionEdge`

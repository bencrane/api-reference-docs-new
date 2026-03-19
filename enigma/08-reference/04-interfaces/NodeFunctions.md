# NodeFunctions Interface

## Overview

The `NodeFunctions` interface provides aggregation and analytical operations for querying data within the Enigma GraphQL API.

## Fields

| Field | Type | Arguments | Purpose |
|-------|------|-----------|---------|
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Counts records matching specified criteria |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Counts unique values in a field |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Checks field existence given conditions |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sums numeric field values |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Returns minimum numeric value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Returns maximum numeric value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Calculates average of numeric values |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Aggregates field values into delimited string |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Returns earliest datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Returns latest datetime value |
| `_fn` | `JSON` | — | Advanced function metadata |

## Implementing Types

This interface is implemented by 39 object types including:
- Address-related objects (Address, AddressDeliverability)
- Brand objects (Brand, BrandActivity, BrandCardTransaction, etc.)
- Entity objects (LegalEntity, Person, RegisteredEntity)
- Location data (OperatingLocation and variants)
- Contact information (EmailAddress, PhoneNumber, Website)

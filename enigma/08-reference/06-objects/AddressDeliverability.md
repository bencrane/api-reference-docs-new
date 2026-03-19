# AddressDeliverability

## Overview

The `AddressDeliverability` type represents USPS delivery information for physical business addresses, conforming to standards in "USPS Publication 28" where applicable. It provides details about whether an address can receive mail and its delivery characteristics.

## Type Definition

```graphql
type AddressDeliverability implements NodeFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  rdi: String
  deliveryType: String
  deliverable: String
  virtual: String
  internalId: String
  internalAddressId: String
  count(field: String!, conditions: Conditions): Int
  countDistinct(field: String!, conditions: Conditions): Int
  has(field: String!, conditions: Conditions): Boolean
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
  _fn: JSON
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID!` | Unique identifier |
| `firstObservedDate` | `String` | Date when address information was first recorded |
| `lastObservedDate` | `String` | Date of most recent observation |
| `rdi` | `String` | Residential Delivery Indicator classifying address as Residential or Commercial for postal purposes |
| `deliveryType` | `String` | Mail delivery method: Street, Multi-Tenant Building, Post Office Box, Firm, Rural Route, General Delivery, or null if undetermined |
| `deliverable` | `String` | Status indicating whether address is deliverable, vacant, not deliverable, or unknown |
| `virtual` | `String` | Whether address is virtual/CMRA-associated or a standard location |
| `internalId` | `String` | Internal reference identifier |
| `internalAddressId` | `String` | Internal address reference identifier |

## Aggregate Functions

The type implements `NodeFunctions`, providing aggregation capabilities: `count`, `countDistinct`, `has`, `sum`, `min`, `max`, `avg`, `collect`, `minDateTime`, and `maxDateTime`.

## Interfaces

- **NodeFunctions**: Provides query and aggregation functionality

## Related Types

- Part of `AddressDeliverabilityEdge` object

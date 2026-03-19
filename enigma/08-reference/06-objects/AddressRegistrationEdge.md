# AddressRegistrationEdge

## Overview

The `AddressRegistrationEdge` represents a Relay-compliant edge structure used in pagination, containing a `Registration` node along with pagination metadata and address-related attributes.

## Type Definition

```graphql
type AddressRegistrationEdge {
  node: Registration
  cursor: String!
  registrationRecordedAddressId: UUID
  addressType: String
  rank: Int
  id: ID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalRegistrationRecordedAddressId: String
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `node` | `Registration` | The registration entity at the end of this edge |
| `cursor` | `String!` | Required pagination cursor for use in subsequent requests |
| `registrationRecordedAddressId` | `UUID` | Unique identifier for the registration's recorded address |
| `addressType` | `String` | Classification of the address type |
| `rank` | `Int` | Numeric ranking value for the address registration |
| `id` | `ID` | Unique identifier for the edge |
| `datasetIds` | `JSON` | Set of dataset identifiers associated with this edge |
| `firstObservedDate` | `String` | Initial observation date for this record |
| `lastObservedDate` | `String` | Most recent observation date for this record |
| `internalId` | `String` | Internal system identifier |
| `internalRegistrationRecordedAddressId` | `String` | Internal system identifier for registration address |

## Relationships

- **Member of:** `AddressRegistrationConnection` — appears as an element within connection results

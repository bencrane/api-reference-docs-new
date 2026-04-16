# Tin

## Overview

A Taxpayer Identification Number (TIN) is an identification number assigned by the IRS for tax administration. TIN data is available on Legal Entities and is commonly used in business verification and KYB workflows. Both EINs (Employer Identification Numbers) and SSNs (Social Security Numbers) are types of TIN. Currently provided data is primarily EIN records from government sources like Secretary of State registrations and IRS forms.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `tin` | `String` | — | The 9-digit taxpayer identification number assigned by the IRS |
| `tinType` | `String` | — | Type of TIN: EIN, SSN, ITIN, ATIN, or PTIN (currently EIN only) |
| `validity` | `String` | — | Validity status when verified against IRS: issued, not_issued, invalid, or null |
| `firstObservedDate` | `String` | — | Date when TIN was first observed |
| `lastObservedDate` | `String` | — | Date when TIN was last observed |
| `internalId` | `String` | — | Internal identifier |
| `internalTinId` | `String` | — | Internal TIN identifier |
| `legalEntities` | `TinLegalEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Connected legal entities |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Boolean existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values with separator |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `LegalEntityTinEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `LegalEntity`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/tin

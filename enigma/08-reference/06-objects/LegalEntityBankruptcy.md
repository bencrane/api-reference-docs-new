# LegalEntityBankruptcy

## Overview

Captures bankruptcy filing details for legal entities, including chapter type, filing date, and case number. All bankruptcy cases are handled in federal courts under rules outlined in the U.S. Bankruptcy Code.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | No description |
| `lastObservedDate` | `String` | — | No description |
| `debtorName` | `String` | — | The debtor's name on the filing |
| `trustee` | `String` | — | Trustee appointed by the U.S. Trustee Program who oversees the process, ensuring fair asset distribution and creditor repayment |
| `judge` | `String` | — | Name of the bankruptcy court judge presiding over the case |
| `filingDate` | `Date` | — | The date the bankruptcy was filed |
| `chapterType` | `String` | — | Chapter designation under U.S. Bankruptcy Code (e.g., Chapter 7 or 11 for businesses) |
| `caseNumber` | `String` | — | Case identifier where digits represent district court number, filing year, "bk" for bankruptcy, and sequence number |
| `petition` | `String` | — | Indicates voluntary filing by debtor or involuntary filing initiated by creditors |
| `entryDate` | `Date` | — | Date when the case was entered |
| `dateConverted` | `Date` | — | Date when the case was converted from chapter 11 to chapter 7 |
| `dateDismissed` | `Date` | — | Date when the case was dismissed from court |
| `dateTerminated` | `Date` | — | Final docket entry date; bankruptcy case closed |
| `debtorDischargedDate` | `Date` | — | Date when debtor completed plan repayments and plan is fulfilled |
| `planConfirmedDate` | `Date` | — | Date when the plan was confirmed |
| `internalId` | `String` | — | No description |
| `internalLegalEntityId` | `String` | — | No description |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation function |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value aggregation |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value aggregation |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value aggregation |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect aggregation function |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime aggregation |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime aggregation |
| `_fn` | `JSON` | — | No description |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `LegalEntityBankruptcyEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `LegalEntity`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-bankruptcy

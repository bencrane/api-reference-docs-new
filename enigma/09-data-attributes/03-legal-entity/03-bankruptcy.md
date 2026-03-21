# Bankruptcy

## Description
The Business Bankruptcy attribute provides comprehensive details about bankruptcy filings for legal entities. All bankruptcy cases are handled in federal courts under rules outlined in the U.S. Bankruptcy Code.

## Tier
Premium

## Applies To
- Legal Entity

## Chapter Types
- **Chapter 7**: Liquidation
- **Chapter 11**: Reorganization
- **Chapter 12**: Family farmer/fisherman
- **Chapter 13**: Individual debt adjustment
- **Chapter 15**: International bankruptcy

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| bankruptcy_flag | String | Boolean indicator of any bankruptcy filings |
| caseNumber | String | Federal case identifier (format: district-year-bk-sequence) |
| chapterType | String | Bankruptcy classification |
| petition | String | Filing type (voluntary or involuntary) |
| filingDate | Date | Date of bankruptcy filing (YYYY-MM-DD) |
| entryDate | Date | Case entry into system |
| dateConverted | Date | Conversion between chapters |
| dateDismissed | Date | Final docket entry date, case closed |
| dateTerminated | Date | Court enters date when plan is fulfilled |
| debtorDischargedDate | Date | Date when plan was confirmed/fulfilled |
| planConfirmedDate | Date | Plan confirmation date |
| debtorName | String | Name on the filing |
| judge | String | Presiding bankruptcy court judge |
| trustee | String | Court-appointed trustee |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Coverage
- Business coverage: 100%
- Business Locations coverage: 100%
- 100% fill rate on business bankruptcy

## Data Source
Public Access to Court Electronic Records (PACER)

## Historical Depth
Bankruptcy filings dating back to the 1980s

## Access
Requires account activation via sales team, retrieved using `attrs` parameter

## Sources
- https://developers.enigma.com/docs/business-bankruptcy
- https://documentation.enigma.com/reference/attributes/legal-entity-bankruptcy
- https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-bankruptcy

## Last Updated
March 11, 2026

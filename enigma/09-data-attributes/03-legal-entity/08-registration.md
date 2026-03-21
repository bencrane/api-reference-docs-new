# Registration

## Description
Enigma KYB collects and verifies corporate registrations associated with businesses by sourcing data from Secretary of State filings. These registrations either establish a legal entity in that state ("domestic") or allow an existing entity to conduct business there ("foreign").

## Tier
Premium

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier |
| fileNumber | String | Unique identifier for corporate registration filing |
| registeredName | String | Official business name on registration |
| issueDate | Date | Filing date (YYYY-MM-DD format) |
| expirationDate | Date | When registration expires, if applicable |
| registrationState | String | Two-letter state code where filed |
| homeJurisdictionState | String | Two-letter abbreviation of business home state |
| jurisdictionType | String | "domestic" or "foreign" status |
| registrationType | String | Legal form as designated by Secretary of State |
| status | String | "active," "inactive," or "unknown" |
| subStatus | String | Detailed status classification |
| statusDetail | String | Official state-provided status message |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Sub-Status Values
- good_standing
- not_good_standing
- pending_active
- pending_inactive
- unknown
- null

## Package-Dependent Attributes
- **Verify Package**: Returns all child attributes including status fields
- **Identify Package**: Returns restricted subset (file_number, registered_name, addresses, persons, issue_date, registration_state)

## Coverage
- All 50 US states plus DC and Puerto Rico
- ~48M active filings, ~57M inactive, ~11M unknown status (August 2024)
- ~105M distinct legal entities identified
- Delaware and New Jersey don't provide status in bulk data
- Nine states lack mailing address data

## Updates
Weekly

## Ordering
When multiple filings exist, domestic filing listed first, followed by foreign filings ordered oldest to newest

## Sources
- https://developers.enigma.com/docs/registrations
- https://documentation.enigma.com/reference/graphql_api/objects/registration

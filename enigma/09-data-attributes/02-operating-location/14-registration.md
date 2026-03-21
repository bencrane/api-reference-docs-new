# Registration

## Description
Business registrations filed with a Secretary of State (or equivalent) in a U.S. state or territory.

## Tier
Premium

## Applies To
- Brand
- Operating Location
- Legal Entity

## Key Details
Represents either new legal entities ("domestic" registrations) or existing entities authorized to operate in additional states ("foreign" registrations). These are "a source of truth about that business."

## Sub-Status Values
- good_standing
- not_good_standing
- pending_active
- pending_inactive
- unknown
- null

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| fileNumber | String | Registration file number |
| registeredName | String | Registered business name |
| issueDate | String | Registration issue date |
| expirationDate | String | Registration expiration date |
| registrationState | String | State where registered |
| homeJurisdictionState | String | Home jurisdiction state |
| jurisdictionType | String | Jurisdiction type (domestic/foreign) |
| registrationType | String | Registration type |
| status | String | Current status |
| statusDetail | String | Detailed status information |
| subStatus | String | Sub-status category |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/registration

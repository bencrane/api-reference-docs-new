# Registration

## Description
Business registration data filed with state Secretaries of State.

## Tier
Premium

## Registration Types
- **Domestic**: Entity created in-state
- **Foreign**: Entity operating cross-state

## Fields

| Field | Type | Description |
|-------|------|-------------|
| fileNumber | String | Registration file number |
| registeredName | String | Registered business name |
| issueDate | String | Registration issue date |
| expirationDate | String | Registration expiration date |
| registrationState | String | State where registered |
| homeJurisdictionState | String | Home jurisdiction state |
| jurisdictionType | String | Type of jurisdiction |
| registrationType | String | Type of registration (Domestic/Foreign) |
| status | String | Current registration status |
| statusDetail | String | Detailed status information |
| subStatus | String | Sub-status category |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/registration

# Email Address

## Description
The EmailAddress object represents email addresses associated with businesses or individuals connected to a business through roles.

## Tier
Core

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| emailAddress | String | Complete email address including username, @, and domain |
| id | UUID | Unique identifier |
| firstObservedDate | String | When email was first detected |
| lastObservedDate | String | Most recent observation timestamp |

## Key Notes
- Email addresses are primarily available through the Contacts attribute, which is only available via file delivery (not in the API)
- Not all contacts include email addresses
- Email campaigns optimized for <4% bounce rates

## Sources
- https://developers.enigma.com/docs/contacts
- https://documentation.enigma.com/reference/graphql_api/objects/email-address

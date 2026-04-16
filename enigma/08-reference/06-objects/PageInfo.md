# PageInfo

## Overview

The Relay compliant `PageInfo` type, containing data necessary to paginate through connection results.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `hasNextPage` | `Boolean!` | — | When paginating forwards, are there more items? |
| `hasPreviousPage` | `Boolean!` | — | When paginating backwards, are there more items? |
| `startCursor` | `String` | — | When paginating backwards, the cursor to continue. |
| `endCursor` | `String` | — | When paginating forwards, the cursor to continue. |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** AddressDeliverabilityConnection, AddressLegalEntityConnection, AddressOperatingLocationConnection, AddressRegistrationConnection, AddressWatchlistEntryConnection, BrandActivityConnection, BrandBrandConnection, BrandCardTransactionConnection, BrandConnection, BrandIndustryConnection, BrandIsMarketableConnection, BrandLegalEntityConnection, BrandLocationDescriptionConnection, BrandNameConnection, BrandOperatingLocationConnection, BrandRevenueQualityConnection, BrandRoleConnection, BrandWebsiteConnection, EmailAddressRoleConnection, IndustryBrandConnection, IndustryIndustryConnection, LegalEntityAddressConnection, LegalEntityAppearsOnWatchlistEntryConnection, LegalEntityBankruptcyConnection, LegalEntityBrandConnection, LegalEntityIsFlaggedByWatchlistEntryConnection, LegalEntityLegalEntityConnection, LegalEntityNameConnection, LegalEntityOperatingLocationConnection, LegalEntityPersonConnection, LegalEntityRegisteredEntityConnection, LegalEntityRoleConnection, LegalEntityTinConnection, LegalEntityTypeConnection, ListConnection, ListMaterializationBillingEventDetailConnection, ListMaterializationConnection, ListMaterializationMetricConnection, OperatingLocationAddressConnection, OperatingLocationBrandConnection, OperatingLocationCardTransactionConnection, OperatingLocationIsMarketableConnection, OperatingLocationLegalEntityConnection, OperatingLocationLocationTypeConnection, OperatingLocationNameConnection, OperatingLocationOperatingStatusConnection, OperatingLocationPhoneNumberConnection, OperatingLocationRankConnection, OperatingLocationRevenueQualityConnection, OperatingLocationReviewSummaryConnection, OperatingLocationRoleConnection, OperatingLocationTechnologiesUsedConnection, OperatingLocationWebsiteConnection, PersonLegalEntityConnection, PersonNameConnection, PhoneNumberOperatingLocationConnection, PhoneNumberRoleConnection, RegisteredEntityLegalEntityConnection, RegisteredEntityRegistrationConnection, RegistrationAddressConnection, RegistrationRegisteredEntityConnection, RegistrationRoleConnection, ReviewSummaryOperatingLocationConnection, RoleBrandConnection, RoleEmailAddressConnection, RoleLegalEntityConnection, RoleOperatingLocationConnection, RolePhoneNumberConnection, RoleRegistrationConnection, TinLegalEntityConnection, WatchlistEntryAddressConnection, WatchlistEntryAppearsOnLegalEntityConnection, WatchlistEntryIsFlaggedByLegalEntityConnection, WebsiteBrandConnection, WebsiteContentWebsiteConnection, WebsiteOnlinePresenceConnection, WebsiteOperatingLocationConnection, WebsiteTechnologiesUsedConnection, WebsiteWebsiteContentConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** All Connection objects listed above

## Source

https://documentation.enigma.com/reference/graphql_api/objects/page-info

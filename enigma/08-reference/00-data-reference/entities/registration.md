> Source: https://documentation.enigma.com/reference/data/entities/registration/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/registration/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesRegistrationOn this pageRegistration
A business registration filed with a Secretary of State (or equivalent) in a U.S. state or
territory. Registrations either create a legal entity in that state ("domestic" registrations)
or allow an existing entity to do business in that state ("foreign" registrations), and are a
primary source of truth about the legal aspect of a business.
GraphQL type: Registration
ExampleStarbucks Corporation's UBI filing in Washington State is a Registration — a single Secretary of State record tied to the registered entity.
Business registrations filed with a Secretary of State (or equivalent) in a U.S. state or territory.
Pricing tier: Premium
FieldNameTypeDescriptionRegistration Typeregistration_typeThe legal form of the registered entity, as given by the regististering jurisdiction's Secretary of State.Expiration Dateexpiration_dateThe registration's expiration, if any.Jurisdiction Statejurisdiction_stateThe US state where the registration was filed.Jurisdiction Typejurisdiction_typeforeign if the registration is for any state other than the business's home state; otherwise, domestic.Home Jurisdiction Statehome_jurisdiction_stateTwo-letter abbreviation for the state jurisdiction of the business.Registered Nameregistered_nameBusiness name as on the registration filing.File Numberfile_numberFile number of the registration filing.Issue Dateissue_dateIssue date of the registration filing, formatted YYYY/MM/DD.Statusstandardized_registration_statusStatus field indicating whether the registration is active or inactive.Sub-Statusstandardized_registration_sub_statusIf available from the state, a normalized sub-status for the business. Possible values are: [good_standing, not_good_standing, pending_active, pending_inactive, unknown, null]Status Detailregistration_statusIf available, the official filing status message provided by the state.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Registration connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity→recordedAddress→recordedRole→registeredRegistered Entity
View all relationships →Last updated on Apr 6, 2026PreviousRegistered EntityNextReview SummaryRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---

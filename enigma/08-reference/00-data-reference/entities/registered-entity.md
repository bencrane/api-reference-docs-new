> Source: https://documentation.enigma.com/reference/data/entities/registered-entity/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/registered-entity/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesRegistered EntityOn this pageRegistered Entity
A business that has become a legal entity by registering with a U.S. Secretary of State (SoS).
A business may form in one state ("domestic registration") and register with other states to
conduct business there ("foreign registration"). Enigma joins these records together to
represent the single entity they constitute. Each state's SoS is the ultimate source of truth
for these records.
GraphQL type: RegisteredEntity
ExampleStarbucks Corporation, registered with the Washington Secretary of State, is a Registered Entity — the formal corporate filing behind the legal entity.
Businesses which have become legal entities by registering with a U.S. Secretary of State (SoS).
Pricing tier: Premium
FieldNameTypeDescriptionFormation Dateformation_datedateThe earliest non-null issue_date from the entity's registrations, formatted YYYY-MM-DD.Formation Yearformation_yearintegerThe year (YYYY) of the earliest non-null issue_date from the entity's registrations.Namestandardized_nameThis is the standardized name of the entity, derived from the name as listed on the entity's registration.Registered Entity Typeregistered_entity_typeThe standardized legal form of the entity, e.g. "Corporation", "LLC", etc.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Registered Entity connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity→is instance ofLegal Entity←registeredRegistration
View all relationships →Last updated on Apr 6, 2026PreviousPhone NumberNextRegistrationRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---

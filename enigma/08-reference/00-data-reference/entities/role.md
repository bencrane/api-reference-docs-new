> Source: https://documentation.enigma.com/reference/data/entities/role/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/role/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesRoleOn this pageRole
A role held by a person or other legal entity at a U.S. business. Roles include both
governance roles (such as owner, founder, and board member) typically sourced from business
registrations, and functional roles (such as CEO, VP, and manager) sourced from employee
contact data. Job titles are standardized: abbreviations are expanded, accented characters
normalized, and separators replaced.
GraphQL type: Role
ExampleCEO at Starbucks Corporation is a Role entity — it connects a Person (the CEO) to a Brand (Starbucks) through a specific business function.
Available from: Legal Entity
These are roles which people (and other legal entities) hold at U.S. businesses.
Pricing tier: Plus
FieldNameTypeDescriptionExternal IDexternal_idstructExternal URLexternal_urlstringJob Titlestandardized_job_titleThe standardized job title observed in our datasets.Job Functionstandardized_job_functionThe standardized job description for this role.Management Levelstandardized_management_levelThe standardized management level for this role.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Role connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←performsLegal Entity←recordedRegistration→is associated withEmail Address→is associated withPhone Number→is performed atBrand→is performed atOperating Location
View all relationships →Last updated on Apr 6, 2026PreviousReview SummaryNextTaxpayer Identification Number (TIN)Relationships
--- END UNTRUSTED EXTERNAL CONTENT ---

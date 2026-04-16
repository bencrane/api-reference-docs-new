> Source: https://documentation.enigma.com/reference/data/entities/tin/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/tin/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesTaxpayer Identification Number (TIN)On this pageTaxpayer Identification Number (TIN)
A Taxpayer Identification Number (TIN) used by the Internal Revenue Service (IRS) in the
administration of tax laws.
GraphQL type: Tin
ExampleA TIN (EIN) is linked to Starbucks Corporation through the files taxes using relationship, identifying the entity for IRS tax administration.
Available from: Legal Entity
Taxpayer Identification Number (TIN). Identification number used by the Internal Revenue Service (IRS) in the administration of tax laws.
Pricing tier: Premium
FieldNameTypeDescriptionTINstandardized_tinThe taxpayer identification number. A 9-digit number assigned by the IRS.TIN Typetin_typeThe type of TIN on record, such as EIN or SSN. In practice, we currently provide EIN data.ValidityvalidityVerification status for a business and TIN combination when checked against live IRS records.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Taxpayer Identification Number (TIN) connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←files taxes usingLegal Entity
View all relationships →Last updated on Apr 6, 2026PreviousRoleNextWatchlist EntryRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---

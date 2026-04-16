> Source: https://documentation.enigma.com/reference/data/entities/industry/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/industry/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesIndustryOn this pageIndustry
The industry within which the business operates.
Multiple distinct classification systems have been created to describe a business's activity
(such as NAICS, SIC, and MCC). Rather than selecting one, Enigma provides multiple different
classifications for each business via the industry_type, industry_code, and industry_desc
fields. We also provide a non-hierarchical enigma_industry_description that gives a more
colloquial indication of the business's primary activity, useful when standard systems like
NAICS lack the expressiveness to distinguish between similar business types.
GraphQL type: Industry
ExampleStarbucks is classified under NAICS 722515 — Snack and Nonalcoholic Beverage Bars — an Industry entity linked to the Starbucks brand.
Available from: Brand
The industry within which the business operates.
Pricing tier: Core
FieldNameTypeDescriptionIndustry Descriptionindustry_descstringHuman-readable description of the industry.Industry Codeindustry_codestringNumeric industry code. Used for naics_2017_code, naics_2022_code, sic_code, and mcc_code.Industry Typeindustry_typestringHuman-readable description of the industry classification system (e.g. Enigma Industry Description, NAICS, MCC, etc.)IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Industry connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←does business withinBrand→is parent ofIndustry
View all relationships →Last updated on Apr 6, 2026PreviousEmail AddressNextPhone NumberRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---

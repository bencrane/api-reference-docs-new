> Source: https://documentation.enigma.com/reference/data/relationships/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/relationships/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesRelationshipsRelationshipsOn this page
Entity Relationships​
Entities in the Enigma graph are connected by typed, directed relationships. When querying the API, you traverse relationships to reach data on connected entities — for example, navigating from a Brand through its operating locations to their addresses.
Every relationship has an assertion type: positive (the relationship exists) or negative (the relationship explicitly does not exist — a rare but meaningful signal).
Core relationships​
These connect the four primary entities to each other and to supporting entities.
Brand​
VerbTargetDescriptiondoes business withinIndustryLinks a brand to its industry classifications.is affiliated withBrandLinks a brand to other brands it is affiliated with.operates atOperating LocationLinks a brand to the operating locations where it conducts business.operates websiteWebsiteLinks a brand to its associated websites.
Operating Location​
VerbTargetDescriptioncan be called atPhone NumberLinks an operating location to its phone number(s).is subject ofReview SummaryLinks an operating location to its aggregated customer review summary.operates atAddressLinks an operating location to its physical address(es).operates websiteWebsiteLinks an operating location to its associated websites.
Legal Entity​
VerbTargetDescriptiondoes business asBrandLinks a legal entity to the brands it operates under.files taxes usingTaxpayer Identification Number (TIN)Links a legal entity to its tax identification number(s).ownsLegal EntityLinks a legal entity to other legal entities it owns.owns locationOperating LocationLinks a legal entity to the operating locations it owns or is responsible for.performsRoleLinks a legal entity to the roles it performs at other businesses.receives mail atAddressLinks a legal entity to a mailing address.
Person​
VerbTargetDescriptionis instance ofLegal EntityLinks a person to their corresponding legal entity record.
Other​
FromVerbToIndustryis parent ofIndustryRegistered Entityis instance ofLegal EntityRegistrationrecordedAddressRegistrationrecordedRoleRegistrationregisteredRegistered EntityRoleis associated withEmail AddressRoleis associated withPhone NumberRoleis performed atBrandRoleis performed atOperating LocationWebsiteservesWebsite Content
Relationships with attributes​
Most relationships are pure links. Two carry their own data fields:
Brand affiliations​
The brand → is affiliated with → brand relationship includes an affiliation type describing the nature of the connection:
merged · acquired · rebranded · sub_brand · agent · co_branded · co_located · dealer · divested · franchisee · joint_venture · licensee · location_type · ownership · partnership · reseller · service · supplier
TIN verification​
The legal_entity → files taxes using → tin relationship includes verification status:
FieldValuesverification_resulttin_verified, tin_not_verified, not_completed, errorverification_statusSuccess, Failure, or null
Watchlist and screening​
Several relationships connect entities to watchlist screening results:
FromVerbToAddressappears onWatchlist EntryLegal Entityappears onWatchlist EntryLegal Entityis flagged byWatchlist Entry
These are used by the KYB and Screening workflows.Last updated on Mar 26, 2026PreviousWebsite ContentCore relationshipsBrandOperating LocationLegal EntityPersonOtherRelationships with attributesBrand affiliationsTIN verificationWatchlist and screening
--- END UNTRUSTED EXTERNAL CONTENT ---

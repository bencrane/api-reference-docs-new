> Source: https://documentation.enigma.com/reference/data/entities/website/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/website/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesWebsiteOn this pageWebsite
A website associated with a business. Website URLs are decomposed into their component parts
(subdomain, domain, top-level domain, path) for filtering and analysis. A business may be
associated with multiple websites.
GraphQL type: Website
Examplestarbucks.com is a Website entity linked to the Starbucks brand, with URL components (domain, path, TLD) parsed into structured fields.
Available from: Brand, Operating Location
A website associated with a business.
Pricing tier: Core
FieldNameTypeDescriptionWebsitestandardized_websiteThe complete url of the website including protocol, subdomain and pathSubdomainstandardized_subdomainThe subdomain component of the website (e.g. "documentation" in "https://documentation.enigma.com/getting_started/introduction")Domainstandardized_domainThe subdomain component of the website (e.g. "enigma" in "https://documentation.enigma.com/getting_started/introduction")Top Level Domainstandardized_top_level_domainThe top_level_domain (a.k.a. tld) component of the website (e.g. "com" in "https://documentation.enigma.com/getting_started/introduction")Pathstandardized_pathThe path component of the website (e.g. "getting_started/introduction" in "https://documentation.enigma.com/getting_started/introduction")Fragmentstandardized_fragmentThe fragment component of the website (e.g. "getting_started/introduction" in "https://documentation.enigma.com/getting_started/introduction")Querystandardized_queryThe query component of the website (e.g. "getting_started/introduction" in "https://documentation.enigma.com/getting_started/introduction")Path Parametersstandardized_path_paramsThe path parameters component of the website (e.g. "getting_started/introduction" in "https://documentation.enigma.com/getting_started/introduction")IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Online Presence​
Indicates whether a website is an e-commerce website that sells products directly online.
Pricing tier: Core
FieldNameTypeDescriptionHas Online Saleshas_online_salesstringTwo possible values: [Yes, null]. Yes suggests website is an e-commerce website selling products directly online, while null suggests insufficient information.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Technologies Used​
Indicates third-party technologies used by a website.
Pricing tier: Premium
FieldNameTypeDescriptionTechnologytechnologystringThis field represents the specific third-party technology being used by the website.CategorycategorystringThis field represents the category of the third-party technology being used by the website. An example would be "payments"IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Website connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←operates websiteBrand←operates websiteOperating Location→servesWebsite Content
View all relationships →Last updated on Apr 6, 2026PreviousWatchlist EntryNextWebsite ContentOnline PresenceTechnologies UsedRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---

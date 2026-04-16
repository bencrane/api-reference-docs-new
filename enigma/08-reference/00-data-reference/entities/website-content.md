> Source: https://documentation.enigma.com/reference/data/entities/website-content/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/website-content/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesWebsite ContentOn this pageWebsite Content
The state of a website's content at a particular point in time. Enigma makes a request to each website
at least every ninety days, and each website content record represents what was learned on one
of those requests.
GraphQL type: WebsiteContent
ExampleA snapshot of starbucks.com captured on a specific date is a Website Content entity — it records the page state at a point in time.
The state of the website at a particular time.
Pricing tier: Plus
FieldNameTypeDescriptionWebsite Availabilitywebsite_availabilitystringHTTP Status Codehttp_status_codeThe HTTP status code returned by the request (e.g. 200, 404, etc.)Favicon URLfavicon_urlThe url from which the website's favicon was served.Favicon Imagefavicon_imageA binary representation of the website's favicon that was returned from the HTTP request.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Website Content connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←servesWebsite
View all relationships →Last updated on Apr 6, 2026PreviousWebsiteNextRelationshipsRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---

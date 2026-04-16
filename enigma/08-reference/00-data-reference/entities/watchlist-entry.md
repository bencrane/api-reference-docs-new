> Source: https://documentation.enigma.com/reference/data/entities/watchlist-entry/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/watchlist-entry/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesWatchlist EntryOn this pageWatchlist Entry
A watchlist entry drawn from publications of the Office of Foreign Assets Control (OFAC),
including:
Specially Designated Nationals and Blocked Persons List (SDN)
Consolidated Sanctions List (Non-SDN), which includes the Foreign Sanctions Evaders List
(FSE), Sectoral Sanctions Identifications List (SSI), Palestinian Legislative Council List
(PLC), CAPTA List, Non-SDN Menu-Based Sanctions List (NS-MBS), and the Non-SDN Chinese
Military-Industrial Complex Companies List (NS-CMIC).
GraphQL type: WatchlistEntry
ExampleA Watchlist Entry is a match on an OFAC sanctions list — for example, if a legal entity appeared on the SDN list.
Available from: Legal Entity
A watchlist entry for the entity.
Pricing tier: Premium
FieldNameTypeDescriptionWatchlist Namewatchlist_nameName of the watchlist, including SDN and Non-SDN.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Watchlist Entry connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←appears onAddress←appears onLegal Entity←is flagged byLegal Entity
View all relationships →Last updated on Apr 6, 2026PreviousTaxpayer Identification Number (TIN)NextWebsiteRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---
